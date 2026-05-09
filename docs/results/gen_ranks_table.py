import json
import yaml

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from textwrap import wrap

def calculate_ranks(config: dict) -> pd.DataFrame:
    ranks = {"endpoint": [], "language": []}
    for metric in config["metrics"]:
        ranks[metric] = []
    for endpoint in config["endpoints"]:
        try:
            with open(
                f"{config['dataset']}/{endpoint}/{config['dataset']}_results2.json", "r"
            ) as f:
                results = json.load(f)
        except FileNotFoundError:
            with open(
                f"{config['dataset']}/{endpoint}/{config['dataset']}_results.json", "r"
            ) as f:
                results = json.load(f)
        if len(config["languages"]) > 1:
            for language in config["languages"]:
                ranks["endpoint"].append(endpoint)
                ranks["language"].append(language)
                for metric in config["metrics"]:
                    ranks[metric].append(results[f"average-{language}"][metric])
        ranks["endpoint"].append(endpoint)
        ranks["language"].append("-")
        for metric in config["metrics"]:
            ranks[metric].append(results["average"][metric])
    
    ranks_group = (
        pd.DataFrame(ranks)
        .rename(columns=config["metrics_names"])
        .groupby("language")
        .apply(
            lambda x: x.sort_values(config["to_rank"], ascending=False).reset_index(
                drop=True
            ),
            include_groups=False,
        )
    )

    return ranks_group


def separate_ranks_by_language(ranks: pd.DataFrame, config: dict) -> dict:
    separated_ranks = {}
    for language in ranks.index.get_level_values("language").unique():
        separated_ranks[config["language_names"][language]] = ranks.xs(
            language, level="language"
        ).reset_index(drop=True).set_index(["endpoint", config["to_rank"]])
    return separated_ranks


def get_ranks_html(ranks: pd.DataFrame, ranks_html: str, config: dict) -> str:
    if len(ranks.columns) > 5:
        table_class = "with-order"
    else:
        table_class = "without-order"
    for language, ranks_language in separate_ranks_by_language(ranks, config).items():
        ranks_html += f"<h2>{language}</h2>\n"
        ranks_html += ranks_language.to_html(
            justify="center", classes=table_class, index_names=True
        )

    return ranks_html


def calculate_retries(config: dict) -> dict:
    retries = {}

    for endpoint in config["endpoints"]:
        retries[endpoint] = {"retries": 0, "skips": 0}
        with open(
            f"{config['dataset']}/{endpoint}/{config['dataset']}_retries.log", "r"
        ) as f:
            for line in f:
                if "WARNING" in line:
                    retries[endpoint]["retries"] += 1
                elif "ERROR" in line:
                    retries[endpoint]["skips"] += 1

    return retries


def generate_extra_info_html(config: dict, ranks: pd.DataFrame) -> None:
    retries = calculate_retries(config)
    for endpoint in config["endpoints"]:
        extra_info_html = """<html>
<head>
    <link rel="stylesheet" href="../../extra_style.css">
</head>
<body>
"""
        extra_info_html += f"<h2>Retries and skips for {endpoint}</h2>\n"
        extra_info_html += f"<p>Retries: {retries[endpoint]['retries']}</p>\n"
        extra_info_html += f"<p>Skips: {retries[endpoint]['skips']}</p>\n"
        if retries[endpoint]["retries"] > 0 or retries[endpoint]["skips"] > 0:
            extra_info_html += "<h3>Retries log:</h3>\n"
            with open(
                f"{config['dataset']}/{endpoint}/{config['dataset']}_retries.log", "r"
            ) as f:
                extra_info_html += "<p class='code'>\n"
                for line in f:
                    extra_info_html += f"{line}<br>\n"
                extra_info_html += "</p>\n"

        extra_info_html += f"<h2>Results per-language for {endpoint}</h2>\n"

        if endpoint in ranks["endpoint"].values:
            temp_df = (
                ranks.loc[ranks["endpoint"] == endpoint]
                .reset_index()
                .drop(columns=["level_1", "endpoint"])
            )
            temp_df["language"] = temp_df["language"].replace(
                {"-": "overall", "en": "english", "de": "german", "es": "spanish"}
            )
            extra_info_html += temp_df.set_index("language").T.to_html(
                justify="center", classes="per-language", index_names=False
            )

        extra_info_html += "<h3>Data collected per query:</h3>\n"
        # questions file
        with open(
            f"{config['dataset']}/{config['questions']}", "r"
        ) as f:
            questions_file = yaml.safe_load(f)
        # true result set
        with open(
            f"{config['dataset']}/{config['dataset']}_true_result_set.json", "r"
        ) as f:
            true_result_set = yaml.safe_load(f)
        # answers file
        for num in range(3, 0, -1):
            try:
                if num == 1:
                    with open(
                        f"{config['dataset']}/{endpoint}/{config['dataset']}_answers.json", "r"
                    ) as f:
                        answers_file = json.load(f)
                    break
                with open(
                    f"{config['dataset']}/{endpoint}/{config['dataset']}_answers{num}.json", "r"
                ) as f:
                    answers_file = json.load(f)
                break
            except FileNotFoundError:
                continue
        # returned result set
        for num in range(3, 0, -1):
            try:
                if num == 1:
                    with open(
                        f"{config['dataset']}/{endpoint}/{config['dataset']}_pred_result_set.json", "r"
                    ) as f:
                        pred_result_set = json.load(f)
                    break
                with open(
                    f"{config['dataset']}/{endpoint}/{config['dataset']}_pred_result_set{num}.json", "r"
                ) as f:
                    pred_result_set = json.load(f)
                break
            except FileNotFoundError:
                continue
        # results file
        for num in range(3, 0, -1):
            try:
                if num == 1:
                    with open(
                        f"{config['dataset']}/{endpoint}/{config['dataset']}_results.json", "r"
                    ) as f:
                        results_file = json.load(f)
                    break
                with open(
                    f"{config['dataset']}/{endpoint}/{config['dataset']}_results{num}.json", "r"
                ) as f:
                    results_file = json.load(f)
                break
            except FileNotFoundError:
                continue
        raw_results = {
            "id": [],
            "question": [],
            "standard query": [],
            "standard result set": [],
            "returned query": [],
            "returned result set": [],
            "scores": []
        }
        dict_answers = {res["qname"]: res["query"] for res in answers_file}
        for question in questions_file["questions"]:
            for lang in question["question"].keys():
                qname = f"{questions_file['dataset']['prefix']}:{question['id']}-{lang}"
                raw_results["id"].append(qname)
                raw_results["question"].append(f'TAG_START{"LINE_END".join(wrap(question["question"][lang], width=35))}TAG_END')
                raw_results["standard query"].append(f"TAG_START{question['query']['sparql']}TAG_END".replace("\n", "LINE_END"))
                raw_results["standard result set"].append(f"TAG_START{json.dumps(true_result_set[qname], indent=4)}TAG_END".replace("\n", "LINE_END"))
                raw_results["returned query"].append(f"TAG_START{dict_answers.get(qname, 'N/A')}TAG_END".replace("\n", "LINE_END"))
                raw_results["returned result set"].append(f"TAG_START{json.dumps(pred_result_set[qname], indent=4)}TAG_END".replace("\n", "LINE_END"))
                raw_results["scores"].append(f"TAG_START{json.dumps(results_file[qname], indent=4)}TAG_END".replace("\n", "LINE_END"))

        extra_info_html += pd.DataFrame(raw_results).set_index("id").to_html(
            justify="center", classes="raw-results", index_names=False, escape=True
        )
        extra_info_html = extra_info_html.replace("LINE_END", "<br>")
        extra_info_html = extra_info_html.replace("TAG_START", "<pre>")
        extra_info_html = extra_info_html.replace("TAG_END", "</pre>")

        extra_info_html += "\n</body>\n</html>"

        soup = BeautifulSoup(extra_info_html, "html.parser")
        with open(f"{config['dataset']}/{endpoint}/{endpoint}.html", "w") as f:
            f.write(soup.prettify())


def generate_extra_info_files(config: dict) -> None:
    for endpoint in config["endpoints"]:
        md_str = f"#{config['dataset'].upper()}: {endpoint} extras\n\n---\n\n"
        path_str = f"docs/results/{config['dataset']}/{endpoint}/{endpoint}.html"
        md_str += f'--8<-- "{path_str}"\n\n---\n'
        with open(f"{config['dataset']}/{endpoint}/index.md", "w") as f:
            f.write(md_str)


def add_links_md(ranks_html: str, config: dict) -> str:
    soup = BeautifulSoup(ranks_html, "html.parser")
    for tr in soup.find_all("tr"):
        th = tr.find("th")
        if th.text in config["endpoints"]:
            endpoint = th.text
            th.string = ""
            a = soup.new_tag("a", href=f"{config['dataset']}/{endpoint}/")
            a.string = endpoint
            th.append(a)
    return str(soup)


def get_ranks_overall_html(overall_ranks: dict, ranks_html: str, config: dict) -> str:
    for language, ranks_language in overall_ranks.items():
        ranks_html += f"<h2>{config['language_names'][language]}</h2>\n"
        ranks_html += ranks_language.to_html(
            justify="center", classes="without-order", index_names=True
        )

    return ranks_html


def merge_header(ranks_html: str) -> str:
    soup = BeautifulSoup(ranks_html, "html.parser")
    for table in soup.find_all("table"):
        for header in table.find_all("thead"):
            if len(header.find_all("tr")) > 1:
                row_zero = list(header.find("tr").find_all("th"))
                for row in header.find_all("tr")[1:]:
                    for idx, th in enumerate(row.find_all("th")):
                        if len(row_zero[idx].text) == 0:
                            row_zero[idx].string = th.text
                        th.decompose()
            else:
                print("Warning: table does not have multiple row header, skipping merge.")
    
    return str(soup)


def generate_separate_tables(config_paths: list) -> list:
    ranks_dfs = []

    for config_path in config_paths:
        ranks_html = """<html>
<head>
    <link rel="stylesheet" href="table_style.css">
</head>
<body>
"""
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        ranks_html += f"<h1>{config['dataset'].upper()} results</h1>"

        ranks = calculate_ranks(config)
        ranks_dfs.append(ranks)
        ranks_html = get_ranks_html(ranks, ranks_html, config)
        generate_extra_info_html(config, ranks)
        if config["generate_extra_md"]:
            generate_extra_info_files(config)
        ranks_html = add_links_md(ranks_html, config)
        ranks_html += "<br></br>"
        ranks_html += "\n</body>\n</html>"
        ranks_html = merge_header(ranks_html)

        soup = BeautifulSoup(ranks_html, "html.parser")
        with open(f"results_table_{config['dataset']}.html", "w") as f:
            f.write(soup.prettify())
    
    return ranks_dfs
    

def generate_overall_table(ranks_dfs: list) -> None:
    overall_config = "overall_config.yml"
    with open(overall_config, "r") as f:
        config = yaml.safe_load(f)
    ranks_html = """<html>
<head>
    <link rel="stylesheet" href="table_style.css">
</head>
<body>
"""
    ranks_html += "<h1>Overall results</h1>"
    overall_ranks = {language: [rank_df[["endpoint"] + config["metrics"]].xs(language) for rank_df in ranks_dfs] for language in config["language_names"].keys()}
    for language, ranks_df in overall_ranks.items():
        overall_ranks[language] = pd.concat(ranks_df).groupby("endpoint").mean().reset_index()
        overall_ranks[language] = overall_ranks[language].sort_values(config["to_rank"], ascending=False).reset_index(drop=True).set_index(["endpoint", config["to_rank"]])
    ranks_html = get_ranks_overall_html(overall_ranks, ranks_html, config)
    ranks_html += "\n</body>\n</html>"
    ranks_html = merge_header(ranks_html)
    soup = BeautifulSoup(ranks_html, "html.parser")
    with open("results_table_overall.html", "w") as f:
        f.write(soup.prettify())


def generate_page(config_paths):
    ranks_dfs = generate_separate_tables(config_paths)
    generate_overall_table(ranks_dfs)


def generate_charts(config_paths: list) -> None:
    ranks_dfs = []
    for config_path in config_paths:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        ranks = calculate_ranks(config)
        ranks_dfs.append(ranks)

        for language, lang_ranks in separate_ranks_by_language(ranks, config).items():
            lang_ranks_reset = lang_ranks.reset_index()
            plt.figure(figsize=(12, 6))
            sns.barplot(data=lang_ranks_reset, x="endpoint", y=config["to_rank"], palette="viridis", hue="endpoint", legend=False)
            plt.title(f"{config['dataset'].upper()} - {language}")
            plt.xlabel("Endpoint")
            plt.ylabel(config["to_rank"])
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f"{config['dataset']}/barplot_{language}.png", dpi=300, bbox_inches="tight")
            plt.close()

    # Generate overall results bar plots
    overall_config_path = "overall_config.yml"
    with open(overall_config_path, "r") as f:
        overall_cfg = yaml.safe_load(f)
    
    overall_ranks = {language: [rank_df[["endpoint"] + overall_cfg["metrics"]].xs(language) for rank_df in ranks_dfs] for language in overall_cfg["language_names"].keys()}
    for language, ranks_df_list in overall_ranks.items():
        combined_ranks = pd.concat(ranks_df_list).groupby("endpoint").mean().reset_index()
        combined_ranks = combined_ranks.sort_values(overall_cfg["to_rank"], ascending=False).reset_index(drop=True)
        
        plt.figure(figsize=(12, 6))
        sns.barplot(data=combined_ranks, x="endpoint", y=overall_cfg["to_rank"], palette="viridis", hue="endpoint", legend=False)
        plt.title(f"Overall - {overall_cfg['language_names'][language]}")
        plt.xlabel("Endpoint")
        plt.ylabel(overall_cfg["to_rank"])
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"overall_barplot_{overall_cfg['language_names'][language]}.png", dpi=300, bbox_inches="tight")
        plt.close()

        

if __name__ == "__main__":
    gen = "charts"

    config_paths = ["ck26_config.yml", "db26_config.yml"]

    # selector
    {"page": generate_page, "charts": generate_charts}[gen](config_paths)


---
icon: material/trophy
title: "Challenge"
---
<!-- markdownlint-disable MD012 MD013 MD024 MD033 -->
# Challenge

## Description

The TEXT2SPARQL’26 challenge is a benchmark designed to assess and enhance the ability of systems to translate natural language questions into SPARQL queries effectively. This task, central to Neural SPARQL Machines (NSpM), aims to bridge the gap between human language and structured knowledge representation. This challenge addresses the evolving needs of NSpM systems, emphasizing the importance of handling complex, multilingual datasets while maintaining accuracy and robustness.

Participants are tasked with developing models that can process natural language questions of varying complexity. These questions include counts, comparisons, and temporal aggregations, necessitating sophisticated parsing and query generation mechanisms. Furthermore, the challenge places significant importance on multilingualism, requiring systems to demonstrate their ability to operate across languages like English and Spanish. This push towards multilingual capabilities ensures broader accessibility and usability of NSpM systems in real-world scenarios.

### 🏆 Prize Announcement

We are thrilled to announce that this edition’s overall winner will walk away with a grand prize of 500 EUR!

## Knowledge Graphs for Evaluation

The evaluation process for the TEXT2SPARQL'26 challenge involves two distinct Knowledge Graphs (KGs), each selected to assess specific dimensions of model performance and adaptability.

### DBpedia (Large Knowledge Graph)

As one of the most comprehensive and widely used knowledge graphs, DBpedia represents a large-scale, open-domain dataset derived from Wikipedia. 
It contains a vast array of topics, relationships, and entities, providing a robust testing ground for models designed to handle complex, diverse, and large-scale data structures.

Evaluating on DBpedia measures a model's ability to:

- Scale effectively within vast information architectures.
  
- Navigate schema complexity across diverse domains.
  
- Manage queries involving extensive, real-world datasets.

The identifier for this dataset is: `https://text2sparql.aksw.org/2026/dbpedia/`

The dataset is available either as a single dump file or as multiple dump files.

- Single dump file:
  [dbpedia_text2sparql_full.zip](https://drive.google.com/file/d/1mvF6oEs1swBWVYxA3kKPmwcZ1_IUl9F0/view?usp=sharing)

- Multiple dump files:
  
??? example "Dumps"

    - [dbpedia_text2sparql_ontology.nt.bz2](https://drive.google.com/file/d/1lK-C6Ez3QolUxQfoYDHGQe07UQQQRup4/view?usp=sharing)
    
    - [labels_en.ttl.bz2](https://drive.google.com/file/d/1bHWdefNLsXQI_TCPH5nu5_ftlVKKZFrj/view?usp=sharing) 
    - [labels_es.ttl.bz2](https://drive.google.com/file/d/1fi6d1drUwJDhmJdeX3HPigUqmmbR2lIo/view?usp=sharing)

    - [short_abstracts_en.ttl.bz2](https://drive.google.com/file/d/1OkvC6RYGLpBOe3bJjWHRXt3vsAA02Yms/view?usp=sharing)
    - [short_abstracts_es.ttl.bz2](https://drive.google.com/file/d/1Ge6-OWqSk44ZTwHlnZ_UrB4nDRzQurej/view?usp=sharing)

    - [infobox_properties_en.ttl.bz2](https://drive.google.com/file/d/15ZtTNd0Kkkj37Q27fFnuqh_Lt77k4hVt/view?usp=sharing)
    - [infobox_properties_es.ttl.bz2](https://drive.google.com/file/d/1sG5oTnLPFBLV39b9zInjZ8hp5Fm55x6D/view?usp=sharing)

    - [instance_types_en.ttl.bz2](https://drive.google.com/file/d/1ZEv0FDmrARuyQFBJDOibwFOfOQZNAgk1/view?usp=sharing) 
    - [instance_types_es.ttl.bz2](https://drive.google.com/file/d/1qGLmj0UHxzikOxjPLCm_kQa2r-8XV7fn/view?usp=sharing)

    - [instance_types_transitive_en.ttl.bz2](https://drive.google.com/file/d/1kz5_E_oz5CDov7g1kefewhkBiIyTN9Oo/view?usp=sharing)
    - [instance_types_transitive_es.ttl.bz2](https://drive.google.com/file/d/1cmpxyn70Y6ZVYAjOO-EvQVpweJ1vWCEi/view?usp=sharing)

    - [mappingbased_literals_en.ttl.bz2](https://drive.google.com/file/d/1NnyQba3QeM58XdwyZO554YwGAF_VWwat/view?usp=sharing) 
    - [mappingbased_literals_es.ttl.bz2](https://drive.google.com/file/d/1HizVRlzFNEGk9jmrtxPQYmztCnWJjbrP/view?usp=sharing) 

    - [mappingbased_objects_en.ttl.bz2](https://drive.google.com/file/d/1xFVbZtwahv40uVYiX_K2Mcmd1L_9xh9F/view?usp=sharing) 
    - [mappingbased_objects_es.ttl.bz2](https://drive.google.com/file/d/1eiQre2K7JNt_-zVw6QoXJLlqKLdLJ2uK/view?usp=sharing) 

    - [persondata_en.ttl.bz2](https://drive.google.com/file/d/1_bEpXm8UNzGk43laXpUagwy9c25EEcj6/view?usp=sharing) 

### Corporate

This smaller, domain-specific knowledge graph represents a corporate setting, where the dataset is compact and highly specialized. It is designed to test a model's ability to adapt to restricted and domain-focused data environments. This evaluation highlights performance in scenarios where precision, domain relevance, and understanding of specialized ontologies are critical.

By evaluating models separately on these two knowledge graphs, the challenge ensures a comprehensive assessment of scalability, adaptability, and domain-specific reasoning. This dual evaluation also provides insights into the generalizability of models across knowledge graph sizes and complexities, reflecting real-world applications in both open-domain and specialized environments.

The identifier for this dataset is: `https://text2sparql.aksw.org/2026/corporate/`

#### 📢 ATTENTION
To ensure a level playing field and prioritize adaptable solutions, the dataset will be released just 24 hours prior to the evaluation. This approach emphasizes the importance of generalized methodologies over pre-existing dataset knowledge.

## Evaluation

### Training Set

The training set for this benchmark dataset is designed to facilitate the development of advanced models capable of translating natural language questions into SPARQL queries.
Participants are encouraged to leverage any publicly available resources on the web for training purposes, ensuring a broad and diverse foundation for model development.
This includes the use of existing Text2SPARQL benchmarks such as DBNQA, QALD, and LC-QuAD, which provide valuable question-query pairs spanning a variety of domains and complexities.
These resources offer rich datasets featuring diverse linguistic structures, logical formulations, and domain-specific ontologies, making them ideal for enhancing both the generalizability and precision of SPARQL query generation models.
By integrating insights from these established benchmarks and other freely available web resources, participants can build robust systems capable of handling the linguistic nuances and logical challenges inherent in natural language to SPARQL translation.

### Test Set

The test set along with the result will be available after individual candidate evaluation.

### Process

In order to attend the challenge, you have to deploy and provide your text2sparql service API somewhere on the web, and register your service for the challenge by adding your data to [CHALLENGERS.yaml](https://github.com/AKSW/text2sparql.aksw.org/blob/2026/CHALLENGERS.yaml).
Here is an example section you need to provide to us:

``` yaml
  example:
    api: "https://example.org/api/"
    authors:
      - name: "Max Muster"
        affiliation: "Group A @ Example University"
      - name: "Erika Muster"
        affiliation: "Group A @ Example University"
```

The deployed service needs to provide a simple API which is described in an [OpenAPI specification](https://petstore.swagger.io/?url=https://text2sparql.aksw.org/2026/openapi.json).
Basically you have to support two GET parameters, `dataset` and `question`.
In addition to that, here is an example implementation using FastAPI:

??? example

    ```python
    """text2sparql-api"""

    import fastapi

    app = fastapi.FastAPI(
        title="TEXT2SPARQL API Example",
    )

    KNOWN_DATASETS = [
        "https://text2sparql.aksw.org/2025/dbpedia/",
        "https://text2sparql.aksw.org/2025/corporate/"
    ]

    @app.get("/")
    async def get_answer(question: str, dataset: str):
        if dataset not in KNOWN_DATASETS:
            raise fastapi.HTTPException(404, "Unknown dataset ...")
        return {
            "dataset": dataset,
            "question": question,
            "query": "... SPARQL here ..."
        }
    ```

Your registration is done, if we merge your data into our repository.

<a id="self-evaluation"></a>In case you want to **self-evaluate your endpoint** with the same client and endpoints we are using for the evaluation, follow this recipe:

??? example "Self-Evaluation using the TEXT2SPARQL command line client"

    ``` bash
    # install the client (use your preferred way)
    $ pipx install text2sparql-client

    # clone the text2sparql-client-examples repository
    $ git clone https://github.com/AKSW/text2sparql-client-examples

    # enter the root directory of the repository that contains reduced questions and true result-set files that can be executed together with a prepared evaluation shell script
    $ cd text2sparql-client-examples

    # with the URL of your API in hands you can run the evaluation script `run_api_ok.sh` passing `<API_URL> <API_NAME>` as parameters, e.g.:
    $ bash run_api_ok.sh "http://localhost:8000" "text2sparql"
    Running ask, query and evaluate for all questions and responses for text2sparql at http://localhost:8000
    2026-03-03 11:53:23.292 | INFO     | text2sparql_client.commands.ask:ask_command:159 - Asking questions about dataset https://text2sparql.aksw.org/2025/corporate/ on endpoint http://localhost:8000.
    2026-03-03 11:53:23.294 | INFO     | text2sparql_client.commands.ask:ask_command:165 - In which department is Ms. Brant? (en) ...
    2026-03-03 11:53:23.333 | INFO     | text2sparql_client.commands.ask:ask_command:165 - What is the telephone of Baldwin Dirksen? (en) ...
    2026-03-03 11:53:23.371 | INFO     | text2sparql_client.commands.ask:ask_command:165 - Who is the manager of Heinrich Hoch? (en) ...
    2026-03-03 11:53:23.409 | INFO     | text2sparql_client.commands.ask:ask_command:165 - What is the email of Sabrina from Marketing? (en) ...
    2026-03-03 11:53:23.447 | INFO     | text2sparql_client.commands.ask:ask_command:200 - Writing 4 responses to api_results/text2sparql_api_ok_answers.json.
    100%|███████████████████████████████████████████████████████████████████████████████████| 4/4 [00:00<00:00, 20.84it/s]
    2026-03-03 11:53:23.928 | INFO     | text2sparql_client.commands.query:query_command:142 - Writing 4 results to api_results/text2sparql_api_ok_pred_result_set.json.
    2026-03-03 11:53:24.214 | INFO     | text2sparql_client.commands.evaluate:evaluate_command:114 - Writing 5 results to api_results/text2sparql_api_ok_results.json.
    
    # check the results in `api_results/` and see if the following files are created:
    $ ls api_results/
    text2sparql_api_ok_answers.db    text2sparql_api_ok_pred_result_set.json  text2sparql_api_ok_retries.log
    text2sparql_api_ok_answers.json  text2sparql_api_ok_results.json
    # if you see these results your API is working fine and you can expect to be evaluated without any problems in the official evaluation with Text2SPARQL'26 questions.

    # additionally you can execute your API with Text2SPARQL'25 questions' and evaluate the results for a more in-depth testing ahead of the official evaluation with Text2SPARQL'26 questions by accessing the corporate dataset:
    $ cd examples_ck25
    $ bash run_ck25.sh "http://localhost:8000" "text2sparql"
    # or the dbpedia multilingual dataset:
    $ cd examples_db25
    $ bash run_db25.sh "http://localhost:8000" "text2sparql"
    ```

For all kinds of problems or other communication, simply create a [repository issue](https://github.com/AKSW/text2sparql.aksw.org/issues).
We will do the same, if we have issues with your service.


### Metrics

Evaluation in the TEXT2SPARQL challenge is centred on robust, well-established metrics tailored to the nuances of TEXT2SPARQL tasks.
These include Precision, Recall, and F1-score.
Precision assesses the proportion of correct answers among those returned by the system, highlighting accuracy.
Recall evaluates the system's ability to retrieve all relevant answers, emphasizing coverage.
F1-score, a harmonic mean of Precision and Recall, provides a balanced measure that considers both the quality and completeness of the answers.
For queries where the order of results matters—such as those involving sorting or ranking—**nDCG (normalized Discounted Cumulative Gain)** is employed to evaluate how effectively the system ranks relevant answers higher in the result list.

Beyond these metrics, the challenge incorporates an analysis of query complexity.
This involves evaluating the structural features of generated SPARQL queries, such as the number of triple patterns, joins, and modifiers like LIMIT and GROUP BY.
This complexity analysis provides deeper insights into the system's capability to handle diverse and intricate queries.
By combining quantitative metrics with complexity analysis, the evaluation framework ensures a comprehensive assessment of NSpM systems, pushing the boundaries of their capabilities and fostering innovation in the field.


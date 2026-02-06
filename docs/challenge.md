---
icon: material/trophy
title: "Challenge"
---
<!-- markdownlint-disable MD012 MD013 MD024 MD033 -->
# Challenge

## Description

TBD

## Knowledge Graphs for Evaluation

TBD

## Evaluation

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

    ``` python
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

<a id="self-evaluation"></a>In case you want to **self-evaluate your endpoint** with the same client we are using for the evaluation, follow this recipe:

??? example "Self-Evaluation using the TEXT2SPARQL command line client"

    ``` bash
    # Install the client (use your preferred way)
    $ pipx install text2sparql-client

    # prepare a questions file like this
    $ cat questions.yaml
    ---
    dataset:
      id: https://text2sparql.aksw.org/2025/corporate/
    questions:
    
      - question:
          en: In which department is Ms. Müller?
          de: In welcher Abteilung ist Frau Müller?
    
      - question:
          de: Was ist der Sinn des Lebens?
    
      - question:
          de: Wieviele Einwohner hat Leipzig?

    # Ask questions from the questions file on your endpoint
    $ text2sparql ask questions.yml [YOUR-API-URL]
    Asking questions about dataset https://text2sparql.aksw.org/2025/corporate/ on endpoint [YOUR-API-URL].
    In which department is Ms. Müller? (en) ... done
    ...
    ```

For all kinds of problems or other communication, simply create a [repository issue](https://github.com/AKSW/text2sparql.aksw.org/issues).
We will do the same, if we have issues with your service.


### Metrics

Evaluation in the TEXT2SPARQL challenge is centred on robust, well-established metrics tailored to the nuances of TEXT2SPARQL tasks.
These include Precision, Recall, and F1-score.
Precision assesses the proportion of correct answers among those returned by the system, highlighting accuracy.
Recall evaluates the system's ability to retrieve all relevant answers, emphasizing coverage.
F1-score, a harmonic mean of Precision and Recall, provides a balanced measure that considers both the quality and completeness of the answers.

Beyond these metrics, the challenge incorporates an analysis of query complexity.
This involves evaluating the structural features of generated SPARQL queries, such as the number of triple patterns, joins, and modifiers like LIMIT and GROUP BY.
This complexity analysis provides deeper insights into the system's capability to handle diverse and intricate queries.
By combining quantitative metrics with complexity analysis, the evaluation framework ensures a comprehensive assessment of NSpM systems, pushing the boundaries of their capabilities and fostering innovation in the field.


---
icon: material/trophy
title: "Challenge"
---
<!-- markdownlint-disable MD012 MD013 MD024 MD033 -->
# Challenge

## Description

The TEXT2SPARQL’26 challenge is a benchmark designed to assess and enhance the ability of systems to translate natural language questions into SPARQL queries effectively. This task, central to Neural SPARQL Machines (NSpM), aims to bridge the gap between human language and structured knowledge representation. This challenge addresses the evolving needs of NSpM systems, emphasizing the importance of handling complex, multilingual datasets while maintaining accuracy and robustness.

Participants are tasked with developing models that can process natural language questions of varying complexity. These questions include counts, comparisons, and temporal aggregations, necessitating sophisticated parsing and query generation mechanisms. Furthermore, the challenge places significant importance on multilingualism, requiring systems to demonstrate their ability to operate across languages like English and Spanish. This push towards multilingual capabilities ensures broader accessibility and usability of NSpM systems in real-world scenarios.

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


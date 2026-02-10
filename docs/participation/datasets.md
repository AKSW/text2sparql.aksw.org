---
icon: material/database
---
# :material-database: Call for Participation

## How to contribute

This task invites the community to contribute high-quality Question Answering (QA) datasets to expand the TEXT2SPARQL benchmark suite. 
The goal is to enrich the ecosystem with diverse data sources, particularly focusing on low-resource languages, domain-specific knowledge graphs, and complex query structures.

We encourage submissions of both novel datasets and existing datasets that have not yet been integrated into standard benchmarks.

## Participation Guidelines

Datasets must contain pairs of Natural Language (NL) questions and their corresponding SPARQL queries executable on a specific Knowledge Graph (e.g., DBpedia, Wikidata, or custom domain KGs).
The question/answer pairs dataset can also be followed by a not yet published Knowledge Graph.

**Focus Areas**: We are particularly interested in:

- Multilingualism: Datasets covering languages other than English.

- Complexity: Questions requiring advanced SPARQL features (aggregations, filters, nesting).

- Domain Specificity: Datasets focused on specialized domains (e.g., biomedical, legal, finance).

**Format**: The quesion/answers pairs should be published in the same format as Text2SPARQL benchmark dataset as follows:

??? example "Dataset"

    ---
    dataset:
      id: https://text2sparql.aksw.org/2025/dbpedia/
      prefix: db25
      defaultNamespace: http://dbpedia.org/
    questions:
      - id: 1
        question:
          en: How many unique authors have written science fiction novels?
          es: ¿Cuántos autores únicos han escrito novelas de ciencia ficción?
        query:
          sparql: |
            SELECT DISTINCT COUNT(?author) WHERE {  
              ?x <http://dbpedia.org/ontology/literaryGenre> <http://dbpedia.org/resource/Science_fiction> .  
              ?x <http://dbpedia.org/ontology/author> ?author .
            }
    ...
  

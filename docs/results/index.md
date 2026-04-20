---
icon: material/chart-bar
title: "Results"
---
# Results

!!! info "2026-04-20 - Endpoint Responses"

    The [:simple-github: results directory](https://github.com/AKSW/text2sparql.aksw.org/tree/2026/docs/results) contains two folders for the datasets [CK26 dataset](https://github.com/AKSW/text2sparql.aksw.org/tree/2026/docs/results/ck26/questions_ck26.yml) and [DB26 dataset](https://github.com/AKSW/text2sparql.aksw.org/tree/2026/docs/results/db26/questions_db26.yml).
    Each folder contains the results for the respective dataset according to the endpoint IDs in the [CHALLENGERS.yaml](https://github.com/AKSW/text2sparql.aksw.org/blob/2026/CHALLENGERS.yaml).

    In each subfolder you will find the following files:

    - `*_answers.json` - the result of the requested queries per respective dataset and endpoint in the correct folders.
    - `*_responses.db` - the database file of the responses per respective dataset and endpoint in the correct folders.
    - `*_retries.log` - the retries log when the endpoint did not respond within the timeout or returned a connection error per respective dataset and endpoint in the correct folders.

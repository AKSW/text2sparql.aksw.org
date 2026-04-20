#!/usr/bin/env bash
# @(#) run ask, query and evaluate for all questions and responses
# Use the unofficial bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail; export FS=$'\n\t'

declare -A URLS=()
URLS[ADFR]="https://grasp.cs.uni-freiburg.de/text2sparql-2026/"
URLS[IRIS]="https://insanalex-iris-at-text2sparql.hf.space/text2sparql"
URLS[SPARQL-LLM]="https://biosoda.unil.ch/sparql-llm/"
URLS[LIBER-AI-CLAUDE]="http://research.liberai.org:8000/m/claude-sonnet-4.6/answer"
URLS[LIBER-AI-QWEN]="http://research.liberai.org:8000/m/qwen3.5-122b-a10b/answer"
URLS[INFAI-ETI-AND-FRIENDS-A]="https://26a.text2sparql.cc-eti.org/text2sparql"
URLS[INFAI-ETI-AND-FRIENDS-B]="https://26b.text2sparql.cc-eti.org/text2sparql"
URLS[INFAI-ETI-AND-FRIENDS-C]="https://26c.text2sparql.cc-eti.org/text2sparql"

API_ID=${1:-}

echo "Running ask, query and evaluate for all questions and responses for $API_ID at ${URLS[$API_ID]}"
mkdir -p "${API_ID}"
text2sparql ask -o "${API_ID}/ck26_answers.json" --timeout 180 --answers-db "${API_ID}/ck26_answers.db" --retries-log "${API_ID}/ck26_retries.log" questions_ck26.yml "${URLS[$API_ID]}"
text2sparql query -o "${API_ID}/ck26_pred_result_set.json" -a "${API_ID}/ck26_answers.json" -l "['en', 'de']" questions_ck26.yml
text2sparql evaluate -o "${API_ID}/ck26_results.json" -l "['en', 'de']" "${API_ID}" ck26_true_result_set.json "${API_ID}/ck26_pred_result_set.json"

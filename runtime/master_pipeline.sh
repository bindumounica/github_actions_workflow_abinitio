#!/bin/bash
set -e   # 🚨 critical line

echo "[PIPELINE] Starting master pipeline"

echo "[PIPELINE] Running user_flow_etl"
docker run --rm \
  -e INPUT_DATA='{"input_dataset":"s3://raw/users"}' \
  bindumounica87/etl-component:graph-user-flow-v1.1.1

echo "[PIPELINE] user_flow_etl completed successfully"

echo "[PIPELINE] Running downstream transformation"
docker run --rm \
  -e INPUT_DATA='{"source":"user_flow_output"}' \
  bindumounica87/enrich-component:v1

echo "[PIPELINE] Downstream transformation completed"

echo "[PIPELINE] Master pipeline completed successfully"

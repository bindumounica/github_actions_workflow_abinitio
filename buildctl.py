#!/bin/bash
set -e

NAME=$1
GRAPH_OUT=$2

echo "Generating ETL component from graph: $NAME"
echo "Graph output path: $GRAPH_OUT"

INTERFACE_FILE="$GRAPH_OUT/$NAME/interface.yaml"

if [[ ! -f "$INTERFACE_FILE" ]]; then
  echo "ERROR: interface.yaml not found at $INTERFACE_FILE"
  echo "Directory contents:"
  ls -R "$GRAPH_OUT"
  exit 1
fi

mkdir -p etl-component/runtime/$NAME

cp "$INTERFACE_FILE" etl-component/component.yaml

cat <<EOF >> etl-component/component.yaml

runtime: container
componentName: ${NAME}-etl
EOF

echo "ETL component generated successfully"

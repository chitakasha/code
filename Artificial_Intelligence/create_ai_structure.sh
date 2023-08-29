#!/bin/bash

# Read instructions.txt line by line
while read -r line; do
  # Skip comments
  [[ "$line" =~ ^#.*$ ]] && continue

  # Create directory or file based on the instruction
  if [[ "$line" =~ ^DIR ]]; then
    mkdir -p "${line#DIR }"
  elif [[ "$line" =~ ^FILE ]]; then
    touch "${line#FILE }"
  fi
done < instructions_ai.txt

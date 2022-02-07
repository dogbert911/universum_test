#!/usr/bin/env sh

TEXT="${1:-Some text}"  
LINE_NUM="${2:-10}"
OUT="${3:-1}" # Redirect to: 1 - stdut; 2 - stderr
EXIT_CODE=${4:-0} 

for i in $(seq ${LINE_NUM}); do
    echo "${i} ${TEXT}" >&$OUT
done

echo "Exit code: ${EXIT_CODE}"
exit ${EXIT_CODE} 

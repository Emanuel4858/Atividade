#!/bin/bash
for i in {1..3}; do
	n=$((RANDOM % 19 + 5))
	touch "${N}.txt"
done

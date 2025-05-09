#!/bin/bash
echo "Bom Dia!, $USER!"
echo "Hoje é $(date '+%A, %d de %B de %Y')"
echo -n "Uso de CPU atual: "

cpu_usage() {
	PREV_IDLE=$(awk '/^cpu / {print $5}' /proc/stat)
	PREV_TOTAL=$(awk '/^cpu / {sum=0; for(i=2;i<=NF;i++) sum+=$i; print sum}' /proc/stat)
	sleep 1
	IDLE=$(awk '^cpu / {print $5}' /proc/stat)
	TOTAL=$(awk '/^cpu / {sum=0; for(i=2;i<=NF;i++) sum+=$i; print sum}' /proc/stat)

	DIFF_IDLE=$((IDLE - PREV_IDLE))
	DIFF_TOTAL=$((TOTAL - PREV_TOTAL))
	DIFF_USAGE=$((100 * (DIFF_TOTAL - DIFF_IDLE) / DIFF_TOTAL))

	echo "Uso de CPU atual: $DIFF_USAGE%"
}
cpu_usage

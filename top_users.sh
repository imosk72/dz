cat $1 | awk '{print $4}' | sort | uniq -c | sort -r | awk 'BEGIN {printed = 0} {if (printed < 10) {print $2} printed++}'

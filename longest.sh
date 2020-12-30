sort -r -nk5 $1 | awk 'BEGIN {printed = 0} {if (printed < 10) {print $0} printed++}'

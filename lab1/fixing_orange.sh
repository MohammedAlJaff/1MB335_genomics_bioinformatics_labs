#!/bin/bash

# Basic substituion and transformation flow. 
# 1. substitue all commas with a . 
# then replace all semmicolons with comma 
# replace tabs with comma 
# deal with letters at end of and inside numbers.

sed 's/,/./g' orange.csv \
| sed 's/;/,/g' \
| sed 's/	/,/g' \
| sed  -E 's/[a-z]+//g' \
> orange_juice.txt

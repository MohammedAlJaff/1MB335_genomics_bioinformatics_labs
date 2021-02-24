#!/bin/bash

## filter out the inital results of the tblast outfile based on a threshold e-value... in this case : 
# 1. 0.0001 = 274 hits/lines
# 2. 0.001 = 288 hits/lines
# 3. 0.00001 = 253 hits/lines

awk '$11 < 0.00001 {print}' < tblastx_blast_outfile_for_C_elegans.blast | wc -l 

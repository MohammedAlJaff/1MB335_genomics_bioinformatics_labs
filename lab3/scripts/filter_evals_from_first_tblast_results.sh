#!/bin/bash

## filter out the inital results of the tblast outfile based on a threshold e-value... in this case : 
# 1. 0.0001

awk '$11 < 0.0001 {print}' < tblastx_blast_outfile_for_C_elegans.blast | wc -l 
#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
python3 ../src/h1b_counting.py ./tests/test_1/input/h1b_input.csv ./tests/test_1/output/top_10_occupations.txt ./tests/test_1/output/top_10_states.txt

python3 ../src/h1b_counting.py ./tests/your-own-test_1/input/h1b_input.csv ./tests/your-own-test_1/output/top_10_occupations.txt ./tests/your-own-test_1/output/top_10_states.txt

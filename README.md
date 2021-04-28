# Coding Task

This repository contains the solution to a coding task given as part of the interview process for a position at Analyze Re. It is a simple command line utility that reads in tabular numeric data from standard input, does some basic processing on the data, and prints out the result. The task is outlined in detail at: https://github.com/analyzere/problem_readme/.

The code can be run on a sample input text file via the following command in terminal:

cat input.txt | python compute.py [threshold value] [limit value]

Here threshold value and limit value are numeric arguments supplied by the user that act as parameters for the data processing step. They can be given as either integer or floating-point-style numbers (so 0, 0., 0.0, and 0.000 would all be valid input formats for the number zero).
# Data Cleaning & Structural Validation

## Objective
Clean a messy dataset by removing duplicates, handling missing values,
standardizing columns and categorical strings, converting dates, and validating data types.

## Files
- sample_dataset.csv - sample messy dataset
- data_cleaning.py - Pandas cleaning script
- cleaned_dataset.csv - generated cleaned dataset
- README.md - project documentation

## Cleaning Decisions
1. Duplicate rows are removed to avoid double-counting.
2. Missing numeric values are replaced with the median.
3. Missing categorical values are replaced with the mode.
4. Column headers are converted to lowercase snake_case.
5. Text values are stripped and converted to lowercase.
6. Date fields are converted using pandas.to_datetime.
7. Final null counts, duplicate counts, and data types are validated.

## Requirements
Python 3.x
Pandas

## Installation
pip install pandas

## Run
python data_cleaning.py

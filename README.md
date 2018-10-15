# CSV-Aggregator
This program aggregates the data in a CSV file and reports the frequency of the values in each column.

Usage: ``python csva.py <file path> [columns]``

Notes:
* Reports are automatically sorted in descending order of frequency.
* Any number of columns can be specified. If none are specified, every column will be reported.
* If a column has any spaces in its name, it cannot be passed as an argument. This is a bug and I'll probably fix it in the future.


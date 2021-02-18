Application to collect cancer genomics data and summarize it.

Run locally by doing the following:

1) Download project from GitHub.
2) Enter terminal.
3) Navigate to project folder.
4) Run 'pipenv shell' in terminal to enter the pipenv shell (requires pipenv downloaded on computer).
5) Run 'pipenv install -r requirements.txt' to install all dependencies (only needed first time).
7) Run 'python setup.py {gene_names}' to run program.

You can view information about the arguments for the program by running 'python setup.py -h'.

Runtime args:
setup.py [-h] [--clear_cache] [gene_names ...]
-h, --help: Show help message for program.
--clear_cache  If this flag is present, the local cache will be cleared before running.
gene_names:  A list of n strings representing the genes to summarize (1 ≤ n ≤ 3).
 
You can run the automated tests for the program by running 'pytest' in the terminal.
You can view more verbose details on the test by adding the '-v' or '-vv' flag to the pytest command.
You can run tests in parallel batches of size INT by adding the '-n INT' argument to the pytest command.

Potential Improvements:
- Currently all tests are done with clearing the cache to make sure old results don't mess up tests.  Testing could be improved to actually test cache functionality and how it influences the program.
- Allowing for user input for the file to use for the gene name to gene id mapping could be supported.
- Allowing for user input for the database to use instead of always doing gbm_tcga could be supported.
- More detailed information about the mutations and copy alterations, such as exact counts or lists of samples where they are present, could be included.
 
This program is made in python version 3.9.

# This file is the main file for running this program.

import argparse
from geneSummarizer import summarize_genes

# The main function that is run when starting the program.
# It takes in a list of arguments for genes to summarize.
# This list needs at least one gene and can't have more than three.
def main():
  parser = argparse.ArgumentParser(description="Arguments being passed to the cancer genomic data summarizer.")
  parser.add_argument("gene_names", type=str, nargs="*", 
                      help="A list of n strings representing the genes to summarize (1 ≤ n ≤ 3).")
  parser.add_argument("--clear_cache", action="store_true",
                      help="If this flag is present, the local cache will be cleared before running")
  args = parser.parse_args()
  number_of_genes = len(args.gene_names)
  if (number_of_genes < 1) or (number_of_genes > 3):
    print("Only supports 1 to 3 genes; you provided: " + str(number_of_genes))
  else:
    summarize_genes(args.gene_names, args.clear_cache)

if __name__ == "__main__":
  main()
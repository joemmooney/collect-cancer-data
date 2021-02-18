# This file contains all functions pertaining to testing geneSummarizer.

from apiRequestHandler import clear_cache
from geneSummarizer import get_gene_name_to_id_dict, print_mutation_alteration_info, summarize_genes

# A template for testing get_gene_name_to_id_dict that inputs the file name,
# a std_out string, and comparison dict.  Then it compares the printed results of the
# function to the std_out string and the results of the dictionary made to the comparison dictionary.
def get_gene_name_to_id_dict_test_template(capsys, file_name, std_out_string, comparison_dict):
    results = get_gene_name_to_id_dict(file_name)
    captured = capsys.readouterr()
    assert captured.out == std_out_string
    assert results == comparison_dict

# The specific tests for get_gene_name_to_id_dict.
def test_get_gene_name_to_id_dict_invalid(capsys):
    file_name = "invalid"
    std_out_string = "An error occurred trying to read in the file: invalid\n"
    comparison_dict = None
    get_gene_name_to_id_dict_test_template(capsys, file_name, std_out_string, comparison_dict)

def test_get_gene_name_to_id_dict_gene_results_5_tsv(capsys):
    file_name = "gene_results.5.tsv"
    std_out_string = ""
    comparison_dict = { "TP53": "7157", "EGFR": "1956", "TNF": "7124", "APOE": "348", "VEGFA": "7422" }
    get_gene_name_to_id_dict_test_template(capsys, file_name, std_out_string, comparison_dict)

# A template for testing print_mutation_alteration_info that inputs a list of gene names
# and ids and a std_out string.  Then it compares the printed results of the function to the std_out string.
def print_mutation_alteration_info_test_template(capsys, genes, std_out_string):
    clear_cache()
    print_mutation_alteration_info(genes)
    captured = capsys.readouterr()
    assert captured.out == std_out_string

# The specific tests for summarize_genes.
def test_print_mutation_alteration_info_invalid_single(capsys):
    genes = [("INVALID", "INVALID")]
    std_out_string = "Post request to get mutations for gene id INVALID failed with status code: 400\n" + \
                     "Can't get mutation and alteration info without list of samples mutated for gene: INVALID\n"
    print_mutation_alteration_info_test_template(capsys, genes, std_out_string)

def test_print_mutation_alteration_info_valid_single(capsys):
    genes = [("TP53", "7157")]
    std_out_string = "TP53 is mutated in 29% of all cases.\n" + \
                     "TP53 is copy number altered in 2% of all cases.\n" + \
                     "Cases with at least one mutation or copy number alteration in TP53: 30% of all cases.\n\n" + \
                     "Cases with at least one mutation or copy number alteration in one of the genes: 30% of all cases.\n" + \
                     "Cases with at least one mutation or copy number alteration in all the queried genes: 30% of all cases.\n"
    print_mutation_alteration_info_test_template(capsys, genes, std_out_string)

def test_print_mutation_alteration_info_invalid_multi(capsys):
    genes = [("TP53", "7157"), ("INVALID", "INVALID")]
    std_out_string = "TP53 is mutated in 29% of all cases.\n" + \
                     "TP53 is copy number altered in 2% of all cases.\n" + \
                     "Cases with at least one mutation or copy number alteration in TP53: 30% of all cases.\n\n" + \
                     "Post request to get mutations for gene id INVALID failed with status code: 400\n" + \
                     "Can't get mutation and alteration info without list of samples mutated for gene: INVALID\n"
    print_mutation_alteration_info_test_template(capsys, genes, std_out_string)

def test_print_mutation_alteration_info_valid_multi(capsys):
    genes = [("TP53", "7157"), ("MDM4", "4194")]
    std_out_string = "TP53 is mutated in 29% of all cases.\n" + \
                     "TP53 is copy number altered in 2% of all cases.\n" + \
                     "Cases with at least one mutation or copy number alteration in TP53: 30% of all cases.\n\n" + \
                     "MDM4 is mutated in less than 0.5% of all cases.\n" + \
                     "MDM4 is copy number altered in 10% of all cases.\n" + \
                     "Cases with at least one mutation or copy number alteration in MDM4: 10% of all cases.\n\n" + \
                     "Cases with at least one mutation or copy number alteration in one of the genes: 38% of all cases.\n" + \
                     "Cases with at least one mutation or copy number alteration in all the queried genes: 2% of all cases.\n"
    print_mutation_alteration_info_test_template(capsys, genes, std_out_string)

# A template for testing summarize_genes that inputs a list of gene names and a std_out string.
# Then it compares the printed results of the function to the std_out string.
def summarize_genes_test_template(capsys, gene_names, clear_cache, std_out_string):
    summarize_genes(gene_names, clear_cache)
    captured = capsys.readouterr()
    assert captured.out == std_out_string

# The specific tests for summarize_genes.
def test_summarize_genes_invalid_single(capsys):
    gene_names = ["INVALID"]
    clear_cache = True
    std_out_string = "Cleared cache\n" + \
                     "Gene INVALID was missing from the gene name to id file gene_results.1000.tsv\n"
    summarize_genes_test_template(capsys, gene_names, clear_cache, std_out_string)

def test_summarize_genes_valid_single(capsys):
    gene_names = ["TP53"]
    clear_cache = True
    std_out_string = "Cleared cache\n" + \
                     "TP53 is mutated in 29% of all cases.\n" + \
                     "TP53 is copy number altered in 2% of all cases.\n" + \
                     "Cases with at least one mutation or copy number alteration in TP53: 30% of all cases.\n\n" + \
                     "Cases with at least one mutation or copy number alteration in one of the genes: 30% of all cases.\n" + \
                     "Cases with at least one mutation or copy number alteration in all the queried genes: 30% of all cases.\n"
    summarize_genes_test_template(capsys, gene_names, clear_cache, std_out_string)

def test_summarize_genes_invalid_multi(capsys):
    gene_names = ["TP53", "INVALID"]
    clear_cache = True
    std_out_string = "Cleared cache\n" + \
                     "Gene INVALID was missing from the gene name to id file gene_results.1000.tsv\n"
    summarize_genes_test_template(capsys, gene_names, clear_cache, std_out_string)

def test_summarize_genes_valid_multi(capsys):
    gene_names = ["TP53", "MDM4"]
    clear_cache = True
    std_out_string = "Cleared cache\n" + \
                     "TP53 is mutated in 29% of all cases.\n" + \
                     "TP53 is copy number altered in 2% of all cases.\n" + \
                     "Cases with at least one mutation or copy number alteration in TP53: 30% of all cases.\n\n" + \
                     "MDM4 is mutated in less than 0.5% of all cases.\n" + \
                     "MDM4 is copy number altered in 10% of all cases.\n" + \
                     "Cases with at least one mutation or copy number alteration in MDM4: 10% of all cases.\n\n" + \
                     "Cases with at least one mutation or copy number alteration in one of the genes: 38% of all cases.\n" + \
                     "Cases with at least one mutation or copy number alteration in all the queried genes: 2% of all cases.\n"
    summarize_genes_test_template(capsys, gene_names, clear_cache, std_out_string)
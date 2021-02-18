# This file contains the functions for summarizing the gene mutations and alterations in the database.

import csv
from apiRequestHandler import get_all_samples, get_mutated_samples, get_altered_samples, clear_cache

# Loads in a dictionary mapping gene names to their ids in the online database.
# Args:
# file_name (str) - The name of the file to load the dictionary from.
def get_gene_name_to_id_dict(file_name):
    gene_name_to_id_dict = dict()
    try:
        gene_map_file = csv.reader(open(file_name, "r"))
        for geneId, geneName in gene_map_file:
            gene_name_to_id_dict[geneName] = geneId
        return gene_name_to_id_dict
    except:
        print("An error occurred trying to read in the file: " + file_name)
        return None

# Loads in a dictionary of genes to find mutation and alteration information on.
# Then, going through this dictionary, it prints a summary of the percentage of samples
# that are mutated or altered for each gene, and then prints a summary of the percentage
# of samples that are mutated or altered by any gene, and one for samples that are
# mutated or altered by each gene.
# Args:
# genes ((str, str)[]) - A list with gene name/id pairs to summarize.
def print_mutation_alteration_info(genes):
    # Collect all samples
    all_samples = get_all_samples()
    if all_samples == None:
        print("Can't get mutation and alteration info without list of all samples")
        return
    number_of_samples = len(all_samples)

    # Set up empty dicts to record mutations and alterations for each gene.
    mutated_samples = dict()
    altered_samples = dict()
    mutated_or_altered_samples = dict()

    # Go through each gene to find and print their mutations and alterations.
    for gene_name, gene_id in genes:
        # Find all samples that are mutated for the given gene and print the percentage of them.
        mutated_samples[gene_id] = get_mutated_samples(gene_id)
        if mutated_samples[gene_id] == None:
            print("Can't get mutation and alteration info without list of samples mutated for gene: " + gene_name)
            return
        number_of_samples_mutated = len(mutated_samples[gene_id])
        if number_of_samples < number_of_samples_mutated:
            print("The number of samples can't be less than the number of samples mutated in " +
                  gene_name + " - there must be an error")
            return
        percent_samples_mutated = round(number_of_samples_mutated / number_of_samples * 100)
        if number_of_samples_mutated > 0 and percent_samples_mutated == 0:
            print(gene_name + " is mutated in less than 0.5% of all cases.")
        elif number_of_samples_mutated < number_of_samples and percent_samples_mutated == 100:
            print(gene_name + " is mutated in more than 99.5% of all cases.")
        else:
            print(gene_name + " is mutated in " + str(percent_samples_mutated) + "% of all cases.")

        # Find all samples that are copy number altered for the given gene and print the percentage of them.
        altered_samples[gene_id] = get_altered_samples(gene_id)
        if altered_samples[gene_id] == None:
            print("Can't get mutation and alteration info without list of samples copy number altered for gene: " + gene_name)
            return
        number_of_samples_altered = len(altered_samples[gene_id])
        if number_of_samples < number_of_samples_altered:
            print("The number of samples can't be less than the number of samples copy number altered in " +
                  gene_name + " - there must be an error")
            return
        percent_samples_altered = round(number_of_samples_altered / number_of_samples * 100)
        if number_of_samples_altered > 0 and percent_samples_altered == 0:
            print(gene_name + " is copy number altered in less than 0.5% of all cases.")
        elif number_of_samples_altered < number_of_samples and percent_samples_altered == 100:
            print(gene_name + " is copy number altered in more than 99.5% of all cases.")
        else:
            print(gene_name + " is copy number altered in " + str(percent_samples_altered) + "% of all cases.")

        # Find all samples that are mutated or altered for the given gene and print the percentage of them.
        mutated_or_altered_samples[gene_id] = mutated_samples[gene_id] | altered_samples[gene_id]
        number_of_mutated_or_altered_samples = len(mutated_or_altered_samples[gene_id])
        if number_of_samples < number_of_mutated_or_altered_samples:
            print("The number of samples can't be less than the number of samples mutated or copy number altered " +
                  gene_name + " - there must be an error")
            return
        percent_mutated_or_altered_samples = round(number_of_mutated_or_altered_samples / number_of_samples * 100)
        if number_of_mutated_or_altered_samples > 0 and percent_mutated_or_altered_samples == 0:
            print("Cases with at least one mutation or copy number alteration in " + gene_name + ": less than 0.5% of all cases.\n")
        elif number_of_mutated_or_altered_samples < number_of_samples and percent_mutated_or_altered_samples == 100:
            print("Cases with at least one mutation or copy number alteration in " + gene_name + ": more than 99.5% of all cases.\n")
        else:
            print("Cases with at least one mutation or copy number alteration in " + gene_name + ": " +
                  str(percent_mutated_or_altered_samples) + "% of all cases.\n")
    
    # Find all samples that are mutated or altered for any of the genes and print the percentage of them.
    all_mutated_or_altered_samples = set()
    for sample_set in mutated_or_altered_samples.values():
        all_mutated_or_altered_samples = all_mutated_or_altered_samples | sample_set
    number_of_all_mutated_or_altered_samples = len(all_mutated_or_altered_samples)
    if number_of_samples < number_of_all_mutated_or_altered_samples:
        print("The number of samples can't be less than the number of all samples mutated or copy number altered" +
              " - there must be an error")
        return
    percent_all_mutated_or_altered_samples = round(number_of_all_mutated_or_altered_samples / number_of_samples * 100)
    if number_of_all_mutated_or_altered_samples > 0 and percent_all_mutated_or_altered_samples == 0:
        print("Cases with at least one mutation or copy number alteration in one of the genes: less than 0.5% of all cases.\n")
    elif number_of_all_mutated_or_altered_samples < number_of_samples and percent_all_mutated_or_altered_samples == 100:
        print("Cases with at least one mutation or copy number alteration in one of the genes: more than 99.5% of all cases.\n")
    else:
        print("Cases with at least one mutation or copy number alteration in one of the genes: " +
              str(percent_all_mutated_or_altered_samples) + "% of all cases.")
    
    # Find all samples that are mutated or altered for each of the genes and print the percentage of them.
    mutated_or_altered_samples_in_all = all_samples
    for sample_set in mutated_or_altered_samples.values():
        mutated_or_altered_samples_in_all = mutated_or_altered_samples_in_all & sample_set
    number_of_mutated_or_altered_samples_in_all = len(mutated_or_altered_samples_in_all)
    if number_of_samples < number_of_mutated_or_altered_samples_in_all:
        print("The number of samples can't be less than the number of samples mutated or copy number altered in each gene" +
              " - there must be an error")
        return
    percent_mutated_or_altered_samples_in_all = round(number_of_mutated_or_altered_samples_in_all / number_of_samples * 100)
    if number_of_mutated_or_altered_samples_in_all > 0 and percent_mutated_or_altered_samples_in_all == 0:
        print("Cases with at least one mutation or copy number alteration in all the queried genes: less than 0.5% of all cases.\n")
    elif number_of_mutated_or_altered_samples_in_all < number_of_samples and percent_mutated_or_altered_samples_in_all == 100:
        print("Cases with at least one mutation or copy number alteration in all the queried genes: more than 99.5% of all cases.\n")
    else:
        print("Cases with at least one mutation or copy number alteration in all the queried genes: " +
              str(percent_mutated_or_altered_samples_in_all) + "% of all cases.")

# Takes a list of gene names and matches them with their ids to send to the function
# that will figure out the information about their mutations and alterations.
# Args:
# gen_names (str[]) - The list of names of genes to use.
def summarize_genes(gene_names, clear_cache_bool):
    if clear_cache_bool:
        clear_cache()
        print("Cleared cache")
    gene_map_file_name = "gene_results.1000.tsv"
    gene_name_to_id_dict = get_gene_name_to_id_dict(gene_map_file_name)
    if gene_name_to_id_dict == None:
        print("Can't run program with empty mapping from file: " + gene_map_file_name)
        return
    for gene_name in gene_names:
        if not gene_name in gene_name_to_id_dict:
            print("Gene " + gene_name + " was missing from the gene name to id file " + gene_map_file_name)
            return
    print_mutation_alteration_info([(gene_name, gene_name_to_id_dict[gene_name]) for gene_name in gene_names])

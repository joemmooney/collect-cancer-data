# This file contains all functions pertaining to testing apiRequestHandler.

from apiRequestHandler import get_all_samples, get_mutated_samples, get_altered_samples, clear_cache

# Hardcoded sets of samples to use for verification.
all_samples = {
    'TCGA-06-0749-01', 'TCGA-06-5414-01', 'TCGA-28-1753-01', 'TCGA-06-2569-01', 'TCGA-06-0882-01',
    'TCGA-06-6697-01', 'TCGA-02-2486-01', 'TCGA-41-2573-01', 'TCGA-14-1825-01', 'TCGA-27-1836-01',
    'TCGA-06-5408-01', 'TCGA-06-0876-01', 'TCGA-28-6450-01', 'TCGA-19-5952-01', 'TCGA-32-2634-01',
    'TCGA-28-5213-01', 'TCGA-32-2638-01', 'TCGA-06-0132-01', 'TCGA-76-4925-01', 'TCGA-76-6285-01',
    'TCGA-26-6174-01', 'TCGA-06-6698-01', 'TCGA-06-2558-01', 'TCGA-06-5413-01', 'TCGA-27-2523-01',
    'TCGA-19-5951-01', 'TCGA-26-5132-01', 'TCGA-27-1832-01', 'TCGA-14-0790-01', 'TCGA-12-0821-01',
    'TCGA-06-0130-01', 'TCGA-15-0742-01', 'TCGA-06-6695-01', 'TCGA-06-0124-01', 'TCGA-41-5651-01',
    'TCGA-76-6280-01', 'TCGA-06-0241-01', 'TCGA-28-5215-01', 'TCGA-06-0939-01', 'TCGA-26-5136-01',
    'TCGA-06-0686-01', 'TCGA-06-0126-01', 'TCGA-16-1048-01', 'TCGA-06-0141-01', 'TCGA-28-5208-01',
    'TCGA-74-6578-01', 'TCGA-06-0129-01', 'TCGA-06-0142-01', 'TCGA-14-0789-01', 'TCGA-28-2502-01',
    'TCGA-32-1982-01', 'TCGA-14-0787-01', 'TCGA-19-5959-01', 'TCGA-06-0137-01', 'TCGA-16-0846-01',
    'TCGA-06-0644-01', 'TCGA-06-0169-01', 'TCGA-41-3392-01', 'TCGA-27-2528-01', 'TCGA-06-0646-01',
    'TCGA-14-0862-01', 'TCGA-06-0879-01', 'TCGA-06-0209-01', 'TCGA-26-6173-01', 'TCGA-76-6283-01',
    'TCGA-06-6701-01', 'TCGA-41-2571-01', 'TCGA-76-4926-01', 'TCGA-76-6282-01', 'TCGA-02-2483-01',
    'TCGA-19-2620-01', 'TCGA-32-1980-01', 'TCGA-32-1979-01', 'TCGA-28-2514-01', 'TCGA-26-1442-01',
    'TCGA-41-4097-01', 'TCGA-12-0619-01', 'TCGA-41-6646-01', 'TCGA-06-1804-01', 'TCGA-28-5216-01',
    'TCGA-06-0188-01', 'TCGA-02-2485-01', 'TCGA-32-1970-01', 'TCGA-06-0155-01', 'TCGA-19-5955-01',
    'TCGA-32-4211-01', 'TCGA-06-2570-01', 'TCGA-28-2513-01', 'TCGA-32-1991-01', 'TCGA-41-2572-01',
    'TCGA-76-6664-01', 'TCGA-26-1439-01', 'TCGA-76-6192-01', 'TCGA-16-0861-01', 'TCGA-14-1450-01',
    'TCGA-06-2564-01', 'TCGA-76-4935-01', 'TCGA-06-0192-01', 'TCGA-06-0152-01', 'TCGA-81-5911-01',
    'TCGA-06-0184-01', 'TCGA-06-5856-01', 'TCGA-41-3915-01', 'TCGA-28-5214-01', 'TCGA-06-6388-01',
    'TCGA-27-1834-01', 'TCGA-87-5896-01', 'TCGA-27-2521-01', 'TCGA-06-0154-01', 'TCGA-06-0744-01',
    'TCGA-76-6193-01', 'TCGA-06-0158-01', 'TCGA-74-6575-01', 'TCGA-76-4934-01', 'TCGA-06-0216-01',
    'TCGA-06-2559-01', 'TCGA-06-5410-01', 'TCGA-19-5960-01', 'TCGA-26-5135-01', 'TCGA-28-2510-01',
    'TCGA-27-1830-01', 'TCGA-32-2494-01', 'TCGA-14-0871-01', 'TCGA-06-0240-01', 'TCGA-27-2527-01',
    'TCGA-19-2623-01', 'TCGA-06-0237-01', 'TCGA-02-0033-01', 'TCGA-06-5859-01', 'TCGA-76-4928-01',
    'TCGA-41-2575-01', 'TCGA-76-4929-01', 'TCGA-76-6656-01', 'TCGA-32-2491-01', 'TCGA-14-1043-01',
    'TCGA-76-6660-01', 'TCGA-06-2562-01', 'TCGA-06-0145-01', 'TCGA-06-0650-01', 'TCGA-32-2615-01',
    'TCGA-28-5219-01', 'TCGA-26-5134-01', 'TCGA-06-0166-01', 'TCGA-06-0213-01', 'TCGA-27-1831-01',
    'TCGA-15-1444-01', 'TCGA-27-1833-01', 'TCGA-12-3650-01', 'TCGA-28-5209-01', 'TCGA-06-0238-01',
    'TCGA-06-5412-01', 'TCGA-19-2624-01', 'TCGA-14-2554-01', 'TCGA-19-2629-01', 'TCGA-76-6657-01',
    'TCGA-06-0178-01', 'TCGA-26-5139-01', 'TCGA-28-1747-01', 'TCGA-12-0618-01', 'TCGA-32-1977-01',
    'TCGA-06-6389-01', 'TCGA-16-1045-01', 'TCGA-06-2557-01', 'TCGA-74-6584-01', 'TCGA-06-0119-01',
    'TCGA-19-2625-01', 'TCGA-06-0173-01', 'TCGA-32-5222-01', 'TCGA-06-0645-01', 'TCGA-12-0688-01',
    'TCGA-06-0743-01', 'TCGA-06-0189-01', 'TCGA-06-0185-01', 'TCGA-26-5133-01', 'TCGA-14-0740-01',
    'TCGA-02-0055-01', 'TCGA-08-0386-01', 'TCGA-14-0786-01', 'TCGA-06-0151-01', 'TCGA-76-6191-01',
    'TCGA-32-2495-01', 'TCGA-06-0750-01', 'TCGA-12-5301-01', 'TCGA-76-6286-01', 'TCGA-19-5953-01',
    'TCGA-06-6390-01', 'TCGA-06-2563-01', 'TCGA-06-0214-01', 'TCGA-06-0157-01', 'TCGA-14-4157-01',
    'TCGA-12-5295-01', 'TCGA-06-0747-01', 'TCGA-06-5858-01', 'TCGA-06-0881-01', 'TCGA-02-0047-01',
    'TCGA-19-1390-01', 'TCGA-06-0165-01', 'TCGA-14-0781-01', 'TCGA-74-6573-01', 'TCGA-06-2567-01',
    'TCGA-76-4931-01', 'TCGA-12-0616-01', 'TCGA-28-5218-01', 'TCGA-06-0168-01', 'TCGA-14-0813-01',
    'TCGA-06-1806-01', 'TCGA-19-5950-01', 'TCGA-14-1829-01', 'TCGA-28-2501-01', 'TCGA-14-1456-01',
    'TCGA-06-2561-01', 'TCGA-06-6391-01', 'TCGA-76-6662-01', 'TCGA-06-6700-01', 'TCGA-27-1835-01',
    'TCGA-32-1986-01', 'TCGA-06-0128-01', 'TCGA-32-2632-01', 'TCGA-12-5299-01', 'TCGA-06-0219-01',
    'TCGA-32-4213-01', 'TCGA-06-0875-01', 'TCGA-06-0139-01', 'TCGA-19-5954-01', 'TCGA-06-6699-01',
    'TCGA-14-1395-01', 'TCGA-14-0817-01', 'TCGA-12-0692-01', 'TCGA-12-0615-01', 'TCGA-19-5947-01',
    'TCGA-28-5204-01', 'TCGA-76-6663-01', 'TCGA-27-1837-01', 'TCGA-06-0140-01', 'TCGA-81-5910-01',
    'TCGA-32-4208-01', 'TCGA-14-1823-01', 'TCGA-06-0877-01', 'TCGA-74-6577-01', 'TCGA-28-2509-01',
    'TCGA-12-3652-01', 'TCGA-06-0648-01', 'TCGA-32-4210-01', 'TCGA-06-0122-01', 'TCGA-27-1838-01',
    'TCGA-06-0745-01', 'TCGA-06-5411-01', 'TCGA-06-6693-01', 'TCGA-32-4719-01', 'TCGA-41-3393-01',
    'TCGA-27-2526-01', 'TCGA-28-5211-01', 'TCGA-06-6694-01', 'TCGA-02-0003-01', 'TCGA-19-2619-01',
    'TCGA-06-0878-01', 'TCGA-27-2518-01', 'TCGA-06-0174-01', 'TCGA-19-2631-01', 'TCGA-06-0195-01',
    'TCGA-28-5207-01', 'TCGA-19-5958-01', 'TCGA-06-5415-01', 'TCGA-06-2565-01', 'TCGA-12-3653-01',
    'TCGA-27-2524-01', 'TCGA-06-5418-01', 'TCGA-27-2519-01', 'TCGA-12-3649-01', 'TCGA-02-2470-01',
    'TCGA-76-6661-01', 'TCGA-06-0649-01', 'TCGA-28-5220-01'
}

# Id: 7157
tp53_samples_mutated = {
    'TCGA-28-1753-01', 'TCGA-06-2569-01', 'TCGA-14-1825-01', 'TCGA-27-1836-01', 'TCGA-06-5408-01',
    'TCGA-06-0876-01', 'TCGA-32-2634-01', 'TCGA-76-4925-01', 'TCGA-06-6698-01', 'TCGA-06-2558-01',
    'TCGA-06-0130-01', 'TCGA-41-5651-01', 'TCGA-06-0241-01', 'TCGA-28-5215-01', 'TCGA-26-5136-01',
    'TCGA-06-0129-01', 'TCGA-16-0846-01', 'TCGA-06-0644-01', 'TCGA-76-6283-01', 'TCGA-06-6701-01',
    'TCGA-02-2483-01', 'TCGA-26-1442-01', 'TCGA-12-0619-01', 'TCGA-28-5216-01', 'TCGA-06-0188-01',
    'TCGA-02-2485-01', 'TCGA-32-1970-01', 'TCGA-06-2570-01', 'TCGA-76-6664-01', 'TCGA-06-0184-01',
    'TCGA-06-0744-01', 'TCGA-27-2521-01', 'TCGA-76-6193-01', 'TCGA-76-4934-01', 'TCGA-06-2559-01',
    'TCGA-27-1830-01', 'TCGA-14-0871-01', 'TCGA-06-0237-01', 'TCGA-19-2623-01', 'TCGA-02-0033-01',
    'TCGA-41-2575-01', 'TCGA-76-4929-01', 'TCGA-32-2491-01', 'TCGA-15-1444-01', 'TCGA-06-0238-01',
    'TCGA-19-2629-01', 'TCGA-12-0618-01', 'TCGA-06-6389-01', 'TCGA-19-2625-01', 'TCGA-06-0743-01',
    'TCGA-06-0189-01', 'TCGA-26-5133-01', 'TCGA-14-0740-01', 'TCGA-02-0055-01', 'TCGA-76-6286-01',
    'TCGA-06-2563-01', 'TCGA-14-4157-01', 'TCGA-06-5858-01', 'TCGA-19-1390-01', 'TCGA-06-2567-01',
    'TCGA-74-6573-01', 'TCGA-14-0813-01', 'TCGA-14-1456-01', 'TCGA-76-6662-01', 'TCGA-27-1835-01',
    'TCGA-06-0128-01', 'TCGA-06-0875-01', 'TCGA-14-0817-01', 'TCGA-76-6663-01', 'TCGA-32-4208-01',
    'TCGA-28-2509-01', 'TCGA-32-4210-01', 'TCGA-27-1838-01', 'TCGA-06-6694-01', 'TCGA-02-0003-01',
    'TCGA-06-0195-01', 'TCGA-28-5207-01', 'TCGA-27-2519-01', 'TCGA-28-5219-01'
}

# Id: 7157
tp53_samples_altered = {
    'TCGA-06-0213-01', 'TCGA-06-0192-01', 'TCGA-16-0846-01', 'TCGA-41-2573-01', 'TCGA-06-0646-01'
}

# Id: 4194
mdm4_samples_mutated = {
    'TCGA-06-0129-01'
}

# Id: 4194
mdm4_samples_altered = {
    'TCGA-06-0240-01', 'TCGA-76-6662-01', 'TCGA-32-2632-01', 'TCGA-32-1979-01', 'TCGA-19-5952-01',
    'TCGA-32-4213-01', 'TCGA-02-2470-01', 'TCGA-41-6646-01', 'TCGA-12-0692-01', 'TCGA-19-2625-01',
    'TCGA-12-0821-01', 'TCGA-32-1991-01', 'TCGA-74-6577-01', 'TCGA-06-0185-01', 'TCGA-76-4935-01',
    'TCGA-06-5411-01', 'TCGA-06-0750-01', 'TCGA-27-1834-01', 'TCGA-16-1048-01', 'TCGA-06-0154-01',
    'TCGA-27-2518-01', 'TCGA-06-0157-01', 'TCGA-28-5207-01', 'TCGA-14-0787-01', 'TCGA-16-0846-01',
    'TCGA-28-5220-01'
}

# A test for get_all_samples that  compares the printed results of the
# function to a blank string and the results of the set made to the all_samples set.
def test_get_all_samples(capsys):
    clear_cache()
    results = get_all_samples()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert results == all_samples

# A template for testing get_mutated_samples that inputs the gene id,
# a std_out string, and comparison set.  Then it compares the printed results of the
# function to the std_out string and the results of the set made to the comparison set.
def get_mutated_samples_test_template(capsys, gene_id, std_out_string, comparison_set):
    clear_cache()
    results = get_mutated_samples(gene_id)
    captured = capsys.readouterr()
    assert captured.out == std_out_string
    assert results == comparison_set

# The specific tests for get_mutated_samples.
def test_get_mutated_samples_invalid(capsys):
    gene_id = "INVALID"
    std_out_string = "Post request to get mutations for gene id INVALID failed with status code: 400\n"
    comparison_set = None
    get_mutated_samples_test_template(capsys, gene_id, std_out_string, comparison_set)

def test_get_mutated_samples_tp53(capsys):
    gene_id = "7157"
    std_out_string = ""
    comparison_set = tp53_samples_mutated
    get_mutated_samples_test_template(capsys, gene_id, std_out_string, comparison_set)

def test_get_mutated_samples_mdm4(capsys):
    gene_id = "4194"
    std_out_string = ""
    comparison_set = mdm4_samples_mutated
    get_mutated_samples_test_template(capsys, gene_id, std_out_string, comparison_set)

# A template for testing get_altered_samples that inputs the gene id,
# a std_out string, and comparison set.  Then it compares the printed results of the
# function to the std_out string and the results of the set made to the comparison set.
def get_altered_samples_test_template(capsys, gene_id, std_out_string, comparison_set):
    clear_cache()
    results = get_altered_samples(gene_id)
    captured = capsys.readouterr()
    assert captured.out == std_out_string
    assert results == comparison_set

# The specific tests for get_altered_samples.
def test_get_altered_samples_invalid(capsys):
    gene_id = "INVALID"
    std_out_string = "Post request to get copy number alterations for gene id INVALID failed with status code: 400\n"
    comparison_set = None
    get_altered_samples_test_template(capsys, gene_id, std_out_string, comparison_set)

def test_get_altered_samples_tp53(capsys):
    gene_id = "7157"
    std_out_string = ""
    comparison_set = tp53_samples_altered
    get_altered_samples_test_template(capsys, gene_id, std_out_string, comparison_set)

def test_get_altered_samples_mdm4(capsys):
    gene_id = "4194"
    std_out_string = ""
    comparison_set = mdm4_samples_altered
    get_altered_samples_test_template(capsys, gene_id, std_out_string, comparison_set)
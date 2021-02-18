# This file contains the functions for making rest api calls.

import requests
import json
from beaker.cache import CacheManager
from beaker.cache import cache_managers
from beaker.util import parse_cache_config_options

# Stuff to set up local caching
cache_opts = {
    'cache.type': 'file',
    'cache.data_dir': '/tmp/cache/data',
    'cache.lock_dir': '/tmp/cache/lock'
}
cache = CacheManager(**parse_cache_config_options(cache_opts))

cache_verbose_names = {
    "get_all_samples": "apiRequestHandler_get_all_samples",
    "get_mutated_samples": "apiRequestHandler_get_mutated_samples",
    "get_altered_samples": "apiRequestHandler_get_altered_samples"
}

# Makes a get call to the cbioportal web api to get all samples for gbm_tcga.
@cache.cache(cache_verbose_names["get_all_samples"], type="file", expire=3600)
def get_all_samples():
    headers = { "Content-Type": "application/json" }
    url = "https://www.cbioportal.org/api/sample-lists/gbm_tcga_cnaseq"
    response = requests.get(url, headers = headers)
    if response.status_code != requests.codes.ok:
        print("Get request to get total sample count failed with status code: " + str(response.status_code))
        return None
    return set(response.json()["sampleIds"])

# Makes a post call to the cbioportal web api to get all samples with mutations
# for the gene_id given for gbm_tcga.
# Args:
# gene_id (str) - The unique id of the gene to get information regarding.
@cache.cache(cache_verbose_names["get_mutated_samples"], type="file", expire=3600)
def get_mutated_samples(gene_id):
    headers = { "accept": "application/json", "Content-Type": "application/json" }
    url = "https://www.cbioportal.org/api/molecular-profiles/gbm_tcga_mutations/mutations/fetch?" + \
          "direction=ASC&pageNumber=0&pageSize=10000000&projection=SUMMARY"
    params  = {
                "entrezGeneIds": [gene_id],
                "sampleListId": "gbm_tcga_cnaseq"
              }
    response = requests.post(url, json = params, headers = headers)
    if response.status_code != requests.codes.ok:
        print("Post request to get mutations for gene id " + gene_id + " failed with status code: " + str(response.status_code))
        return None
    responseJsonList = response.json()
    mutatedSampleSet = set([mutation["sampleId"] for mutation in responseJsonList])
    return mutatedSampleSet

# Makes a post call to the cbioportal web api to get alteration info for the gene_id given
# in all samples for gbm_tcga, and then filters them to only include samples where both
# copies of the gene are deleted or multiple copies of the gene are observed.
# Args:
# gene_id (str) - The unique id of the gene to get information regarding.
@cache.cache(cache_verbose_names["get_altered_samples"], type="file", expire=3600)
def get_altered_samples(gene_id):
    headers = { "accept": "application/json", "Content-Type": "application/json" }
    url = "https://www.cbioportal.org/api/molecular-profiles/gbm_tcga_gistic/discrete-copy-number/fetch?" + \
          "discreteCopyNumberEventType=ALL&projection=SUMMARY"
    params = {
                "entrezGeneIds": [gene_id],
                "sampleListId": "gbm_tcga_cnaseq"
             }
    response = requests.post(url, json = params, headers = headers)
    if response.status_code != requests.codes.ok:
        print("Post request to get copy number alterations for gene id " + gene_id +
              " failed with status code: " + str(response.status_code))
        return None
    responseJsonList = response.json()
    alteredSampleSet = set([alteration["sampleId"] for alteration in responseJsonList if abs(alteration["alteration"]) > 1])
    return alteredSampleSet

def clear_cache():
    for _cache in cache_managers.values():
        _cache.clear()
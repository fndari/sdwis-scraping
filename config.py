from pathlib import Path


PATH_INPUT = Path('./data-in')
PATH_DATA = Path('./data-out')

PATH_HTML_URLS = PATH_INPUT / 'wsd-urls-js-table.html'

PATH_URLS = PATH_DATA / 'wsd-urls.csv'

# change this number to set the number of URLs to process (-1 to process all of them)
# Running the whole dataset can be somewhat slow (~10 minutes) and memory-intensive (~3 GB)
# since the processing, especially the parsing, is not really optimized for performance
N_URLS_TO_PROCESS = 1000
# without the ".sqlite" suffix
PATH_REQUESTS_CACHE_DB = PATH_INPUT / 'requests-cache-db'

# N_URLS_TO_PROCESS = -1
# PATH_REQUESTS_CACHE_DB = Path('/data/datasets/parse-pws')

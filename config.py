from pathlib import Path

PATH_DATA = Path('./data')
# PATH_DATA = Path('/tmp/test-binder/data')

PATH_INPUT = PATH_DATA / 'input'
PATH_INTERMEDIATE_RESULTS = PATH_DATA / 'intermediate-results'
PATH_RESULTS = PATH_DATA / 'results'

PATH_HTML_URLS = PATH_INPUT / 'wsd-urls-js-table.html'

PATH_URLS = PATH_INTERMEDIATE_RESULTS / 'wsd-urls.csv'
PATH_HTML_PAGES = PATH_INTERMEDIATE_RESULTS / 'html-pages'
PATH_PARSED_RECORDS = PATH_INTERMEDIATE_RESULTS / 'parsed-records.json'

PATH_DATAPACKAGE = PATH_DATA / 'datapackage.zip'
PATH_DATAPACKAGE_METADATA = Path('./datapackage-metadata.yaml')

_PATH_ARCHIVES = PATH_DATA / 'archives'

_URL_REPO = 'https://github.com/fndari/sdwis-scraping/'
_URL_INPUT_DATA_ARCHIVE = _URL_REPO + 'releases/download/v0.1.0/input-data.zip'

_PATHS_TO_CREATE = [PATH_INPUT, PATH_INTERMEDIATE_RESULTS, PATH_RESULTS, PATH_HTML_PAGES]


def _create_paths(paths):
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)


# N_URLS_TO_FETCH = 1000
N_URLS_TO_FETCH = -1


_create_paths(_PATHS_TO_CREATE)

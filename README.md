Scraping and processing Water System data from HTML pages of the SDWIS portal of the California Water Boards.

# Running the notebooks

## Using Binder

The easiest way to run these notebooks interactively is via Binder:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fndari/sdwis-scraping/master).

NOTE: depending on the exact nature of the workflow, as well as other parameters (e.g. the amount of data to process/collect),
Binder users might encounter technical as well as usage limitations.
Make sure to check Binder's [Guidelines for users](https://mybinder.readthedocs.io/en/latest/user-guidelines.html) for more information.

## Manual installation

First, clone the Git repository:

```sh
git clone <url-for-this-repo> && cd sdwis-scraping
```

Then, install the dependencies using Conda. This will create and subsequently activate a virtual environment (virtualenv):

```sh
NAME='sdwis-scraping' && conda env create --name $NAME --file environment.yml && source activate $NAME
```

After activating the virtualenv, make it available as a kernel to existing Jupyter(Lab) installations:

```sh
python -m ipykernel install --user --name $NAME
```

# Getting the data

## Input data and intermediate results

Both the input data (required in the first notebook) and intermediate results (to avoid having to re-run every notebook in sequence, which can be time- and resource-consuming, especially for fetching the HTML pages) are available as ZIP archives.

The files are accessible from the [Releases section](https://github.com/fndari/sdwis-scraping/releases), under "Assets": 

- [Input data](https://github.com/fndari/sdwis-scraping/releases/download/v0.1.0/input-data.zip)
- [Intermediate results](https://github.com/fndari/sdwis-scraping/releases/download/v0.1.0/intermediate-results.zip)

To install them, download them and extract them to their respective appropriate location, i.e. as specified in `config.py`.

The input data can also be installed automatically:

```sh
invoke install-input-data
```

## Results

The resulting parsed data is released as a Datapackage. It is accessible at <https://github.com/waterdatacollaborative/sdwis-scraping-data>.

# Licensing

The code contained in this repository is released under a permissive MIT license.

The data collected and used for this example is publicly available and accessible.
Unless otherwise specified, the data is owned and managed by the California Water Boards, and distributed under an Open Data policy.
For more information, refer to <https://data.ca.gov/group/california-state-water-resources-control-board>.

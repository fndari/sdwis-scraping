Scraping and processing Water System data from HTML pages of the SDWIS portal of the California Water Boards.

# Running the notebooks

## Using Binder

The easiest way to run these notebooks interactively is via Binder: **TODO add URL/button**.

NOTE: depending on the exact nature of the workflow, as well as other parameters (e.g. the amount of data to process/collect),
Binder users might encounter technical as well as usage limitations.
Make sure to check Binder's [Guidelines for users](https://mybinder.readthedocs.io/en/latest/user-guidelines.html) for more information.

## Manual installation

First, clone the Git repository:

```sh
git clone <this-url> && cd sdwis-scraping
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

Both the input data (required in the first notebook) and intermediate results (to avoid having to re-run every notebook in sequence, which can be time- and resource-consuming, especially for fetching the HTML pages) are available as ZIP archives.

To use them, download them from **TODO: add URL** and extract them to their respective appropriate location, i.e. as specified in `config.py`.

The resulting parsed data is released as a Datapackage, available at **TODO: add URL**.

# Licensing

The code contained in this repository is released under a permissive MIT license.

The data collected and used for this example is publicly available and accessible.
Unless otherwise specified, the data is owned and managed by the California Water Boards, and distributed under an Open Data policy.
For more information, refer to <https://data.ca.gov/group/california-state-water-resources-control-board>.

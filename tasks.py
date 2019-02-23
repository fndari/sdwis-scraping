from invoke import task
from zipfile import ZipFile
from tqdm import tqdm

import config as c


@task
def package_input_data(ctx, path_archive=c.PATH_ARCHIVES / 'input-data.zip'):
    path_to_archive = c.PATH_HTML_URLS
    with ZipFile(path_archive, 'w') as z:
        z.write(path_to_archive, path_to_archive.name)
        print(z)

@task
def package_intermediate_results(ctx, path_archive=c.PATH_ARCHIVES / 'intermediate-results.zip'):
    path_to_archive = c.PATH_INTERMEDIATE_RESULTS
    to_archive = path_to_archive.rglob('*')

    with ZipFile(path_archive, 'w') as z:
        for path_source in tqdm(to_archive, unit=' files'):
            path_in_archive = path_source.relative_to(path_to_archive)
            z.write(path_source, path_in_archive)
        print(z)

from invoke import task
from pathlib import Path
from zipfile import ZipFile
from tqdm import tqdm


import config as c


@task
def package_input_data(ctx, path_archive=c._PATH_ARCHIVES / 'input-data.zip'):
    path_to_archive = c.PATH_HTML_URLS
    with ZipFile(path_archive, 'w') as z:
        z.write(path_to_archive, path_to_archive.name)
        print(z)

@task
def package_intermediate_results(ctx, path_archive=c._PATH_ARCHIVES / 'intermediate-results.zip'):
    path_to_archive = c.PATH_INTERMEDIATE_RESULTS
    to_archive = path_to_archive.rglob('*')

    with ZipFile(path_archive, 'w') as z:
        for path_source in tqdm(to_archive, unit=' files'):
            path_in_archive = path_source.relative_to(path_to_archive)
            z.write(path_source, path_in_archive)
        print(z)


@task
def install_input_data(ctx, url=c._URL_INPUT_DATA_ARCHIVE, path=c.PATH_INPUT):
    ctx.run(f'wget {url}', pty=True)
    path_archive = Path(Path(url).name)
    ZipFile(path_archive).extractall(path)
    ctx.run(f'ls -l {path}')
    path_archive.unlink()


def _format_datapackage(path):
    import json

    path = Path(path)

    data = json.loads(path.read_text())
    path.write_text(json.dumps(data, indent=4, separators=(', ', ': ')))

@task
def export_datapackage_to_repo(ctx, path_repo, datapackage_archive_path=c.PATH_DATAPACKAGE):
    path_repo = Path(path_repo)
    with ZipFile(datapackage_archive_path) as z:
        z.extractall(path_repo)
    
    _format_datapackage(path_repo / 'datapackage.json')
    
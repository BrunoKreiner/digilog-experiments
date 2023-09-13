# Python Project Template

A low dependency and really simple to start project template for Python Projects.

See also

- [Flask-Project-Template](https://github.com/rochacbruno/flask-project-template/) for a full feature Flask project including database, API, admin interface, etc.
- [FastAPI-Project-Template](https://github.com/rochacbruno/fastapi-project-template/) The base to start an openapi project featuring: SQLModel, Typer, FastAPI, JWT Token Auth, Interactive Shell, Management Commands.

### What is included on this template?

- 🖼️ Templates for starting multiple application types:
  * **Basic low dependency** Python program (default) [use this template](https://github.com/rochacbruno/python-project-template/generate)
  * **Flask** with database, admin interface, restapi and authentication [use this template](https://github.com/rochacbruno/flask-project-template/generate).
    **or Run `make init` after cloning to generate a new project based on a template.**
- 📦 A basic [setup.py](setup.py) file to provide installation, packaging and distribution for your project.Template uses setuptools because it's the de-facto standard for Python packages, you can run `make switch-to-poetry` later if you want.
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your project.
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🐋 A simple [Containerfile](Containerfile) to build a container image for your project.`Containerfile` is a more open standard for building container images than Dockerfile, you can use buildah or docker with this file.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- ✅ Code linting using [flake8](https://flake8.pycqa.org/en/latest/)
- 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
- 🛳️ Automatic release to [PyPI](https://pypi.org) using [twine](https://twine.readthedocs.io/en/latest/) and github actions.
- 🎯 Entry points to execute your program using `python -m <digilog_experiments>` or `$ digilog_experiments` with basic CLI argument parsing.

<!--  DELETE THE LINES ABOVE THIS AND WRITE YOUR PROJECT README BELOW -->

---

# digilog_experiments

[![codecov](https://codecov.io/gh/BrunoKreiner/digilog-experiments/branch/main/graph/badge.svg?token=digilog-experiments_token_here)](https://codecov.io/gh/BrunoKreiner/digilog-experiments)
[![CI](https://github.com/BrunoKreiner/digilog-experiments/actions/workflows/main.yml/badge.svg)](https://github.com/BrunoKreiner/digilog-experiments/actions/workflows/main.yml)

Awesome digilog_experiments created by BrunoKreiner

## Install it from PyPI

```bash
pip install digilog_experiments
```

## Usage

```py
from digilog_experiments import BaseClass
from digilog_experiments import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m digilog_experiments
#or
$ digilog_experiments
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

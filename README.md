The following steps need to be run in a terminal

# Requirements

There are three ways to setup your machine for the workshop, you should use the one that you are most familiar with. One is via conda, another via pyenv and the other with virtual env and pip.

- conda

OR

- pyenv >= 1.2.13
- python >= 3.7.0
- poetry >= 1.0.0 (to be installed in your local pyenv)

OR

- venv
- python >= 3.7.0

---

# Setup

Clone the repo locally:

```bash script
git clone https://github.com/wimlds/berlin-tdd-workshop
cd berlin-tdd-workshop
```

Choose your preferred setup:

with **conda**:

```bash script
# install working environment with conda
conda env create -n berlin-tdd-workshop -f environment.yml

# environment should be activated now
# if not type: source activate berlin-tdd-workshop
```

In case this fails, updating conda might help, run: `conda update -n base -c defaults conda`

With **pyenv and poetry**:

```bash script
pyenv local 3.7.4
pip install poetry
make setup                          #if you use a different python version update that in pyproject.toml
source .venv/bin/activate           #to activate the environment
```

With **venv**:

```bash script
todo: add .venv setup
pip install -r requirements.txt
source .venv/bin/activate           #to activate the environment
```

---

# Running test

Start environment and:

`pytest` or `pytest -vv` for verbose output

This should return tha a test has passed and some were skipped.

## Workshop

We prepared some data for the workshop, using a Pockets dataset from [the-pudding](https://github.com/the-pudding/). In order to try out different imputation methods we removed 10% of the price values. If you want to take a look at all the data check the [data/PrepareWorkshopData](data/PrepareWorkshopData.ipynb) notebook. We will not cover this through the workshop.

Walk through in [workshop.md](workshop.md)

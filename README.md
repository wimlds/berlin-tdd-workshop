## Requirements

0. conda

OR

1. poetry >= 1.0.0
2. pyenv >= 1.2.13
3. python >= 3.7.0

## Setup

with conda:

```python script
# install working environment with conda
conda env create -n berlin-tdd-workshop -f environment.yml

# environment should be activated now
# if not type: source activate berlin-tdd-workshop
```

With pyenv and poetry:

`make setup`
`source .venv/bin/activate` to activate the environment

## Running test

Start environment and:

`pytest` or `pytest -vv` for verbose output

or if you did the poetry setup:
`make test`

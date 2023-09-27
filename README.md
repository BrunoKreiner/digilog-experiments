# digilog_experiments

[![codecov](https://codecov.io/gh/BrunoKreiner/digilog-experiments/branch/main/graph/badge.svg?token=digilog-experiments_token_here)](https://codecov.io/gh/BrunoKreiner/digilog-experiments)
[![CI](https://github.com/BrunoKreiner/digilog-experiments/actions/workflows/main.yml/badge.svg)](https://github.com/BrunoKreiner/digilog-experiments/actions/workflows/main.yml)

Awesome digilog_experiments created by BrunoKreiner

## Install it from PyPI

```bash
pip install digilog_experiments
```

## Usage

cd digilog_experiments

#### python -m cli human-labeling-preprocess:

###### Arguments

1. `csv_path`: Path to the input CSV file. This path must exist.
2. `output_path`: Path where the preprocessed data will be saved.
3. `n`: Number of top examples to take after preprocessing.

###### Options

- `--seed`: Random seed for reproducibility. (Default: 42)
- `--include-luqa`: Include Luqa, Malta in the top n examples. (Default: True)
- `--shuffle`: Shuffle the data before taking the top n examples. (Default: True)

###### Example

```bash
$ human_labeling_preprocess ./path/to/input.csv ./path/to/output.csv 100 --seed 123 --include-luqa true --shuffle false
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

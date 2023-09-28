# digilog_experiments

[![codecov](https://codecov.io/gh/BrunoKreiner/digilog-experiments/branch/main/graph/badge.svg?token=digilog-experiments_token_here)](https://codecov.io/gh/BrunoKreiner/digilog-experiments)
[![CI](https://github.com/BrunoKreiner/digilog-experiments/actions/workflows/main.yml/badge.svg)](https://github.com/BrunoKreiner/digilog-experiments/actions/workflows/main.yml)

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

#### python -m cli label_data:

###### Arguments
1. `csv_file`: Path to the input CSV file with data to be labeled. This path must exist. (Default: ../data/HumanAnnotated.csv)

###### Example
```bash
$ label_data ./path/to/data/HumanAnnotated.csv
```

###### Workflow

1. The program fetches the first unlabeled row from the CSV.
2. Displays the website, municipality, and country information to the user.
3. Asks the user to enter a label, optional comments, and a confidence level.
4. The input data is saved back into the CSV.
5. The program then asks if the user wishes to continue labeling. If not, it terminates.

###### Prompts

1. Label: "Enter label (0 for incorrect, 1 for correct, 2 for website problem)"
2. Comment: "Enter any comments" (Optional)
3. Confidence: "Enter confidence level (0-100)"

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

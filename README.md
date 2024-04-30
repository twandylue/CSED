# Final Report

- Name: An Lu (Andy Lu)
- What programming language is being used: Python

## How to start

### Create a virtual environment and Activate it

#### Windows

```console
$ python -m venv env
...(snip)
$ .\env\Scripts\activate
...(snip)
```

#### MacOS and Linux

```console
$ python3 -m venv env
...(snip)
$ source env/bin/activate
...(snip)
```

### Install the required packages

```console
$ pip install -r requirements.txt
...(snip)
```

### Deactivate the virtual environment

```console
deactivate
```

## How to run the code

### Get some help

```console
$ python3 main.py -h
Usage: python main.py [SUBCOMMAND] [OPTIONS]
Subcommands and options:
     -t, --train <file>                    train the model using the <file> (.csv)
     -p, --predict <file>                  predict the class of the emails in the <file> (.txt)
     -h, --help                            display this help message
```

### Train the model

Example:

```console
$ python3 main.py -t ./data/spam.csv
Starting to train the model...
Model trained
Accuracy: 0.9835
Saving the model...
Model saved
```

### Predict the spam email by the model

Example:

```console
$ python3 main.py -p ./data/email.txt
Email content:
Sounds great! Are you home now?

Result: This email is not Spam.
Probability: 0.9993
```

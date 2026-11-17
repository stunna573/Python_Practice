# Python Practice Portfolio

A collection of practical Python exercises and small examples covering the fundamentals of the language. This repository has been organized from my learning exercises into readable, runnable modules.

## What this portfolio covers

- Variables, data types, operators, and input/output
- Conditional statements and loops
- Lists, tuples, dictionaries, and common collection operations
- String methods and formatting
- Functions, parameters, return values, and scope
- Modules and imports
- Reading and writing text files
- Exception handling and custom exceptions
- Regular expressions
- Small practical programs: a command-line calculator and sales calculations

## Repository structure

```text
Python-Practice-Portfolio/
├── README.md
├── .gitignore
├── requirements.txt
├── basics/
├── control_flow/
├── collections/
├── strings/
├── functions/
├── modules/
├── file_handling/
├── exceptions/
├── regular_expressions/
├── projects/
│   ├── calculator/
│   └── sales/
└── tests/
```

Each topic folder has its own README with a short overview and run instructions.

## Requirements

- Python 3.10 or newer
- No third-party packages are required; examples use the Python standard library.

Check your Python version:

```bash
python --version
```

## Run an example

From the repository root:

```bash
python basics/data_types.py
python control_flow/loops.py
python projects/calculator/calculator.py
python projects/sales/main.py
```

Some examples ask for input in the terminal.

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Notes

- The examples are intended for learning and practice, not as production applications.
- Some exercises have been rewritten for clarity and corrected where the original code contained obvious mistakes.
- Temporary files, editor metadata, Python cache files, and nested Git metadata from the source folder are not included.
- File-handling examples create their sample files in a `sample_data/` directory when run.

## Learning approach

The repository is organized by topic so that each concept can be explored independently. The small projects combine several fundamentals into complete, runnable examples.

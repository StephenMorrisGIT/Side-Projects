# Stock Valuation Toolkit

## Overview
A Python-based toolkit for evaluating stock fundamentals. The program offers customizable stock valuation methods and detailed company financial insights.

## Description
This toolkit streamlines the process of evaluating stocks using various financial metrics and valuation methods. It supports dynamic imports for different evaluation techniques, integrates with Yahoo Finance for live data, and provides tools for analyzing revenue growth, profit growth, and financial ratios. The program is designed for developers and finance enthusiasts who want to customize and expand their analysis workflows.

## Dependencies
Before installing and running the program, ensure the following prerequisites are met:
- **Python**: Version 3.8 or later.
- **Libraries**:
  - `yfinance`
  - `pandas`
  - `csv`
  - `python-docx`

- **OS**: Windows, macOS, or Linux.
- Additional requirement: A CSV file named `stockValuationMethods.csv` containing available valuation methods.

## Installing
1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```
3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure the `stockValuationMethods.csv` file exists in the root directory, formatted with valuation methods.

## Executing Program
1. Run the main entry point:
   ```bash
   python main.py
   ```
2. Follow these steps:
   - Enter a valid stock ticker (e.g., `AAPL` for Apple Inc.).
   - Select a valuation method from the presented list.
   - View the financial analysis and insights.

## Authors
- Stephen Morris - [\[Github\]](https://github.com/StephenMorrisGIT)

## Version History
- **v1.0**: Initial release. 01.09.2025

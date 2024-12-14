# Autolysis

**Autolysis** is a Python-based tool designed to simplify dataset analysis. It automates the process of generating visualizations and reports, making data analysis faster and more efficient.

## Features
- Load datasets from CSV files easily.
- Automatically generate summary statistics.
- Visualizations including heatmaps and pairplots.
- Export Markdown reports summarizing the dataset.

## installation
1. clone the repository:
   bash
   git clone https://github.com/Shrinidhi2307/autolysis.git

2. navigate to the directory:
    cd autolysis

3. install the required Python libraries:
    pip install -r requirements.txt

## usage
1. run the script
    python autolysis.py

2. Enter the path to your CSV file when prompted.

## outputs
1. visualizations directory, which contains heatmap.png, pairplot.png
2. markdown report saved in reports directory as dataset_report.markdown

## example
    $ python autolysis.py
    Enter the path to the CSV file: path/to/your/dataset.csv
    Dataset loaded successfully with X rows and Y columns.
    Heatmap saved as visualizations/heatmap.png
    Pairplot saved as visualizations/pairplot.png
    Markdown report saved to 'reports/dataset_report.md'.

## project is licensed under MIT License, as required
## thank you!



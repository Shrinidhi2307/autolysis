import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_dataset(file_path):
    """
    Analyze the dataset and generate visualizations.
    """
    try:
        # Load the dataset
        data = pd.read_csv(file_path)
        print(f"Dataset loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.\n")
        
        # Generate summary statistics
        summary = data.describe(include='all')
        print("Summary Statistics:")
        print(summary)
        
        # Save heatmap
        os.makedirs("visualizations", exist_ok=True)
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
        heatmap_path = "visualizations/heatmap.png"
        plt.savefig(heatmap_path)
        plt.close()
        print(f"Heatmap saved as {heatmap_path}")
        
        # Save pairplot
        pairplot_path = "visualizations/pairplot.png"
        sns.pairplot(data)
        plt.savefig(pairplot_path)
        plt.close()
        print(f"Pairplot saved as {pairplot_path}")
        
        # Generate Markdown report
        generate_markdown_report(data.describe().to_string())
    except Exception as e:
        print(f"Error analyzing dataset: {e}")

def generate_markdown_report(data_summary):
    """
    Save dataset summary locally as a Markdown-like text file.
    """
    try:
        os.makedirs("reports", exist_ok=True)
        report_path = "reports/dataset_report.md"
        with open(report_path, "w") as file:
            file.write("# Dataset Summary Report\n\n")
            file.write("## Summary Statistics\n\n")
            file.write(data_summary)
        print(f"Markdown report saved to '{report_path}'.")
    except Exception as e:
        print(f"Error generating Markdown report locally: {e}")

if __name__ == "__main__":
    # Get the CSV file path from the user
    file_path = input("Enter the path to the CSV file: ").strip()
    analyze_dataset(file_path)

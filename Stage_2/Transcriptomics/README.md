# Transcriptomics Analysis - Volcano Plot and Gene Expression Interpretation

## Overview
This Python script, `transcriptomics_script.py`, performs RNA-seq data analysis on a processed dataset containing gene expression information from a diseased cell line and a diseased cell line treated with compound X. The script includes the following functionalities:

- **Volcano Plot Generation:** Visualises the relationship between log2 fold change and p-value.
- **Identification of Upregulated and Downregulated Genes:** Filters genes based on log2 fold change and p-value thresholds.
- **Gene Function Interpretation:** Identifies functions of the top 5 upregulated and downregulated genes.

The dataset for this analysis can be accessed [here](https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt).

## Installation

Follow these steps to set up the environment and install necessary dependencies:

### Clone the Repository:
```bash
git clone https://github.com/SamuelEA25/HackBio-Coding-Internship.git
cd HackBio-Coding-Internship/Stage_2/Transcriptomics
```

### Create a Virtual Environment:
It is recommended to use a virtual environment to manage dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### Install Required Dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Script
After setting up the environment, the script can be executed as follows:
```bash
python transcriptomics_script.py
```

## Dependencies
This script requires the following Python libraries:
- `numpy`: Supports efficient numerical computations and array operations
- `pandas`: Creates and manipulates structured data (DataFrames, Series)
- `matplotlib`: Creates static, animated, and interactive plots
- `seaborn`: Simplifies and beautifies statistical visualisations
- `scipy`: Performs advanced mathematical, scientific, and engineering computations
- `requests`: Sends HTTP requests for web API interactions

For manual installation of the dependencies, execute:
```bash
pip install numpy pandas matplotlib seaborn scipy requests
```

## Process of Result Generation
The script performs the following key tasks:

### **1. Data Loading & Preprocessing**
The dataset is loaded from the provided URL and processed to extract relevant gene expression information:
```python
url = "https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt"
transcriptomics_data = pd.read_csv(url, sep=r'\s+', engine='python')
```
Each gene's **p-value** is transformed to `-log10(p-value)` for better visualisation:
```python
transcriptomics_data['neg_log10_pvalue'] = -np.log10(transcriptomics_data['pvalue'])
```

### **2. Volcano Plot Generation**
A volcano plot is generated using **log2 fold change** and **p-value** to highlight significantly upregulated and downregulated genes.
```python
sns.scatterplot(data=transcriptomics_data, x='log2FoldChange', y='neg_log10_pvalue', hue='category', palette=category_colors, edgecolor=None, alpha=0.7)
```
The categories are:
- **Upregulated Genes:** Log2 fold change > 1 and p-value < 0.01
- **Downregulated Genes:** Log2 fold change < -1 and p-value < 0.01
- **Not Significant:** Other genes with Log2 fold change and p-value outside the threshold for upregulated and downregulated genes

[View Volcano Plot Here](https://github.com/SamuelEA25/HackBio-Coding-Internship/blob/main/Stage_2/Transcriptomics/Output/transcriptomics_volcano_plot.png)

### **3. Upregulated and Downregulated Gene Identification**
Genes meeting the upregulated or downregulated criteria are filtered:
```python
top_upregulated_genes = transcriptomics_data[(transcriptomics_data['log2FoldChange'] > 1) & (transcriptomics_data['pvalue'] < 0.01)].nlargest(5, 'log2FoldChange')
top_downregulated_genes = transcriptomics_data[(transcriptomics_data['log2FoldChange'] < -1) & (transcriptomics_data['pvalue'] < 0.01)].nsmallest(5, 'log2FoldChange')
```
[View Top 5 Upregulated Genes Here](https://github.com/SamuelEA25/HackBio-Coding-Internship/blob/main/Stage_2/Transcriptomics/Output/top_upregulated_genes.csv)

[View Top 5 Downregulated Genes Here](https://github.com/SamuelEA25/HackBio-Coding-Internship/blob/main/Stage_2/Transcriptomics/Output/top_downregulated_genes.csv)

### **4. Gene Function Retrieval**
For the **top 5 upregulated and downregulated genes**, functional descriptions are retrieved from the Ensembl database:
```python
def get_gene_function_ensembl(gene_name):
    url = f"https://rest.ensembl.org/lookup/symbol/human/{gene_name}?content-type=application/json"
    response = requests.get(url)
    if response.status_code == 200:
        gene_info = response.json()
        return gene_info.get('description', "No functional information available")
    return "Failed to retrieve data"
```
[View Gene Functions for Top 5 Upregulated and Downregulated Genes Here](https://github.com/SamuelEA25/HackBio-Coding-Internship/blob/main/Stage_2/Transcriptomics/Output/merged_gene_functions.csv)

### **5. Saving Results**
The script does not automatically save results as CSV files. You can manually save the filtered genes by running the following commands in a Python environment:
```python
# Save upregulated genes
import pandas as pd
upregulated_genes.to_csv('upregulated_genes.csv', index=False)

# Save downregulated genes
downregulated_genes.to_csv('downregulated_genes.csv', index=False)
```

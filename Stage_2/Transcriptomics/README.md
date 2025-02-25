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

### **3. Upregulated and Downregulated Gene Identification**
Genes meeting the upregulated or downregulated criteria are filtered:
```python
top_upregulated_genes = transcriptomics_data[(transcriptomics_data['log2FoldChange'] > 1) & (transcriptomics_data['pvalue'] < 0.01)].nlargest(5, 'log2FoldChange')
top_downregulated_genes = transcriptomics_data[(transcriptomics_data['log2FoldChange'] < -1) & (transcriptomics_data['pvalue'] < 0.01)].nsmallest(5, 'log2FoldChange')
```

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

### **5. Saving Results**
The script does not automatically save results as CSV files. You can manually save the filtered genes by running the following commands in a Python environment:
```python
# Save upregulated genes
import pandas as pd
upregulated_genes.to_csv('upregulated_genes.csv', index=False)

# Save downregulated genes
downregulated_genes.to_csv('downregulated_genes.csv', index=False)
```
## Results Interpretation

The transcriptomic analysis performed in this study provides insights into the differential gene expression patterns between a diseased cell line and the same cell line treated with compound X. The key findings from the analysis are outlined below:

### 1. Volcano Plot Interpretation
The volcano plot serves as a visual representation of differentially expressed genes, where:

- **Upregulated Genes (Red Dots):** Genes with a log2 fold change > 1 and p-value < 0.01 indicate significant upregulation in response to compound X. These genes may be involved in pathways activated by the treatment, suggesting a potential therapeutic mechanism.
- **Downregulated Genes (Blue Dots):** Genes with a log2 fold change < -1 and p-value < 0.01 represent significant downregulation, implying that these genes are suppressed under treatment conditions. This suppression could indicate pathways that compound X inhibits, either directly or indirectly.
- **Non-significant Genes (Gray Dots):** Genes that do not meet the statistical threshold for significance, suggesting that their expression remains unchanged between treated and untreated conditions.

[View Volcano Plot Here](https://github.com/SamuelEA25/HackBio-Coding-Internship/blob/main/Stage_2/Transcriptomics/Output/transcriptomics_volcano_plot.png)

### 2. Identification of Differentially Expressed Genes
- The top **upregulated genes** are likely involved in cellular responses triggered by compound X, including stress response, metabolic reprogramming, or activation of signaling cascades relevant to disease mitigation.
- The top **downregulated genes** may be associated with disease-promoting processes that are repressed upon treatment, potentially revealing molecular targets modulated by compound X.

[View Top 5 Upregulated Genes Here](https://github.com/SamuelEA25/HackBio-Coding-Internship/blob/main/Stage_2/Transcriptomics/Output/top_upregulated_genes.csv)

[View Top 5 Downregulated Genes Here](https://github.com/SamuelEA25/HackBio-Coding-Internship/blob/main/Stage_2/Transcriptomics/Output/top_downregulated_genes.csv)

### 3. Functional Significance of Differentially Expressed Genes

#### **Top 5 Upregulated Genes and Their Functions:**
1. **DTHD1 (Death Domain Containing 1)** – Implicated in apoptotic signaling pathways, suggesting that compound X may influence cell survival mechanisms.
2. **EMILIN2 (Elastin Microfibril Interfacer 2)** – Plays a role in extracellular matrix organization and cell adhesion, potentially indicating an impact on tissue remodeling.
3. **PI16 (Peptidase Inhibitor 16)** – Involved in immune response regulation and inhibition of proteolytic activity, which may suggest a role in modulating inflammatory responses.
4. **C4orf45 (Chromosome 4 Open Reading Frame 45)** – A poorly characterized gene, but its upregulation may indicate involvement in an unrecognized regulatory process affected by the treatment.
5. **FAM180B (Family With Sequence Similarity 180 Member B)** – Its function remains largely unknown, though its expression changes could suggest relevance in disease-associated pathways.

#### **Top 5 Downregulated Genes and Their Functions:**
1. **TBX5 (T-Box Transcription Factor 5)** – A key regulator of cardiac and limb development, suggesting that compound X might modulate developmental or repair-associated pathways.
2. **IFITM1 (Interferon Induced Transmembrane Protein 1)** – Plays a role in innate immunity, particularly antiviral responses, implying that compound X may suppress immune activation.
3. **TNN (Tenascin N)** – An extracellular matrix glycoprotein involved in tissue remodeling and neuronal development, which may indicate reduced fibrosis or structural reorganization under treatment.
4. **COL13A1 (Collagen Type XIII Alpha 1 Chain)** – A structural component of the extracellular matrix, its downregulation could be associated with changes in cell adhesion or tissue integrity.
5. **IFITM3 (Interferon Induced Transmembrane Protein 3)** – Similar to IFITM1, it is involved in immune defense, and its suppression may indicate modulation of inflammatory signaling.

#### **Biological Insights from Gene Expression Changes:**
Functional annotations retrieved from the Ensembl database ([View Gene Functions for Top 5 Upregulated and Downregulated Genes Here](https://github.com/SamuelEA25/HackBio-Coding-Internship/blob/main/Stage_2/Transcriptomics/Output/merged_gene_functions.csv)) provide insights into the biological roles of the top differentially expressed genes:

- **Upregulated genes** suggest a response to **cellular stress, extracellular matrix remodeling, and immune modulation**, which could be linked to the therapeutic action of compound X.
- **Downregulated genes** predominantly include **immune-related and extracellular matrix components**, suggesting that compound X may suppress inflammation and tissue remodeling processes commonly associated with disease progression.

These functional insights are valuable for understanding the mechanism of action of compound X, identifying potential therapeutic targets, and guiding further experimental validation.

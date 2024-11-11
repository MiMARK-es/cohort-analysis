# Detailed Data for P02654


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: P02654
- **Gene Name**: APOC1
- **Protein Name**: apolipoprotein C1
- **Swiss Prot**: APOC1_HUMAN
- **Family**: transporter
- **Biomarker Application**: prognosis,unspecified application
- **Number of Isoforms**: 0
- **Regulation**: 2
- **(transcriptomics) AUC**: 0.98
- **(transcriptomics) Fold Change**: 1.86
- **(transcriptomics) Regulation**: Upregulated
- **Discotope Epitope Count**: 3
- **Max n_uniprots (Homo)**: 2
- **Max n_uniprots (Hetero)**: N/A


## Expression Comparison

![Expression Comparison](./P02654_expression_comparison.png)

## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| APOC1             | APOC3             |   0.999 |
| APOC1             | APOE              |   0.999 |
| APOC1             | APOC2             |   0.999 |
| APOC1             | APOA1             |   0.998 |
| APOC1             | APOB              |   0.996 |
| APOC1             | APOA2             |   0.991 |
| APOC1             | APOC4             |   0.99  |
| APOC1             | CETP              |   0.985 |
| APOC1             | LCAT              |   0.973 |
| APOC1             | APOA4             |   0.969 |
| APOC1             | CLU               |   0.969 |
| APOC1             | APOA5             |   0.947 |
| APOC1             | APOM              |   0.939 |
| APOC1             | APOH              |   0.931 |
| APOC1             | PON1              |   0.93  |
| APOC1             | APOL1             |   0.918 |

## Homologs

| uniprot_id   | gene_id   |
|--------------|-----------|

## Biological Assemblies

|   Unnamed: 0 |   assembly |   n_uniprots | composition   | crystal_id   |
|-------------:|-----------:|-------------:|:--------------|:-------------|
|            0 |          1 |            1 | Homo          | 1alf         |
|            0 |          1 |            2 | Homo          | 6dz6         |
|            0 |          1 |            2 | Homo          | 6dvu         |
|            0 |          1 |            2 | Homo          | 6dxr         |
|            0 |          1 |            1 | Homo          | 1ioj         |
|            0 |          1 |            2 | Homo          | 6nf3         |
|            0 |          1 |            1 | Homo          | 1ale         |
|            0 |          1 |            1 | Homo          | 1opp         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification   |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:---------------|
|     1 | M    |         0.25011 | False     |                          1.09649 |                 56.56 |         0     | N/A            |
|     2 | R    |         0.37953 | False     |                          0.86771 |                 60.03 |         0     | N/A            |
|     3 | L    |         0.4002  | False     |                          0.92051 |                 61.16 |         0.001 | N/A            |
|     4 | F    |         0.40198 | False     |                          0.86163 |                 63.87 |         0.001 | N/A            |
|     5 | L    |         0.2924  | False     |                          0.79269 |                 65.19 |         0.001 | N/A            |
|     6 | S    |         0.27086 | False     |                          0.45777 |                 69.42 |         0.001 | N/A            |
|     7 | L    |         0.37885 | False     |                          0.75064 |                 71.15 |         0.001 | N/A            |
|     8 | P    |         0.304   | False     |                          0.4881  |                 72.11 |         1.106 | N/A            |
|     9 | V    |         0.16897 | False     |                          0.67298 |                 75.67 |        90.936 | N/A            |
|    10 | L    |         0.2935  | False     |                          0.66019 |                 73.35 |        98.519 | N/A            |
|    11 | V    |         0.23688 | False     |                          0.60418 |                 74.85 |        99.87  | N/A            |
|    12 | V    |         0.10882 | False     |                          0.60361 |                 73.04 |        99.984 | N/A            |
|    13 | V    |         0.20147 | False     |                          0.53221 |                 73.68 |        99.993 | N/A            |
|    14 | L    |         0.25224 | False     |                          0.58846 |                 68.81 |        99.58  | N/A            |
|    15 | S    |         0.10869 | False     |                          0.40185 |                 63.95 |        97.126 | N/A            |
|    16 | I    |         0.13456 | False     |                          0.67618 |                 63.56 |        96.817 | N/A            |
|    17 | V    |         0.29378 | False     |                          0.78112 |                 63.31 |        93.426 | N/A            |
|    18 | L    |         0.35439 | False     |                          0.88666 |                 57.59 |        78.989 | N/A            |
|    19 | E    |         0.31192 | False     |                          0.70718 |                 51.74 |         0     | N/A            |
|    20 | G    |         0.26857 | False     |                          0.24718 |                 50.64 |         0     | N/A            |
|    21 | P    |         0.3539  | False     |                          0.7182  |                 50.81 |         0     | N/A            |
|    22 | A    |         0.32046 | False     |                          0.79705 |                 42.16 |         0     | N/A            |
|    23 | P    |         0.40528 | False     |                          0.90186 |                 44.69 |         0     | N/A            |
|    24 | A    |         0.35543 | False     |                          0.90704 |                 48.12 |         0     | N/A            |
|    25 | Q    |         0.63793 | True      |                          0.90178 |                 43.17 |         0     | N/A            |
|    26 | G    |         0.50353 | True      |                          0.79726 |                 42.66 |         0     | N/A            |
|    27 | T    |         0.44415 | False     |                          0.95002 |                 41.83 |         0     | N/A            |
|    28 | P    |         0.3951  | False     |                          0.89817 |                 47.07 |         0     | N/A            |
|    29 | D    |         0.43424 | False     |                          0.50125 |                 52.53 |         0     | N/A            |
|    30 | V    |         0.37084 | False     |                          0.73993 |                 55.2  |         0     | N/A            |
|    31 | S    |         0.33263 | False     |                          0.63917 |                 57.39 |         0     | N/A            |
|    32 | S    |         0.26164 | False     |                          0.4     |                 61.28 |         0     | N/A            |
|    33 | A    |         0.24355 | False     |                          0.26486 |                 61.72 |         0     | N/A            |
|    34 | L    |         0.24734 | False     |                          0.68291 |                 65.04 |         0     | N/A            |
|    35 | D    |         0.30823 | False     |                          0.48279 |                 72.2  |         0     | N/A            |
|    36 | K    |         0.21817 | False     |                          0.71504 |                 73.25 |         0     | N/A            |
|    37 | L    |         0.21444 | False     |                          0.62407 |                 72.25 |         0     | N/A            |
|    38 | K    |         0.23061 | False     |                          0.66251 |                 76.22 |         0     | N/A            |
|    39 | E    |         0.37425 | False     |                          0.59706 |                 79.02 |         0     | N/A            |
|    40 | F    |         0.26797 | False     |                          0.67756 |                 76.79 |         0     | N/A            |
|    41 | G    |         0.18326 | False     |                          0.38862 |                 79.35 |         0     | N/A            |
|    42 | N    |         0.27292 | False     |                          0.54836 |                 81.87 |         0     | N/A            |
|    43 | T    |         0.27046 | False     |                          0.52799 |                 84.95 |         0     | N/A            |
|    44 | L    |         0.19941 | False     |                          0.6377  |                 78.48 |         0     | N/A            |
|    45 | E    |         0.18608 | False     |                          0.44048 |                 81.22 |         0     | N/A            |
|    46 | D    |         0.23706 | False     |                          0.60726 |                 85.51 |         0     | N/A            |
|    47 | K    |         0.31919 | False     |                          0.66069 |                 83.11 |         0     | N/A            |
|    48 | A    |         0.1181  | False     |                          0.35986 |                 80.56 |         0     | N/A            |
|    49 | R    |         0.22026 | False     |                          0.6129  |                 80.7  |         0     | N/A            |
|    50 | E    |         0.32138 | False     |                          0.59203 |                 83.22 |         0     | N/A            |
|    51 | L    |         0.23628 | False     |                          0.62969 |                 78.09 |         0     | N/A            |
|    52 | I    |         0.23247 | False     |                          0.61357 |                 78.7  |         0     | N/A            |
|    53 | S    |         0.26114 | False     |                          0.49225 |                 76.61 |         0     | N/A            |
|    54 | R    |         0.41359 | False     |                          0.67799 |                 71.88 |         0     | N/A            |
|    55 | I    |         0.2477  | False     |                          0.17999 |                 68.56 |         0     | N/A            |
|    56 | K    |         0.34225 | False     |                          0.80359 |                 65.65 |         0     | N/A            |
|    57 | Q    |         0.51364 | True      |                          0.85867 |                 64.21 |         0     | N/A            |
|    58 | S    |         0.28294 | False     |                          0.31427 |                 59.18 |         0     | N/A            |
|    59 | E    |         0.31439 | False     |                          0.81545 |                 62.02 |         0     | N/A            |
|    60 | L    |         0.27962 | False     |                          0.56352 |                 65.95 |         0     | N/A            |
|    61 | S    |         0.22008 | False     |                          0.31208 |                 66.76 |         0     | N/A            |
|    62 | A    |         0.25786 | False     |                          0.64535 |                 70.58 |         0     | N/A            |
|    63 | K    |         0.35291 | False     |                          0.72819 |                 74.83 |         0     | N/A            |
|    64 | M    |         0.18167 | False     |                          0.45095 |                 78.16 |         0     | N/A            |
|    65 | R    |         0.22878 | False     |                          0.75919 |                 76.47 |         0     | N/A            |
|    66 | E    |         0.35454 | False     |                          0.61215 |                 84.41 |         0     | N/A            |
|    67 | W    |         0.30138 | False     |                          0.70011 |                 87.25 |         0     | N/A            |
|    68 | F    |         0.16792 | False     |                          0.66275 |                 86.83 |         0     | N/A            |
|    69 | S    |         0.20225 | False     |                          0.44005 |                 86.79 |         0     | N/A            |
|    70 | E    |         0.26234 | False     |                          0.48099 |                 87.92 |         0     | N/A            |
|    71 | T    |         0.13719 | False     |                          0.37638 |                 88.51 |         0     | N/A            |
|    72 | F    |         0.1833  | False     |                          0.57797 |                 84.43 |         0     | N/A            |
|    73 | Q    |         0.31474 | False     |                          0.4344  |                 87.22 |         0     | N/A            |
|    74 | K    |         0.23408 | False     |                          0.62026 |                 87.62 |         0     | N/A            |
|    75 | V    |         0.16495 | False     |                          0.53493 |                 84.02 |         0     | N/A            |
|    76 | K    |         0.23116 | False     |                          0.43868 |                 82.66 |         0     | N/A            |
|    77 | E    |         0.33931 | False     |                          0.51237 |                 84.96 |         0     | N/A            |
|    78 | K    |         0.27289 | False     |                          0.68037 |                 82.18 |         0     | N/A            |
|    79 | L    |         0.3089  | False     |                          0.77626 |                 76.6  |         0     | N/A            |
|    80 | K    |         0.32079 | False     |                          0.70458 |                 71.66 |         0     | N/A            |
|    81 | I    |         0.34398 | False     |                          0.86042 |                 62.71 |         0     | N/A            |
|    82 | D    |         0.2796  | False     |                          0.79263 |                 56.35 |         0     | N/A            |
|    83 | S    |         0.17584 | False     |                          0.99288 |                 48.92 |         0     | N/A            |


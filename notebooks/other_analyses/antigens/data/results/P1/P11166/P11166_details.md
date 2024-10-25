# Detailed Data for P11166


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: P11166
- **Gene Name**: Glut1
- **Protein Name**: Solute carrier family 2, facilitated glucose transporter member 1, Glucose transporter type 1 /// 
- **Swiss Prot**: GTR1_HUMAN
- **Family**: transporter
- **Biomarker Application**: diagnosis,efficacy,prognosis
- **Number of Isoforms**: 0
- **Regulation**: 1
- **(transcriptomics) AUC**: nan
- **(transcriptomics) Fold Change**: nan
- **(transcriptomics) Regulation**: Downregulated
- **Discotope Epitope Count**: 106
- **Max n_uniprots (Homo)**: 1
- **Max n_uniprots (Hetero)**: N/A


## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| SLC2A1            | TP53              |   0.967 |
| SLC2A1            | SLC2A4            |   0.909 |
| SLC2A1            | SLC2A2            |   0.906 |
| SLC2A1            | HIF1A             |   0.902 |

## Homologs

| uniprot_id   | gene_id   |
|:-------------|:----------|
| K7EIT1       | SLC2A5    |
| F5GYX0       | SLC2A3    |
| F5H5Q3       | SLC2A14   |
| Q9NRM0       | SLC2A9    |
| F2Z2F6       | SLC2A6    |
| C9J0E8       | SLC2A2    |
| Q5VVV3       | SLC2A8    |
| Q6PXP3       | SLC2A7    |
| Q8TD20       | SLC2A12   |
| I3L2R4       | SLC2A4    |
| O95528       | SLC2A10   |
| Q96QE2       | SLC2A13   |
| F8WCV3       | SLC2A11   |

## Biological Assemblies

|   Unnamed: 0 |   assembly |   n_uniprots | composition   | crystal_id   |
|-------------:|-----------:|-------------:|:--------------|:-------------|
|            0 |          1 |            1 | Homo          | 4pyp         |
|            0 |          1 |            1 | Homo          | 5eqg         |
|            0 |          1 |            1 | Homo          | 5eqh         |
|            0 |          1 |            1 | Homo          | 5eqi         |
|            0 |          1 |            1 | Homo          | 6tha         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification                | glycosylation                   |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:----------------------------|:--------------------------------|
|     1 | M    |         0.13286 | False     |                          1.28057 |                 36.61 |         0     | N-acetylmethionine          | N/A                             |
|     2 | E    |         0.25987 | True      |                          0.81009 |                 40.62 |         0     | N/A                         | N/A                             |
|     3 | P    |         0.22491 | True      |                          0.76522 |                 45.98 |         0     | N/A                         | N/A                             |
|     4 | S    |         0.16185 | True      |                          0.38193 |                 52.03 |         0     | N/A                         | N/A                             |
|     5 | S    |         0.14109 | False     |                          0.28772 |                 57.6  |         0     | N/A                         | N/A                             |
|     6 | K    |         0.2126  | True      |                          0.72064 |                 63.71 |         0     | N/A                         | N/A                             |
|     7 | K    |         0.18873 | True      |                          0.63365 |                 76.41 |         0     | N/A                         | N/A                             |
|     8 | L    |         0.16177 | True      |                          0.64111 |                 87.55 |         0     | N/A                         | N/A                             |
|     9 | T    |         0.09344 | False     |                          0.15253 |                 92.95 |         0     | N/A                         | N/A                             |
|    10 | G    |         0.10976 | False     |                          0.74854 |                 92.74 |         0     | N/A                         | N/A                             |
|    11 | R    |         0.11183 | False     |                          0.51095 |                 93.66 |         0     | N/A                         | N/A                             |
|    12 | L    |         0.00876 | False     |                          0.0033  |                 95.8  |        10.799 | N/A                         | N/A                             |
|    13 | M    |         0.04309 | False     |                          0.46749 |                 96.2  |        11.315 | N/A                         | N/A                             |
|    14 | L    |         0.0236  | False     |                          0.48285 |                 96.46 |        12.893 | N/A                         | N/A                             |
|    15 | A    |         0.00224 | False     |                          0       |                 97.15 |        13.12  | N/A                         | N/A                             |
|    16 | V    |         0.0015  | False     |                          0.00095 |                 97.24 |        13.39  | N/A                         | N/A                             |
|    17 | G    |         0.01353 | False     |                          0.44103 |                 96.69 |         6.933 | N/A                         | N/A                             |
|    18 | G    |         0.01035 | False     |                          0.02695 |                 97.2  |         6.353 | N/A                         | N/A                             |
|    19 | A    |         0.001   | False     |                          0       |                 97.88 |         6.537 | N/A                         | N/A                             |
|    20 | V    |         0.01384 | False     |                          0.14091 |                 97.72 |         6.755 | N/A                         | N/A                             |
|    21 | L    |         0.00767 | False     |                          0.21975 |                 97.56 |         6.012 | N/A                         | N/A                             |
|    22 | G    |         0.00092 | False     |                          0       |                 97.53 |         0.94  | N/A                         | N/A                             |
|    23 | S    |         0.00353 | False     |                          0       |                 97.8  |         0.575 | N/A                         | N/A                             |
|    24 | L    |         0.0142  | False     |                          0.20114 |                 97.94 |         0.575 | N/A                         | N/A                             |
|    25 | Q    |         0.00151 | False     |                          0       |                 97.56 |         0     | N/A                         | N/A                             |
|    26 | F    |         0.01499 | False     |                          0.07835 |                 96.73 |         0     | N/A                         | N/A                             |
|    27 | G    |         0.00606 | False     |                          0       |                 94.88 |         0     | N/A                         | N/A                             |
|    28 | Y    |         0.00715 | False     |                          0.01744 |                 96.36 |         0     | N/A                         | N/A                             |
|    29 | N    |         0.00151 | False     |                          0.00064 |                 95.29 |         0     | N/A                         | N/A                             |
|    30 | T    |         0.04444 | False     |                          0.37661 |                 90.68 |         0     | N/A                         | N/A                             |
|    31 | G    |         0.01242 | False     |                          0.12855 |                 85.96 |         0     | N/A                         | N/A                             |
|    32 | V    |         0.00601 | False     |                          0.00095 |                 91.17 |         0     | N/A                         | N/A                             |
|    33 | I    |         0.01574 | False     |                          0.016   |                 87.7  |         0     | N/A                         | N/A                             |
|    34 | N    |         0.13512 | False     |                          0.50983 |                 81.33 |         0     | N/A                         | N/A                             |
|    35 | A    |         0.08656 | False     |                          0.52922 |                 81.9  |         0     | N/A                         | N/A                             |
|    36 | P    |         0.0221  | False     |                          0.00795 |                 89.58 |         0     | N/A                         | N/A                             |
|    37 | Q    |         0.06091 | False     |                          0.32611 |                 89.61 |         0     | N/A                         | N/A                             |
|    38 | K    |         0.23534 | True      |                          0.84887 |                 90.48 |         0     | N/A                         | N/A                             |
|    39 | V    |         0.09208 | False     |                          0.1845  |                 93.72 |         0     | N/A                         | N/A                             |
|    40 | I    |         0.00464 | False     |                          0       |                 95.09 |         0     | N/A                         | N/A                             |
|    41 | E    |         0.09849 | False     |                          0.1966  |                 95.28 |         0     | N/A                         | N/A                             |
|    42 | E    |         0.14748 | False     |                          0.34795 |                 95.57 |         0     | N/A                         | N/A                             |
|    43 | F    |         0.116   | False     |                          0.06141 |                 96.66 |         0.24  | N/A                         | N/A                             |
|    44 | Y    |         0.01012 | False     |                          0       |                 97    |         0.24  | N/A                         | N/A                             |
|    45 | N    |         0.18637 | True      |                          0.22066 |                 96.81 |         0.24  | N/A                         | N-linked (GlcNAc...) asparagine |
|    46 | Q    |         0.26869 | True      |                          0.4961  |                 96.01 |         0.24  | N/A                         | N/A                             |
|    47 | T    |         0.06549 | False     |                          0.02537 |                 96.25 |         0.24  | N/A                         | N/A                             |
|    48 | W    |         0.13378 | False     |                          0.2293  |                 96.92 |         0.24  | N/A                         | N/A                             |
|    49 | V    |         0.24594 | True      |                          0.42802 |                 96.87 |         0.24  | N/A                         | N/A                             |
|    50 | H    |         0.35045 | True      |                          0.62034 |                 94.63 |         0     | N/A                         | N/A                             |
|    51 | R    |         0.21192 | True      |                          0.38889 |                 95.44 |         0     | N/A                         | N/A                             |
|    52 | Y    |         0.37001 | True      |                          0.58012 |                 95.66 |         0     | N/A                         | N/A                             |
|    53 | G    |         0.39849 | True      |                          0.82234 |                 94.76 |         0     | N/A                         | N/A                             |
|    54 | E    |         0.42539 | True      |                          0.56787 |                 95.41 |         0     | N/A                         | N/A                             |
|    55 | S    |         0.25738 | True      |                          0.58083 |                 95.66 |         0     | N/A                         | N/A                             |
|    56 | I    |         0.21742 | True      |                          0.07252 |                 95.9  |         0     | N/A                         | N/A                             |
|    57 | L    |         0.30982 | True      |                          0.74948 |                 95.57 |         0     | N/A                         | N/A                             |
|    58 | P    |         0.21184 | True      |                          0.75123 |                 93.09 |         0.109 | N/A                         | N/A                             |
|    59 | T    |         0.24793 | True      |                          0.72623 |                 92.12 |         9.419 | N/A                         | N/A                             |
|    60 | T    |         0.1703  | True      |                          0.29344 |                 93.71 |        25.154 | N/A                         | N/A                             |
|    61 | L    |         0.10789 | False     |                          0.21103 |                 94.01 |        52.935 | N/A                         | N/A                             |
|    62 | T    |         0.14504 | False     |                          0.59611 |                 90.21 |        58.026 | N/A                         | N/A                             |
|    63 | T    |         0.08485 | False     |                          0.62344 |                 90.25 |        66.588 | N/A                         | N/A                             |
|    64 | L    |         0.0717  | False     |                          0.1558  |                 93.65 |        81.045 | N/A                         | N/A                             |
|    65 | W    |         0.06093 | False     |                          0.09263 |                 90.63 |        83.67  | N/A                         | N/A                             |
|    66 | S    |         0.04281 | False     |                          0.33755 |                 88.89 |        84.131 | N/A                         | N/A                             |
|    67 | L    |         0.04843 | False     |                          0.47472 |                 91.32 |        89.307 | N/A                         | N/A                             |
|    68 | S    |         0.00526 | False     |                          0       |                 92.27 |        90.095 | N/A                         | N/A                             |
|    69 | V    |         0.0524  | False     |                          0.33244 |                 90.01 |        95.506 | N/A                         | N/A                             |
|    70 | A    |         0.02272 | False     |                          0.14285 |                 90.56 |        95.839 | N/A                         | N/A                             |
|    71 | I    |         0.02655 | False     |                          0.18297 |                 94.89 |        95.953 | N/A                         | N/A                             |
|    72 | F    |         0.02273 | False     |                          0.05287 |                 95.43 |        93.513 | N/A                         | N/A                             |
|    73 | S    |         0.02101 | False     |                          0.05456 |                 94.56 |        62.992 | N/A                         | N/A                             |
|    74 | V    |         0.01394 | False     |                          0.31323 |                 96.33 |        58.904 | N/A                         | N/A                             |
|    75 | G    |         0.00544 | False     |                          0       |                 98.17 |        10.344 | N/A                         | N/A                             |
|    76 | G    |         0.00465 | False     |                          0       |                 97.76 |         5.965 | N/A                         | N/A                             |
|    77 | M    |         0.02544 | False     |                          0.13598 |                 97.41 |         6.589 | N/A                         | N/A                             |
|    78 | I    |         0.02788 | False     |                          0.51274 |                 97.85 |         7.413 | N/A                         | N/A                             |
|    79 | G    |         0.00284 | False     |                          0       |                 97.67 |         3.88  | N/A                         | N/A                             |
|    80 | S    |         0.00632 | False     |                          0.01144 |                 96.19 |         4.982 | N/A                         | N/A                             |
|    81 | F    |         0.02581 | False     |                          0.53404 |                 93.52 |        21.012 | N/A                         | N/A                             |
|    82 | S    |         0.02109 | False     |                          0.18849 |                 94.98 |        22.083 | N/A                         | N/A                             |
|    83 | V    |         0.00222 | False     |                          0.00095 |                 94.98 |        30.835 | N/A                         | N/A                             |
|    84 | G    |         0.04463 | False     |                          0.20475 |                 91.14 |        30.619 | N/A                         | N/A                             |
|    85 | L    |         0.09699 | False     |                          0.79851 |                 91.84 |        30.608 | N/A                         | N/A                             |
|    86 | F    |         0.04956 | False     |                          0.22676 |                 94.58 |        30.332 | N/A                         | N/A                             |
|    87 | V    |         0.00529 | False     |                          0       |                 93.4  |        26.04  | N/A                         | N/A                             |
|    88 | N    |         0.12036 | False     |                          0.4813  |                 89.47 |         0.924 | N/A                         | N/A                             |
|    89 | R    |         0.16983 | True      |                          0.68319 |                 90.14 |         0     | N/A                         | N/A                             |
|    90 | F    |         0.07192 | False     |                          0.30696 |                 94.41 |         0     | N/A                         | N/A                             |
|    91 | G    |         0.00553 | False     |                          0       |                 94.89 |         0     | N/A                         | N/A                             |
|    92 | R    |         0.00825 | False     |                          0.00328 |                 95.95 |         0     | N/A                         | N/A                             |
|    93 | R    |         0.04604 | False     |                          0.2236  |                 97.3  |         0     | N/A                         | N/A                             |
|    94 | N    |         0.08845 | False     |                          0.28804 |                 97.17 |         0.007 | N/A                         | N/A                             |
|    95 | S    |         0.00355 | False     |                          0       |                 97.89 |         0.708 | N/A                         | N/A                             |
|    96 | M    |         0.00548 | False     |                          0.02301 |                 98.2  |        16.463 | N/A                         | N/A                             |
|    97 | L    |         0.02714 | False     |                          0.34777 |                 97.64 |        30.274 | N/A                         | N/A                             |
|    98 | M    |         0.01991 | False     |                          0.41783 |                 97.25 |        32.801 | N/A                         | N/A                             |
|    99 | M    |         0.01945 | False     |                          0.10476 |                 97.13 |        35.017 | N/A                         | N/A                             |
|   100 | N    |         0.00533 | False     |                          0.00258 |                 97.95 |        36.959 | N/A                         | N/A                             |
|   101 | L    |         0.01916 | False     |                          0.70756 |                 97.91 |        86.609 | N/A                         | N/A                             |
|   102 | L    |         0.01837 | False     |                          0.26544 |                 98.44 |        95.27  | N/A                         | N/A                             |
|   103 | A    |         0.0009  | False     |                          0       |                 98.21 |        96.835 | N/A                         | N/A                             |
|   104 | F    |         0.01157 | False     |                          0.21779 |                 98.52 |        98.681 | N/A                         | N/A                             |
|   105 | V    |         0.01237 | False     |                          0.42291 |                 98.5  |        98.674 | N/A                         | N/A                             |
|   106 | S    |         0.00168 | False     |                          0       |                 98.51 |        94.577 | N/A                         | N/A                             |
|   107 | A    |         0.00713 | False     |                          0.02385 |                 98.3  |        94.037 | N/A                         | N/A                             |
|   108 | V    |         0.03113 | False     |                          0.52636 |                 98.27 |        93.576 | N/A                         | N/A                             |
|   109 | L    |         0.01652 | False     |                          0.19043 |                 98.3  |        87.766 | N/A                         | N/A                             |
|   110 | M    |         0.00337 | False     |                          0       |                 97.72 |        55.992 | N/A                         | N/A                             |
|   111 | G    |         0.03382 | False     |                          0.24179 |                 97.1  |        19.738 | N/A                         | N/A                             |
|   112 | F    |         0.05416 | False     |                          0.55572 |                 97.59 |        16.473 | N/A                         | N/A                             |
|   113 | S    |         0.00413 | False     |                          0       |                 97.22 |         1.806 | N/A                         | N/A                             |
|   114 | K    |         0.13404 | False     |                          0.37158 |                 95.88 |         0     | N/A                         | N/A                             |
|   115 | L    |         0.23721 | True      |                          0.86538 |                 94.58 |         0     | N/A                         | N/A                             |
|   116 | G    |         0.11513 | False     |                          0.54573 |                 94.81 |         0     | N/A                         | N/A                             |
|   117 | K    |         0.20362 | True      |                          0.48775 |                 95.22 |         0     | N/A                         | N/A                             |
|   118 | S    |         0.1638  | True      |                          0.10738 |                 96.53 |         2.148 | N/A                         | N/A                             |
|   119 | F    |         0.05216 | False     |                          0.05542 |                 95.9  |        20.517 | N/A                         | N/A                             |
|   120 | E    |         0.06715 | False     |                          0.38384 |                 97.24 |        24.102 | N/A                         | N/A                             |
|   121 | M    |         0.045   | False     |                          0.26257 |                 97.93 |        25.335 | N/A                         | N/A                             |
|   122 | L    |         0.00206 | False     |                          0       |                 97.56 |        25.335 | N/A                         | N/A                             |
|   123 | I    |         0.04777 | False     |                          0.14799 |                 97.37 |        25.335 | N/A                         | N/A                             |
|   124 | L    |         0.03517 | False     |                          0.53984 |                 98.39 |        25.335 | N/A                         | N/A                             |
|   125 | G    |         0.00335 | False     |                          0       |                 98.4  |        25.335 | N/A                         | N/A                             |
|   126 | R    |         0.01372 | False     |                          0.01077 |                 97.42 |        24.102 | N/A                         | N/A                             |
|   127 | F    |         0.03867 | False     |                          0.28042 |                 98.35 |        73.362 | N/A                         | N/A                             |
|   128 | I    |         0.00828 | False     |                          0.15599 |                 98.63 |        76.693 | N/A                         | N/A                             |
|   129 | I    |         0.00292 | False     |                          0       |                 98.35 |        76.62  | N/A                         | N/A                             |
|   130 | G    |         0.00558 | False     |                          0       |                 98.24 |        73.544 | N/A                         | N/A                             |
|   131 | V    |         0.01268 | False     |                          0.16376 |                 98.63 |        73.371 | N/A                         | N/A                             |
|   132 | Y    |         0.00305 | False     |                          0.0091  |                 98.61 |        60.923 | N/A                         | N/A                             |
|   133 | C    |         0.00287 | False     |                          0       |                 98.14 |        16.572 | N/A                         | N/A                             |
|   134 | G    |         0.00571 | False     |                          0.00238 |                 97.8  |         8.913 | N/A                         | N/A                             |
|   135 | L    |         0.00376 | False     |                          0.01319 |                 98.11 |         8.252 | N/A                         | N/A                             |
|   136 | T    |         0.00399 | False     |                          0.02834 |                 97.56 |         4.438 | N/A                         | N/A                             |
|   137 | T    |         0.01062 | False     |                          0.03073 |                 96.16 |         2.229 | N/A                         | N/A                             |
|   138 | G    |         0.0092  | False     |                          0.03083 |                 96.25 |         1.236 | N/A                         | N/A                             |
|   139 | F    |         0.00166 | False     |                          0.00127 |                 96.9  |         1.159 | N/A                         | N/A                             |
|   140 | V    |         0.00065 | False     |                          0       |                 97.72 |         0.134 | N/A                         | N/A                             |
|   141 | P    |         0.0081  | False     |                          0.01115 |                 96.13 |         0.057 | N/A                         | N/A                             |
|   142 | M    |         0.00224 | False     |                          0       |                 95.24 |         0     | N/A                         | N/A                             |
|   143 | Y    |         0.00201 | False     |                          0       |                 97.24 |         0     | N/A                         | N/A                             |
|   144 | V    |         0.00105 | False     |                          0       |                 97.19 |         0     | N/A                         | N/A                             |
|   145 | G    |         0.01758 | False     |                          0.05427 |                 94.08 |         0     | N/A                         | N/A                             |
|   146 | E    |         0.00701 | False     |                          0.00618 |                 94.64 |         0     | N/A                         | N/A                             |
|   147 | V    |         0.00221 | False     |                          0       |                 95.69 |         0     | N/A                         | N/A                             |
|   148 | S    |         0.0171  | False     |                          0.01845 |                 95    |         0     | N/A                         | N/A                             |
|   149 | P    |         0.03865 | False     |                          0.05269 |                 92.82 |         0     | N/A                         | N/A                             |
|   150 | T    |         0.10532 | False     |                          0.23837 |                 90.56 |         0     | N/A                         | N/A                             |
|   151 | A    |         0.16219 | True      |                          0.27624 |                 90.38 |         0     | N/A                         | N/A                             |
|   152 | L    |         0.04161 | False     |                          0.14509 |                 93.37 |         0     | N/A                         | N/A                             |
|   153 | R    |         0.02036 | False     |                          0.02515 |                 94.48 |         0     | N/A                         | N/A                             |
|   154 | G    |         0.00325 | False     |                          0       |                 95.29 |         0     | N/A                         | N/A                             |
|   155 | A    |         0.04468 | False     |                          0.13338 |                 95.84 |         0.001 | N/A                         | N/A                             |
|   156 | L    |         0.0113  | False     |                          0.04369 |                 96.74 |         0.005 | N/A                         | N/A                             |
|   157 | G    |         0.00651 | False     |                          0.01281 |                 96.54 |         0.007 | N/A                         | N/A                             |
|   158 | T    |         0.0025  | False     |                          0       |                 97.57 |         0.031 | N/A                         | N/A                             |
|   159 | L    |         0.00821 | False     |                          0.16322 |                 97.65 |         0.077 | N/A                         | N/A                             |
|   160 | H    |         0.00132 | False     |                          0       |                 97.81 |         0.086 | N/A                         | N/A                             |
|   161 | Q    |         0.02717 | False     |                          0.04724 |                 97.63 |         1.163 | N/A                         | N/A                             |
|   162 | L    |         0.02443 | False     |                          0.18713 |                 98.01 |        28.668 | N/A                         | N/A                             |
|   163 | G    |         0.01116 | False     |                          0.05105 |                 97.89 |        34.027 | N/A                         | N/A                             |
|   164 | I    |         0.02578 | False     |                          0.06    |                 97.43 |        93.568 | N/A                         | N/A                             |
|   165 | V    |         0.02188 | False     |                          0.01821 |                 96.46 |        99.005 | N/A                         | N/A                             |
|   166 | V    |         0.0129  | False     |                          0.31489 |                 97.28 |        99.462 | N/A                         | N/A                             |
|   167 | G    |         0.00204 | False     |                          0       |                 96.82 |        99.439 | N/A                         | N/A                             |
|   168 | I    |         0.02914 | False     |                          0.17519 |                 93.84 |        99.766 | N/A                         | N/A                             |
|   169 | L    |         0.02557 | False     |                          0.21103 |                 94.26 |        99.607 | N/A                         | N/A                             |
|   170 | I    |         0.01539 | False     |                          0.33439 |                 95.56 |        98.519 | N/A                         | N/A                             |
|   171 | A    |         0.00261 | False     |                          0       |                 94.42 |        86.51  | N/A                         | N/A                             |
|   172 | Q    |         0.02731 | False     |                          0.12407 |                 91.05 |        76.352 | N/A                         | N/A                             |
|   173 | V    |         0.01945 | False     |                          0.34941 |                 93.29 |        75.953 | N/A                         | N/A                             |
|   174 | F    |         0.02309 | False     |                          0.33377 |                 94.68 |        71.249 | N/A                         | N/A                             |
|   175 | G    |         0.01962 | False     |                          0.03569 |                 92.82 |        13.584 | N/A                         | N/A                             |
|   176 | L    |         0.10118 | False     |                          0.1763  |                 91.31 |        11.481 | N/A                         | N/A                             |
|   177 | D    |         0.21254 | True      |                          0.62025 |                 89.25 |         0     | N/A                         | N/A                             |
|   178 | S    |         0.23694 | True      |                          0.79148 |                 90.59 |         0     | N/A                         | N/A                             |
|   179 | I    |         0.10292 | False     |                          0.38399 |                 93.81 |         0     | N/A                         | N/A                             |
|   180 | M    |         0.09878 | False     |                          0.20423 |                 94.75 |         0     | N/A                         | N/A                             |
|   181 | G    |         0.02279 | False     |                          0.04367 |                 92.35 |         0     | N/A                         | N/A                             |
|   182 | N    |         0.12025 | False     |                          0.21556 |                 94.22 |         0     | N/A                         | N/A                             |
|   183 | K    |         0.24182 | True      |                          0.65223 |                 93.4  |         0     | N/A                         | N/A                             |
|   184 | D    |         0.35198 | True      |                          0.65221 |                 93.75 |         0     | N/A                         | N/A                             |
|   185 | L    |         0.13443 | False     |                          0.44845 |                 96.56 |         0     | N/A                         | N/A                             |
|   186 | W    |         0.02217 | False     |                          0.00716 |                 96.37 |         0     | N/A                         | N/A                             |
|   187 | P    |         0.03188 | False     |                          0.07953 |                 96.92 |         0.962 | N/A                         | N/A                             |
|   188 | L    |         0.08044 | False     |                          0.54893 |                 96.73 |        79.425 | N/A                         | N/A                             |
|   189 | L    |         0.00337 | False     |                          0       |                 97.04 |        93.708 | N/A                         | N/A                             |
|   190 | L    |         0.0043  | False     |                          0.00122 |                 96.75 |        96.149 | N/A                         | N/A                             |
|   191 | S    |         0.02132 | False     |                          0.12965 |                 97.02 |        96.203 | N/A                         | N/A                             |
|   192 | I    |         0.02876 | False     |                          0.13679 |                 96.1  |        96.397 | N/A                         | N/A                             |
|   193 | I    |         0.00637 | False     |                          0.004   |                 96.18 |        95.913 | N/A                         | N/A                             |
|   194 | F    |         0.02791 | False     |                          0.43665 |                 97.8  |        89.67  | N/A                         | N/A                             |
|   195 | I    |         0.05009 | False     |                          0.57817 |                 97.47 |        10.981 | N/A                         | N/A                             |
|   196 | P    |         0.01328 | False     |                          0.09643 |                 97    |         5.043 | N/A                         | N/A                             |
|   197 | A    |         0.00214 | False     |                          0       |                 97.9  |         0.366 | N/A                         | N/A                             |
|   198 | L    |         0.02273 | False     |                          0.48225 |                 98.2  |         1.155 | N/A                         | N/A                             |
|   199 | L    |         0.01867 | False     |                          0.51275 |                 97.92 |         1.47  | N/A                         | N/A                             |
|   200 | Q    |         0.00868 | False     |                          0.01008 |                 97.93 |         1.47  | N/A                         | N/A                             |
|   201 | C    |         0.02494 | False     |                          0.23007 |                 97.89 |         1.47  | N/A                         | N/A                             |
|   202 | I    |         0.06773 | False     |                          0.55671 |                 97.8  |         1.47  | N/A                         | N/A                             |
|   203 | V    |         0.02848 | False     |                          0.23897 |                 97.73 |         1.408 | N/A                         | N/A                             |
|   204 | L    |         0.00377 | False     |                          0.00069 |                 97.48 |         0     | N/A                         | N/A                             |
|   205 | P    |         0.09813 | False     |                          0.52985 |                 96.56 |         0     | N/A                         | N/A                             |
|   206 | F    |         0.10252 | False     |                          0.75056 |                 96.25 |         0     | N/A                         | N/A                             |
|   207 | C    |         0.0248  | False     |                          0.01627 |                 96.42 |         0     | N/A                         | N/A                             |
|   208 | P    |         0.10717 | False     |                          0.16233 |                 95.71 |         0     | N/A                         | N/A                             |
|   209 | E    |         0.05457 | False     |                          0.05806 |                 96.5  |         0     | N/A                         | N/A                             |
|   210 | S    |         0.00871 | False     |                          0       |                 96.07 |         0     | N/A                         | N/A                             |
|   211 | P    |         0.01204 | False     |                          0.00795 |                 95.78 |         0     | N/A                         | N/A                             |
|   212 | R    |         0.05754 | False     |                          0.04876 |                 92.95 |         0     | N/A                         | N/A                             |
|   213 | F    |         0.03238 | False     |                          0.02484 |                 93.22 |         1.202 | N/A                         | N/A                             |
|   214 | L    |         0.06451 | False     |                          0.04946 |                 95.2  |         1.202 | N/A                         | N/A                             |
|   215 | L    |         0.1101  | False     |                          0.06118 |                 92.92 |         1.202 | N/A                         | N/A                             |
|   216 | I    |         0.12898 | False     |                          0.13534 |                 87.63 |         1.202 | N/A                         | N/A                             |
|   217 | N    |         0.12542 | False     |                          0.39386 |                 87.05 |         1.202 | N/A                         | N/A                             |
|   218 | R    |         0.27788 | True      |                          0.51172 |                 90.04 |         0     | N/A                         | N/A                             |
|   219 | N    |         0.29407 | True      |                          0.84866 |                 90.85 |         0     | N/A                         | N/A                             |
|   220 | E    |         0.11031 | False     |                          0.27839 |                 93.85 |         0     | N/A                         | N/A                             |
|   221 | E    |         0.16431 | True      |                          0.33155 |                 94.32 |         0     | N/A                         | N/A                             |
|   222 | N    |         0.38785 | True      |                          0.81756 |                 95.7  |         0     | N/A                         | N/A                             |
|   223 | R    |         0.21429 | True      |                          0.56278 |                 95.93 |         0     | N/A                         | N/A                             |
|   224 | A    |         0.00375 | False     |                          0       |                 95.96 |         0     | N/A                         | N/A                             |
|   225 | K    |         0.14168 | False     |                          0.41729 |                 96.62 |         0     | N/A                         | N/A                             |
|   226 | S    |         0.13483 | False     |                          0.38056 |                 95.96 |         0     | Phosphoserine; by PKC/PRKCB | N/A                             |
|   227 | V    |         0.07449 | False     |                          0.12567 |                 95.99 |         0     | N/A                         | N/A                             |
|   228 | L    |         0.00904 | False     |                          0.0033  |                 95.16 |         0     | N/A                         | N/A                             |
|   229 | K    |         0.2113  | True      |                          0.37904 |                 95.07 |         0     | N/A                         | N/A                             |
|   230 | K    |         0.15522 | True      |                          0.48468 |                 93.79 |         0     | N/A                         | N/A                             |
|   231 | L    |         0.01028 | False     |                          0.00244 |                 94.95 |         0     | N/A                         | N/A                             |
|   232 | R    |         0.20407 | True      |                          0.08349 |                 93.85 |         0     | N/A                         | N/A                             |
|   233 | G    |         0.26149 | True      |                          0.66226 |                 91.08 |         0     | N/A                         | N/A                             |
|   234 | T    |         0.2509  | True      |                          0.27617 |                 91.01 |         0     | N/A                         | N/A                             |
|   235 | A    |         0.31362 | True      |                          0.74114 |                 88.76 |         0     | N/A                         | N/A                             |
|   236 | D    |         0.19939 | True      |                          0.61177 |                 90.77 |         0     | N/A                         | N/A                             |
|   237 | V    |         0.0472  | False     |                          0.04217 |                 91.62 |         0     | N/A                         | N/A                             |
|   238 | T    |         0.35334 | True      |                          0.68212 |                 91.87 |         0     | N/A                         | N/A                             |
|   239 | H    |         0.26855 | True      |                          0.74569 |                 89.28 |         0     | N/A                         | N/A                             |
|   240 | D    |         0.18117 | True      |                          0.20045 |                 90.11 |         0     | N/A                         | N/A                             |
|   241 | L    |         0.08156 | False     |                          0.07914 |                 92.32 |         0     | N/A                         | N/A                             |
|   242 | Q    |         0.24249 | True      |                          0.40163 |                 92.24 |         0     | N/A                         | N/A                             |
|   243 | E    |         0.18468 | True      |                          0.10925 |                 89.65 |         0     | N/A                         | N/A                             |
|   244 | M    |         0.03631 | False     |                          0.03295 |                 90.58 |         0     | N/A                         | N/A                             |
|   245 | K    |         0.10918 | False     |                          0.32458 |                 91.39 |         0     | N/A                         | N/A                             |
|   246 | E    |         0.16494 | True      |                          0.42264 |                 87.57 |         0     | N/A                         | N/A                             |
|   247 | E    |         0.01882 | False     |                          0.0126  |                 86.29 |         0     | N/A                         | N/A                             |
|   248 | S    |         0.08144 | False     |                          0.18057 |                 86.02 |         0     | N/A                         | N/A                             |
|   249 | R    |         0.27606 | True      |                          0.54602 |                 85.23 |         0     | N/A                         | N/A                             |
|   250 | Q    |         0.15736 | True      |                          0.24308 |                 76.97 |         0     | N/A                         | N/A                             |
|   251 | M    |         0.13186 | False     |                          0.24099 |                 76.59 |         0     | N/A                         | N/A                             |
|   252 | M    |         0.4323  | True      |                          0.86718 |                 74.96 |         0     | N/A                         | N/A                             |
|   253 | R    |         0.31699 | True      |                          0.79508 |                 71.05 |         0     | N/A                         | N/A                             |
|   254 | E    |         0.29329 | True      |                          0.30086 |                 69.89 |         0     | N/A                         | N/A                             |
|   255 | K    |         0.21593 | True      |                          0.85423 |                 68.82 |         0     | N/A                         | N/A                             |
|   256 | K    |         0.25134 | True      |                          0.96149 |                 70.64 |         4.349 | N/A                         | N/A                             |
|   257 | V    |         0.10174 | False     |                          0.16156 |                 78.56 |         4.515 | N/A                         | N/A                             |
|   258 | T    |         0.16987 | True      |                          0.53188 |                 84.78 |         4.515 | N/A                         | N/A                             |
|   259 | I    |         0.11104 | False     |                          0.29305 |                 86.09 |         4.693 | N/A                         | N/A                             |
|   260 | L    |         0.16448 | True      |                          0.6091  |                 86.46 |         4.693 | N/A                         | N/A                             |
|   261 | E    |         0.20409 | True      |                          0.28495 |                 86.34 |         4.693 | N/A                         | N/A                             |
|   262 | L    |         0.0084  | False     |                          0       |                 87.43 |         4.534 | N/A                         | N/A                             |
|   263 | F    |         0.08668 | False     |                          0.51876 |                 89.52 |         4.217 | N/A                         | N/A                             |
|   264 | R    |         0.32461 | True      |                          0.64118 |                 87.07 |         0.344 | N/A                         | N/A                             |
|   265 | S    |         0.19847 | True      |                          0.23032 |                 85.98 |         0     | N/A                         | N/A                             |
|   266 | P    |         0.24778 | True      |                          0.78987 |                 85.14 |         0     | N/A                         | N/A                             |
|   267 | A    |         0.11794 | False     |                          0.3457  |                 85.48 |         0     | N/A                         | N/A                             |
|   268 | Y    |         0.06738 | False     |                          0.12542 |                 89.8  |         0     | N/A                         | N/A                             |
|   269 | R    |         0.13441 | False     |                          0.5362  |                 91.65 |         0     | N/A                         | N/A                             |
|   270 | Q    |         0.08714 | False     |                          0.26093 |                 94.01 |         0     | N/A                         | N/A                             |
|   271 | P    |         0.02428 | False     |                          0.03181 |                 95.21 |         0.403 | N/A                         | N/A                             |
|   272 | I    |         0.024   | False     |                          0.03507 |                 95.46 |        90.267 | N/A                         | N/A                             |
|   273 | L    |         0.02616 | False     |                          0.50121 |                 96.67 |        98.404 | N/A                         | N/A                             |
|   274 | I    |         0.00431 | False     |                          0       |                 97.74 |        99.707 | N/A                         | N/A                             |
|   275 | A    |         0.00114 | False     |                          0       |                 97.24 |        99.733 | N/A                         | N/A                             |
|   276 | V    |         0.01597 | False     |                          0.21612 |                 97.73 |        99.76  | N/A                         | N/A                             |
|   277 | V    |         0.00576 | False     |                          0.14757 |                 98.1  |        98.81  | N/A                         | N/A                             |
|   278 | L    |         0.00413 | False     |                          0.0033  |                 98    |        86.618 | N/A                         | N/A                             |
|   279 | Q    |         0.01635 | False     |                          0.01818 |                 97.68 |        19.033 | N/A                         | N/A                             |
|   280 | L    |         0.0131  | False     |                          0.29512 |                 97.64 |        16.383 | N/A                         | N/A                             |
|   281 | S    |         0.00227 | False     |                          0.00416 |                 97.76 |         1.888 | N/A                         | N/A                             |
|   282 | Q    |         0.01022 | False     |                          0.03823 |                 96.11 |         0.09  | N/A                         | N/A                             |
|   283 | Q    |         0.02085 | False     |                          0.08271 |                 94.45 |         0.036 | N/A                         | N/A                             |
|   284 | L    |         0.00816 | False     |                          0.25143 |                 95.07 |         0.98  | N/A                         | N/A                             |
|   285 | S    |         0.00154 | False     |                          0       |                 95.23 |         1.122 | N/A                         | N/A                             |
|   286 | G    |         0.00289 | False     |                          0.01288 |                 91.59 |         2.555 | N/A                         | N/A                             |
|   287 | I    |         0.0196  | False     |                          0.0576  |                 92.06 |        18.73  | N/A                         | N/A                             |
|   288 | N    |         0.0306  | False     |                          0.21448 |                 84.37 |        20.171 | N/A                         | N/A                             |
|   289 | A    |         0.0051  | False     |                          0.0011  |                 82.48 |        55.39  | N/A                         | N/A                             |
|   290 | V    |         0.00463 | False     |                          0.00476 |                 85.6  |        88.004 | N/A                         | N/A                             |
|   291 | F    |         0.02809 | False     |                          0.25317 |                 81.32 |        90.666 | N/A                         | N/A                             |
|   292 | Y    |         0.09021 | False     |                          0.4089  |                 73.06 |        90.561 | N/A                         | N/A                             |
|   293 | Y    |         0.07831 | False     |                          0.09665 |                 73.34 |        89.45  | N/A                         | N/A                             |
|   294 | S    |         0.00735 | False     |                          0.00104 |                 79.04 |        77.722 | N/A                         | N/A                             |
|   295 | T    |         0.09921 | False     |                          0.39658 |                 76.54 |        75.145 | N/A                         | N/A                             |
|   296 | S    |         0.11733 | False     |                          0.32237 |                 71.3  |        73.555 | N/A                         | N/A                             |
|   297 | I    |         0.05316 | False     |                          0.012   |                 73.18 |        73.372 | N/A                         | N/A                             |
|   298 | F    |         0.01719 | False     |                          0.00637 |                 80.17 |        72.614 | N/A                         | N/A                             |
|   299 | E    |         0.21029 | True      |                          0.61891 |                 79.69 |         0.141 | N/A                         | N/A                             |
|   300 | K    |         0.20778 | True      |                          0.68843 |                 72.71 |         0.141 | N/A                         | N/A                             |
|   301 | A    |         0.1185  | False     |                          0.18518 |                 73.11 |         0.09  | N/A                         | N/A                             |
|   302 | G    |         0.26338 | True      |                          0.69132 |                 71.83 |         0.046 | N/A                         | N/A                             |
|   303 | V    |         0.14308 | False     |                          0.35576 |                 73.59 |         0.046 | N/A                         | N/A                             |
|   304 | Q    |         0.30933 | True      |                          0.88755 |                 72.79 |         0     | N/A                         | N/A                             |
|   305 | Q    |         0.20282 | True      |                          0.52297 |                 76.77 |         0     | N/A                         | N/A                             |
|   306 | P    |         0.09381 | False     |                          0.21472 |                 75.1  |         0.001 | N/A                         | N/A                             |
|   307 | V    |         0.08895 | False     |                          0.56599 |                 77.66 |         0.123 | N/A                         | N/A                             |
|   308 | Y    |         0.18319 | True      |                          0.55417 |                 79.92 |         0.124 | N/A                         | N/A                             |
|   309 | A    |         0.04148 | False     |                          0.15034 |                 78.08 |         0.125 | N/A                         | N/A                             |
|   310 | T    |         0.0322  | False     |                          0.17328 |                 81.14 |         0.129 | N/A                         | N/A                             |
|   311 | I    |         0.06751 | False     |                          0.11759 |                 86.34 |         0.619 | N/A                         | N/A                             |
|   312 | G    |         0.03452 | False     |                          0.22856 |                 88.13 |         0.547 | N/A                         | N/A                             |
|   313 | S    |         0.00692 | False     |                          0.00416 |                 87.79 |         1.044 | N/A                         | N/A                             |
|   314 | G    |         0.02753 | False     |                          0.02169 |                 90.19 |         5.068 | N/A                         | N/A                             |
|   315 | I    |         0.0302  | False     |                          0.57173 |                 94.75 |        49.782 | N/A                         | N/A                             |
|   316 | V    |         0.01077 | False     |                          0.2066  |                 95.25 |        53.875 | N/A                         | N/A                             |
|   317 | N    |         0.01595 | False     |                          0.0408  |                 94.59 |        54.222 | N/A                         | N/A                             |
|   318 | T    |         0.02029 | False     |                          0.15138 |                 97.22 |        63.147 | N/A                         | N/A                             |
|   319 | A    |         0.01421 | False     |                          0.45329 |                 97.98 |        78.15  | N/A                         | N/A                             |
|   320 | F    |         0.03082 | False     |                          0.37836 |                 97.91 |        95.889 | N/A                         | N/A                             |
|   321 | T    |         0.00232 | False     |                          0       |                 97.9  |        97.335 | N/A                         | N/A                             |
|   322 | V    |         0.01379 | False     |                          0.41034 |                 97.93 |        99.767 | N/A                         | N/A                             |
|   323 | V    |         0.01743 | False     |                          0.47508 |                 97.77 |        99.971 | N/A                         | N/A                             |
|   324 | S    |         0.00223 | False     |                          0.00104 |                 97.6  |        99.96  | N/A                         | N/A                             |
|   325 | L    |         0.03195 | False     |                          0.18043 |                 95.69 |        99.956 | N/A                         | N/A                             |
|   326 | F    |         0.08123 | False     |                          0.67175 |                 95.25 |        99.935 | N/A                         | N/A                             |
|   327 | V    |         0.01279 | False     |                          0.35512 |                 96.52 |        99.673 | N/A                         | N/A                             |
|   328 | V    |         0.00365 | False     |                          0       |                 96.2  |        98.549 | N/A                         | N/A                             |
|   329 | E    |         0.05787 | False     |                          0.17271 |                 93.26 |         0.038 | N/A                         | N/A                             |
|   330 | R    |         0.2112  | True      |                          0.79763 |                 93.66 |         0.038 | N/A                         | N/A                             |
|   331 | A    |         0.05944 | False     |                          0.35934 |                 95.39 |         0.009 | N/A                         | N/A                             |
|   332 | G    |         0.02052 | False     |                          0.01288 |                 94.57 |         0     | N/A                         | N/A                             |
|   333 | R    |         0.00902 | False     |                          0.00795 |                 96.69 |         0     | N/A                         | N/A                             |
|   334 | R    |         0.03216 | False     |                          0.31857 |                 97.34 |         0     | N/A                         | N/A                             |
|   335 | T    |         0.04661 | False     |                          0.42038 |                 97.73 |         0     | N/A                         | N/A                             |
|   336 | L    |         0.00535 | False     |                          0.02391 |                 97.88 |         0.011 | N/A                         | N/A                             |
|   337 | H    |         0.00144 | False     |                          0.00441 |                 98.39 |         0.021 | N/A                         | N/A                             |
|   338 | L    |         0.01806 | False     |                          0.14565 |                 98.6  |         1.182 | N/A                         | N/A                             |
|   339 | I    |         0.02039 | False     |                          0.48397 |                 98.31 |         1.22  | N/A                         | N/A                             |
|   340 | G    |         0.00163 | False     |                          0       |                 98.25 |         1.22  | N/A                         | N/A                             |
|   341 | L    |         0.00189 | False     |                          0.00183 |                 98.53 |         1.498 | N/A                         | N/A                             |
|   342 | A    |         0.01291 | False     |                          0.47839 |                 98.41 |         1.544 | N/A                         | N/A                             |
|   343 | G    |         0.00909 | False     |                          0.15416 |                 98.14 |         0.685 | N/A                         | N/A                             |
|   344 | M    |         0.00213 | False     |                          0       |                 98.1  |         1.355 | N/A                         | N/A                             |
|   345 | A    |         0.00846 | False     |                          0.09821 |                 97.98 |         1.871 | N/A                         | N/A                             |
|   346 | G    |         0.00884 | False     |                          0.37463 |                 97.71 |         2.536 | N/A                         | N/A                             |
|   347 | C    |         0.01683 | False     |                          0.07633 |                 96.25 |        10.286 | N/A                         | N/A                             |
|   348 | A    |         0.00293 | False     |                          0       |                 94.68 |        46.972 | N/A                         | N/A                             |
|   349 | I    |         0.02569 | False     |                          0.50398 |                 95.73 |        90.298 | N/A                         | N/A                             |
|   350 | L    |         0.01426 | False     |                          0.4501  |                 94.22 |        94.498 | N/A                         | N/A                             |
|   351 | M    |         0.0028  | False     |                          0.00067 |                 91.24 |        95.257 | N/A                         | N/A                             |
|   352 | T    |         0.03746 | False     |                          0.10123 |                 91.66 |        95.85  | N/A                         | N/A                             |
|   353 | I    |         0.06506 | False     |                          0.46958 |                 92.45 |        96.739 | N/A                         | N/A                             |
|   354 | A    |         0.0052  | False     |                          0       |                 90.63 |        95.287 | N/A                         | N/A                             |
|   355 | L    |         0.07082 | False     |                          0.0952  |                 87.14 |        93.95  | N/A                         | N/A                             |
|   356 | A    |         0.09028 | False     |                          0.36356 |                 88.19 |        86.591 | N/A                         | N/A                             |
|   357 | L    |         0.08454 | False     |                          0.36684 |                 90.34 |        80.413 | N/A                         | N/A                             |
|   358 | L    |         0.11118 | False     |                          0.10179 |                 85.48 |        67.977 | N/A                         | N/A                             |
|   359 | E    |         0.31884 | True      |                          0.86457 |                 82.69 |         0     | N/A                         | N/A                             |
|   360 | Q    |         0.36425 | True      |                          0.6842  |                 88.03 |         0     | N/A                         | N/A                             |
|   361 | L    |         0.24535 | True      |                          0.42866 |                 88.57 |         0     | N/A                         | N/A                             |
|   362 | P    |         0.21393 | True      |                          0.76601 |                 83.6  |         0.458 | N/A                         | N/A                             |
|   363 | W    |         0.2051  | True      |                          0.62202 |                 86.61 |        37.8   | N/A                         | N/A                             |
|   364 | M    |         0.06577 | False     |                          0.06328 |                 88.22 |        42.014 | N/A                         | N/A                             |
|   365 | S    |         0.035   | False     |                          0.02214 |                 85.14 |        45.708 | N/A                         | N/A                             |
|   366 | Y    |         0.18751 | True      |                          0.66325 |                 86.98 |        75.488 | N/A                         | N/A                             |
|   367 | L    |         0.02295 | False     |                          0.31115 |                 90.96 |        84.124 | N/A                         | N/A                             |
|   368 | S    |         0.00516 | False     |                          0       |                 88.59 |        85.706 | N/A                         | N/A                             |
|   369 | I    |         0.03204 | False     |                          0.16639 |                 88.4  |        98.583 | N/A                         | N/A                             |
|   370 | V    |         0.01556 | False     |                          0.69957 |                 91.75 |        99.76  | N/A                         | N/A                             |
|   371 | A    |         0.00406 | False     |                          0.0153  |                 93.62 |        99.859 | N/A                         | N/A                             |
|   372 | I    |         0.00438 | False     |                          0.0008  |                 91.53 |        99.976 | N/A                         | N/A                             |
|   373 | F    |         0.01376 | False     |                          0.30421 |                 93.3  |        99.976 | N/A                         | N/A                             |
|   374 | G    |         0.00534 | False     |                          0.22766 |                 96.4  |        99.831 | N/A                         | N/A                             |
|   375 | F    |         0.00114 | False     |                          0.00064 |                 96.48 |        99.827 | N/A                         | N/A                             |
|   376 | V    |         0.00422 | False     |                          0       |                 95.95 |        99.664 | N/A                         | N/A                             |
|   377 | A    |         0.00628 | False     |                          0.07908 |                 97.64 |        97.749 | N/A                         | N/A                             |
|   378 | F    |         0.01538 | False     |                          0.36753 |                 98.33 |        96.129 | N/A                         | N/A                             |
|   379 | F    |         0.00941 | False     |                          0.05796 |                 98.16 |        88.881 | N/A                         | N/A                             |
|   380 | E    |         0.00234 | False     |                          0.00464 |                 97.91 |         0     | N/A                         | N/A                             |
|   381 | V    |         0.00422 | False     |                          0.14091 |                 96.33 |         0     | N/A                         | N/A                             |
|   382 | G    |         0.00208 | False     |                          0       |                 95.49 |         0     | N/A                         | N/A                             |
|   383 | P    |         0.00114 | False     |                          0       |                 97.5  |         0     | N/A                         | N/A                             |
|   384 | G    |         0.00136 | False     |                          0       |                 96.26 |         0     | N/A                         | N/A                             |
|   385 | P    |         0.00247 | False     |                          0.00367 |                 96.84 |         0     | N/A                         | N/A                             |
|   386 | I    |         0.00271 | False     |                          0.0024  |                 97.42 |         0     | N/A                         | N/A                             |
|   387 | P    |         0.00136 | False     |                          0       |                 97.26 |         1.451 | N/A                         | N/A                             |
|   388 | W    |         0.01211 | False     |                          0.05076 |                 94.16 |        55.652 | N/A                         | N/A                             |
|   389 | F    |         0.01482 | False     |                          0.0233  |                 93.55 |        55.652 | N/A                         | N/A                             |
|   390 | I    |         0.00639 | False     |                          0.0024  |                 95.77 |        55.652 | N/A                         | N/A                             |
|   391 | V    |         0.00521 | False     |                          0.01523 |                 94.26 |        55.652 | N/A                         | N/A                             |
|   392 | A    |         0.00588 | False     |                          0.00893 |                 91.33 |        54.866 | N/A                         | N/A                             |
|   393 | E    |         0.02016 | False     |                          0.0184  |                 93.38 |         0     | N/A                         | N/A                             |
|   394 | L    |         0.00533 | False     |                          0.00975 |                 93.48 |         0     | N/A                         | N/A                             |
|   395 | F    |         0.02255 | False     |                          0.01441 |                 91.08 |         0     | N/A                         | N/A                             |
|   396 | S    |         0.0402  | False     |                          0.11531 |                 86.67 |         0     | N/A                         | N/A                             |
|   397 | Q    |         0.02444 | False     |                          0.02271 |                 82.61 |         0     | N/A                         | N/A                             |
|   398 | G    |         0.08535 | False     |                          0.31088 |                 84.03 |         0     | N/A                         | N/A                             |
|   399 | P    |         0.04376 | False     |                          0.02187 |                 88.25 |         0     | N/A                         | N/A                             |
|   400 | R    |         0.00813 | False     |                          0       |                 91.11 |         0     | N/A                         | N/A                             |
|   401 | P    |         0.01591 | False     |                          0.01988 |                 90.46 |         0     | N/A                         | N/A                             |
|   402 | A    |         0.02021 | False     |                          0.11554 |                 91.55 |         4.16  | N/A                         | N/A                             |
|   403 | A    |         0.00189 | False     |                          0       |                 93.92 |        13.165 | N/A                         | N/A                             |
|   404 | I    |         0.01296 | False     |                          0.05255 |                 94.45 |        19.369 | N/A                         | N/A                             |
|   405 | A    |         0.0065  | False     |                          0.01148 |                 94.67 |        19.818 | N/A                         | N/A                             |
|   406 | V    |         0.01086 | False     |                          0.08093 |                 96.02 |        19.818 | N/A                         | N/A                             |
|   407 | A    |         0.00485 | False     |                          0.01275 |                 96.93 |        18.44  | N/A                         | N/A                             |
|   408 | G    |         0.03389 | False     |                          0.07567 |                 96.07 |        13.517 | N/A                         | N/A                             |
|   409 | F    |         0.04564 | False     |                          0.42427 |                 96.34 |        12.674 | N/A                         | N/A                             |
|   410 | S    |         0.01447 | False     |                          0.12126 |                 96.83 |         1.885 | N/A                         | N/A                             |
|   411 | N    |         0.0085  | False     |                          0.00509 |                 96.51 |         0.634 | N/A                         | N/A                             |
|   412 | W    |         0.01738 | False     |                          0.01266 |                 95.73 |         2.559 | N/A                         | N/A                             |
|   413 | T    |         0.01207 | False     |                          0.26563 |                 95.8  |         2.73  | N/A                         | N/A                             |
|   414 | S    |         0.02455 | False     |                          0.02348 |                 94.49 |         3.018 | N/A                         | N/A                             |
|   415 | N    |         0.03202 | False     |                          0.20313 |                 91.94 |         4.331 | N/A                         | N/A                             |
|   416 | F    |         0.0328  | False     |                          0.31297 |                 91.59 |        35.517 | N/A                         | N/A                             |
|   417 | I    |         0.02539 | False     |                          0.51678 |                 91.06 |        37.491 | N/A                         | N/A                             |
|   418 | V    |         0.02902 | False     |                          0.08093 |                 87.97 |        37.6   | N/A                         | N/A                             |
|   419 | G    |         0.05727 | False     |                          0.46528 |                 82.86 |        35.805 | N/A                         | N/A                             |
|   420 | M    |         0.06085 | False     |                          0.41617 |                 83.8  |        35.61  | N/A                         | N/A                             |
|   421 | C    |         0.02188 | False     |                          0.43566 |                 84.93 |        29.696 | N/A                         | N/A                             |
|   422 | F    |         0.0447  | False     |                          0.03642 |                 82.87 |        28.399 | N/A                         | N/A                             |
|   423 | Q    |         0.21706 | True      |                          0.52618 |                 78.96 |        11.199 | N/A                         | N/A                             |
|   424 | Y    |         0.18531 | True      |                          0.66412 |                 84.3  |        10.629 | N/A                         | N/A                             |
|   425 | V    |         0.03923 | False     |                          0.35703 |                 86.46 |         9.912 | N/A                         | N/A                             |
|   426 | E    |         0.08543 | False     |                          0.2491  |                 81.43 |         0     | N/A                         | N/A                             |
|   427 | Q    |         0.27454 | True      |                          0.75931 |                 82.28 |         0     | N/A                         | N/A                             |
|   428 | L    |         0.26575 | True      |                          0.95164 |                 87.86 |         0     | N/A                         | N/A                             |
|   429 | C    |         0.07772 | False     |                          0.30353 |                 86.06 |         0     | N/A                         | N/A                             |
|   430 | G    |         0.17333 | True      |                          0.28308 |                 81.82 |         0     | N/A                         | N/A                             |
|   431 | P    |         0.13388 | False     |                          0.34892 |                 77.21 |         0.308 | N/A                         | N/A                             |
|   432 | Y    |         0.15026 | True      |                          0.56028 |                 89.18 |        39.361 | N/A                         | N/A                             |
|   433 | V    |         0.01579 | False     |                          0.00476 |                 88.85 |        94.866 | N/A                         | N/A                             |
|   434 | F    |         0.00409 | False     |                          0.00064 |                 90.55 |        99.583 | N/A                         | N/A                             |
|   435 | I    |         0.03155 | False     |                          0.49278 |                 93.65 |        99.961 | N/A                         | N/A                             |
|   436 | I    |         0.06024 | False     |                          0.44596 |                 93.54 |        99.996 | N/A                         | N/A                             |
|   437 | F    |         0.02967 | False     |                          0.07771 |                 93.29 |        99.999 | N/A                         | N/A                             |
|   438 | T    |         0.02221 | False     |                          0.11977 |                 96.81 |       100     | N/A                         | N/A                             |
|   439 | V    |         0.03392 | False     |                          0.5717  |                 97.87 |       100     | N/A                         | N/A                             |
|   440 | L    |         0.01714 | False     |                          0.28852 |                 97.52 |       100     | N/A                         | N/A                             |
|   441 | L    |         0.00399 | False     |                          0.00191 |                 98.41 |       100     | N/A                         | N/A                             |
|   442 | V    |         0.01211 | False     |                          0.47508 |                 98.44 |       100     | N/A                         | N/A                             |
|   443 | L    |         0.01562 | False     |                          0.60603 |                 98.49 |       100     | N/A                         | N/A                             |
|   444 | F    |         0.01298 | False     |                          0.0962  |                 98.52 |        99.999 | N/A                         | N/A                             |
|   445 | F    |         0.02792 | False     |                          0.34114 |                 98.58 |        99.986 | N/A                         | N/A                             |
|   446 | I    |         0.04985 | False     |                          0.48558 |                 98.47 |        99.825 | N/A                         | N/A                             |
|   447 | F    |         0.06107 | False     |                          0.18867 |                 98.48 |        98.071 | N/A                         | N/A                             |
|   448 | T    |         0.00576 | False     |                          0.00796 |                 98.1  |        76.776 | N/A                         | N/A                             |
|   449 | Y    |         0.09972 | False     |                          0.4683  |                 97.9  |        64.107 | N/A                         | N/A                             |
|   450 | F    |         0.21471 | True      |                          0.74281 |                 97.02 |        48.149 | N/A                         | N/A                             |
|   451 | K    |         0.08174 | False     |                          0.44423 |                 95.72 |         0     | N/A                         | N/A                             |
|   452 | V    |         0.01371 | False     |                          0.03659 |                 96.52 |         0     | N/A                         | N/A                             |
|   453 | P    |         0.08577 | False     |                          0.26315 |                 95.59 |         0     | N/A                         | N/A                             |
|   454 | E    |         0.04158 | False     |                          0.23445 |                 95.89 |         0     | N/A                         | N/A                             |
|   455 | T    |         0.01991 | False     |                          0.01971 |                 94.89 |         0     | N/A                         | N/A                             |
|   456 | K    |         0.0775  | False     |                          0.37378 |                 93.41 |         0     | N/A                         | N/A                             |
|   457 | G    |         0.185   | True      |                          0.60584 |                 90.48 |         0     | N/A                         | N/A                             |
|   458 | R    |         0.14972 | True      |                          0.45733 |                 92.16 |         0     | N/A                         | N/A                             |
|   459 | T    |         0.13178 | False     |                          0.1584  |                 89.9  |         0     | N/A                         | N/A                             |
|   460 | F    |         0.02029 | False     |                          0.00863 |                 87.97 |         0     | N/A                         | N/A                             |
|   461 | D    |         0.16263 | True      |                          0.1813  |                 85.84 |         0     | N/A                         | N/A                             |
|   462 | E    |         0.12921 | False     |                          0.468   |                 89.28 |         0     | N/A                         | N/A                             |
|   463 | I    |         0.02596 | False     |                          0.03826 |                 91.21 |         0     | N/A                         | N/A                             |
|   464 | A    |         0.07618 | False     |                          0.16775 |                 87.26 |         0     | N/A                         | N/A                             |
|   465 | S    |         0.18182 | True      |                          0.28892 |                 85.19 |         0     | Phosphoserine               | N/A                             |
|   466 | G    |         0.21237 | True      |                          0.51141 |                 87.08 |         0     | N/A                         | N/A                             |
|   467 | F    |         0.09746 | False     |                          0.16434 |                 87.17 |         0     | N/A                         | N/A                             |
|   468 | R    |         0.26883 | True      |                          0.34912 |                 78.89 |         0     | N/A                         | N/A                             |
|   469 | Q    |         0.14395 | False     |                          0.67404 |                 72.64 |         0     | N/A                         | N/A                             |
|   470 | G    |         0.11279 | False     |                          0.40317 |                 59.92 |         0     | N/A                         | N/A                             |
|   471 | G    |         0.15478 | True      |                          0.48009 |                 51.52 |         0     | N/A                         | N/A                             |
|   472 | A    |         0.10567 | False     |                          0.553   |                 47.63 |         0     | N/A                         | N/A                             |
|   473 | S    |         0.15109 | True      |                          0.43349 |                 45.04 |         0     | N/A                         | N/A                             |
|   474 | Q    |         0.21641 | True      |                          0.60323 |                 38.9  |         0     | N/A                         | N/A                             |
|   475 | S    |         0.20095 | True      |                          0.71081 |                 41.67 |         0     | N/A                         | N/A                             |
|   476 | D    |         0.29214 | True      |                          0.80626 |                 37.09 |         0     | N/A                         | N/A                             |
|   477 | K    |         0.2173  | True      |                          0.46239 |                 32.26 |         0     | N/A                         | N/A                             |
|   478 | T    |         0.27772 | True      |                          0.62118 |                 38.64 |         0     | Phosphothreonine            | N/A                             |
|   479 | P    |         0.2634  | True      |                          0.73858 |                 42.78 |         0     | N/A                         | N/A                             |
|   480 | E    |         0.39955 | True      |                          0.79998 |                 44.86 |         0     | N/A                         | N/A                             |
|   481 | E    |         0.24257 | True      |                          0.51968 |                 41.08 |         0     | N/A                         | N/A                             |
|   482 | L    |         0.28062 | True      |                          0.70358 |                 39.5  |         0     | N/A                         | N/A                             |
|   483 | F    |         0.34924 | True      |                          0.90723 |                 34.84 |         0     | N/A                         | N/A                             |
|   484 | H    |         0.24652 | True      |                          0.84548 |                 34.11 |         0     | N/A                         | N/A                             |
|   485 | P    |         0.19971 | True      |                          0.86302 |                 35.91 |         0     | N/A                         | N/A                             |
|   486 | L    |         0.24757 | True      |                          1.0868  |                 38.28 |         0     | N/A                         | N/A                             |
|   487 | G    |         0.18626 | True      |                          0.87308 |                 32.43 |         0     | N/A                         | N/A                             |
|   488 | A    |         0.14823 | False     |                          0.90452 |                 32.35 |         0     | N/A                         | N/A                             |
|   489 | D    |         0.2756  | True      |                          0.84366 |                 30.39 |         0     | N/A                         | N/A                             |
|   490 | S    |         0.25866 | True      |                          0.78919 |                 35.93 |         0     | Phosphoserine               | N/A                             |
|   491 | Q    |         0.19133 | True      |                          0.87633 |                 27.35 |         0     | N/A                         | N/A                             |
|   492 | V    |         0.12419 | False     |                          1.49727 |                 38.16 |         0     | N/A                         | N/A                             |


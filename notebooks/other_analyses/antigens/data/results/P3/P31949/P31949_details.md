# Detailed Data for P31949


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: P31949
- **Gene Name**: S100A11
- **Protein Name**: S100 calcium binding protein A11. calgizzarin
- **Swiss Prot**: S111_HUMAN
- **Family**: other
- **Biomarker Application**:  
- **Number of Isoforms**: 0
- **Regulation**: 1
- **(transcriptomics) AUC**: nan
- **(transcriptomics) Fold Change**: nan
- **(transcriptomics) Regulation**: Downregulated
- **Discotope Epitope Count**: 24
- **Max n_uniprots (Homo)**: 2
- **Max n_uniprots (Hetero)**: N/A


## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| S100A11           | ANXA1             |   0.998 |
| S100A11           | ANXA2             |   0.996 |
| S100A11           | AGER              |   0.961 |

## Homologs

| uniprot_id   | gene_id   |
|:-------------|:----------|
| P23297       | S100A1    |
| P33764       | S100A3    |
| P25815       | S100P     |
| P29377       | S100G     |
| P33763       | S100A5    |
| Q9HCY8       | S100A14   |
| P80511       | S100A12   |
| P26447       | S100A4    |
| P60903       | S100A10   |
| Q96FQ6       | S100A16   |
| P05109       | S100A8    |
| P06703       | S100A6    |
| C9JRU3       | SNTN      |
| P29034       | S100A2    |
| Q99584       | S100A13   |
| Q8WXG8       | S100Z     |
| P04271       | S100B     |
| P06702       | S100A9    |
| P31151       | S100A7    |
| Q86SG5       | S100A7A   |
| Q9UBG3       | CRNN      |

## Biological Assemblies

|   Unnamed: 0 |   assembly |   n_uniprots | composition   | crystal_id   |
|-------------:|-----------:|-------------:|:--------------|:-------------|
|            0 |          1 |            2 | Homo          | 2luc         |
|            0 |          1 |            1 | Homo          | 1v4z         |
|            0 |          1 |            1 | Homo          | 1v50         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification                                                 |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:-------------------------------------------------------------|
|     1 | M    |         0.418   | False     |                          1.29892 |                 51.2  |         0     | N-acetylmethionine                                           |
|     2 | A    |         0.42303 | False     |                          0.92416 |                 65.76 |         0     | N-acetylalanine; in Protein S100-A11, N-terminally processed |
|     3 | K    |         0.4953  | True      |                          0.98937 |                 65.56 |         0     | N6-acetyllysine                                              |
|     4 | I    |         0.61359 | True      |                          1.01568 |                 76.14 |         0     | N/A                                                          |
|     5 | S    |         0.46988 | True      |                          0.70472 |                 85.04 |         0     | Phosphoserine                                                |
|     6 | S    |         0.42523 | False     |                          0.67183 |                 90.05 |         0     | Phosphoserine                                                |
|     7 | P    |         0.41141 | False     |                          0.37788 |                 92.03 |         0     | N/A                                                          |
|     8 | T    |         0.44068 | False     |                          0.56489 |                 96.43 |         0     | N/A                                                          |
|     9 | E    |         0.40983 | False     |                          0.64554 |                 96.4  |         0     | N/A                                                          |
|    10 | T    |         0.46267 | True      |                          0.64394 |                 96.44 |         0     | Phosphothreonine                                             |
|    11 | E    |         0.28904 | False     |                          0.43481 |                 96.16 |         0     | N/A                                                          |
|    12 | R    |         0.43042 | False     |                          0.4288  |                 96.9  |         0.017 | N/A                                                          |
|    13 | C    |         0.2596  | False     |                          0.47407 |                 96.63 |         0.017 | N/A                                                          |
|    14 | I    |         0.46586 | True      |                          0.53038 |                 96.61 |         0.017 | N/A                                                          |
|    15 | E    |         0.35079 | False     |                          0.50456 |                 95.68 |         0.017 | N/A                                                          |
|    16 | S    |         0.36654 | False     |                          0.4887  |                 96.53 |        10.428 | N/A                                                          |
|    17 | L    |         0.29207 | False     |                          0.34705 |                 96.43 |        93.384 | N/A                                                          |
|    18 | I    |         0.47539 | True      |                          0.37118 |                 95.69 |        93.462 | N/A                                                          |
|    19 | A    |         0.34303 | False     |                          0.55004 |                 94.82 |        93.462 | N/A                                                          |
|    20 | V    |         0.21403 | False     |                          0.315   |                 95.71 |        93.462 | N/A                                                          |
|    21 | F    |         0.13695 | False     |                          0.0416  |                 95.77 |        93.353 | N/A                                                          |
|    22 | Q    |         0.52887 | True      |                          0.56042 |                 93.45 |         3.563 | N/A                                                          |
|    23 | K    |         0.39972 | False     |                          0.58381 |                 93.78 |         0     | N/A                                                          |
|    24 | Y    |         0.06297 | False     |                          0.02095 |                 95.22 |         0     | N/A                                                          |
|    25 | A    |         0.0879  | False     |                          0.06505 |                 93.7  |         0     | N/A                                                          |
|    26 | G    |         0.34315 | False     |                          0.16819 |                 81.42 |         0     | N/A                                                          |
|    27 | K    |         0.38637 | False     |                          0.6408  |                 79.1  |         0     | N6-acetyllysine                                              |
|    28 | D    |         0.64287 | True      |                          0.56172 |                 75.32 |         0     | N/A                                                          |
|    29 | G    |         0.60592 | True      |                          0.73462 |                 73.69 |         0     | N/A                                                          |
|    30 | Y    |         0.67997 | True      |                          0.74507 |                 74.69 |         0.254 | N/A                                                          |
|    31 | N    |         0.47537 | True      |                          0.59888 |                 76.88 |         0.254 | N/A                                                          |
|    32 | Y    |         0.64118 | True      |                          0.8196  |                 89.21 |         0.254 | N/A                                                          |
|    33 | T    |         0.25645 | False     |                          0.16153 |                 95.43 |         0.254 | N/A                                                          |
|    34 | L    |         0.0103  | False     |                          0.00247 |                 96.34 |         0.254 | N/A                                                          |
|    35 | S    |         0.33196 | False     |                          0.16897 |                 94.87 |         0     | N/A                                                          |
|    36 | K    |         0.35203 | False     |                          0.4329  |                 93.53 |         0     | N/A                                                          |
|    37 | T    |         0.37712 | False     |                          0.67781 |                 93.84 |         0     | N/A                                                          |
|    38 | E    |         0.15033 | False     |                          0.03221 |                 95.65 |         0     | N/A                                                          |
|    39 | F    |         0.01034 | False     |                          0.00064 |                 95.91 |         2.593 | N/A                                                          |
|    40 | L    |         0.33709 | False     |                          0.32041 |                 94.17 |         2.593 | N/A                                                          |
|    41 | S    |         0.34118 | False     |                          0.31846 |                 94.79 |         2.593 | N/A                                                          |
|    42 | F    |         0.04946 | False     |                          0.0242  |                 96.17 |         2.593 | N/A                                                          |
|    43 | M    |         0.02232 | False     |                          0       |                 95.6  |         2.593 | N/A                                                          |
|    44 | N    |         0.37602 | False     |                          0.50064 |                 93.73 |         0     | N/A                                                          |
|    45 | T    |         0.58445 | True      |                          0.58567 |                 95.12 |         0     | N/A                                                          |
|    46 | E    |         0.35065 | False     |                          0.36509 |                 95.02 |         0     | N/A                                                          |
|    47 | L    |         0.27037 | False     |                          0.26379 |                 92.84 |         4.642 | N/A                                                          |
|    48 | A    |         0.25217 | False     |                          0.25402 |                 92.44 |         4.642 | N/A                                                          |
|    49 | A    |         0.35233 | False     |                          0.70748 |                 89.92 |         4.642 | N/A                                                          |
|    50 | F    |         0.38136 | False     |                          0.36511 |                 87.14 |         4.642 | N/A                                                          |
|    51 | T    |         0.1231  | False     |                          0.11967 |                 87.43 |         4.642 | N/A                                                          |
|    52 | K    |         0.5313  | True      |                          0.84086 |                 88.53 |         0     | N/A                                                          |
|    53 | N    |         0.47424 | True      |                          0.74912 |                 89.65 |         0     | N/A                                                          |
|    54 | Q    |         0.3225  | False     |                          0.30572 |                 86.28 |         0     | N/A                                                          |
|    55 | K    |         0.51154 | True      |                          1.01024 |                 87.22 |         0     | N/A                                                          |
|    56 | D    |         0.46333 | True      |                          0.35637 |                 90.77 |         0     | N/A                                                          |
|    57 | P    |         0.34027 | False     |                          0.9899  |                 82.75 |         0     | N/A                                                          |
|    58 | G    |         0.29606 | False     |                          0.27118 |                 91.28 |         0     | N/A                                                          |
|    59 | V    |         0.2766  | False     |                          0.23388 |                 93.04 |         0     | N/A                                                          |
|    60 | L    |         0.18577 | False     |                          0.11355 |                 93.63 |         0     | N/A                                                          |
|    61 | D    |         0.353   | False     |                          0.29856 |                 93.95 |         0     | N/A                                                          |
|    62 | R    |         0.65502 | True      |                          0.53189 |                 94.44 |         0     | N/A                                                          |
|    63 | M    |         0.29829 | False     |                          0.25066 |                 94.55 |         0     | N/A                                                          |
|    64 | M    |         0.16936 | False     |                          0.04674 |                 95.04 |         0     | N/A                                                          |
|    65 | K    |         0.46257 | True      |                          0.79002 |                 95.7  |         0     | N/A                                                          |
|    66 | K    |         0.47337 | True      |                          0.83665 |                 96.2  |         0     | N/A                                                          |
|    67 | L    |         0.12374 | False     |                          0.09233 |                 96.63 |         0     | N/A                                                          |
|    68 | D    |         0.40957 | False     |                          0.11186 |                 97.21 |         0     | N/A                                                          |
|    69 | T    |         0.46557 | True      |                          0.69379 |                 96.19 |         0     | N/A                                                          |
|    70 | N    |         0.29843 | False     |                          0.55743 |                 96.26 |         0     | N/A                                                          |
|    71 | S    |         0.56701 | True      |                          0.72664 |                 94.71 |         0     | N/A                                                          |
|    72 | D    |         0.41882 | False     |                          0.46686 |                 94.76 |         0     | N/A                                                          |
|    73 | G    |         0.39334 | False     |                          0.49429 |                 93.76 |         0     | N/A                                                          |
|    74 | Q    |         0.40321 | False     |                          0.29762 |                 94.82 |         0     | N/A                                                          |
|    75 | L    |         0.0072  | False     |                          0       |                 96.76 |         0     | N/A                                                          |
|    76 | D    |         0.34884 | False     |                          0.30412 |                 96.47 |         0     | N/A                                                          |
|    77 | F    |         0.35892 | False     |                          0.31782 |                 96.03 |         0     | N/A                                                          |
|    78 | S    |         0.34542 | False     |                          0.55798 |                 96.96 |         0     | N/A                                                          |
|    79 | E    |         0.09471 | False     |                          0.0279  |                 97.7  |         0     | N/A                                                          |
|    80 | F    |         0.01068 | False     |                          0.00255 |                 96.91 |         4.18  | N/A                                                          |
|    81 | L    |         0.47651 | True      |                          0.41926 |                 97.46 |         4.18  | N/A                                                          |
|    82 | N    |         0.34787 | False     |                          0.53077 |                 96.72 |         4.18  | N/A                                                          |
|    83 | L    |         0.09287 | False     |                          0.0253  |                 95.69 |         4.745 | N/A                                                          |
|    84 | I    |         0.31881 | False     |                          0.20656 |                 96.3  |         4.745 | N/A                                                          |
|    85 | G    |         0.46687 | True      |                          0.35713 |                 96.32 |         1.296 | N/A                                                          |
|    86 | G    |         0.40938 | False     |                          0.37987 |                 95.23 |         0.985 | N/A                                                          |
|    87 | L    |         0.28009 | False     |                          0.27421 |                 92.59 |         0.985 | N/A                                                          |
|    88 | A    |         0.27488 | False     |                          0.54078 |                 95.07 |         0.67  | N/A                                                          |
|    89 | M    |         0.31253 | False     |                          0.71888 |                 95.8  |         0.404 | N/A                                                          |
|    90 | A    |         0.35546 | False     |                          0.54704 |                 92.57 |         0.122 | N/A                                                          |
|    91 | C    |         0.24902 | False     |                          0.48445 |                 90.81 |         0     | N/A                                                          |
|    92 | H    |         0.24721 | False     |                          0.6066  |                 93.18 |         0     | N/A                                                          |
|    93 | D    |         0.20157 | False     |                          0.37795 |                 95.24 |         0     | N/A                                                          |
|    94 | S    |         0.23758 | False     |                          0.50428 |                 92.25 |         0     | N/A                                                          |
|    95 | F    |         0.38179 | False     |                          0.72348 |                 90.26 |         0     | N/A                                                          |
|    96 | L    |         0.23425 | False     |                          0.66824 |                 92.02 |         0     | N/A                                                          |
|    97 | K    |         0.31181 | False     |                          0.75702 |                 90.86 |         0     | N/A                                                          |
|    98 | A    |         0.2989  | False     |                          0.73531 |                 85.37 |         0     | N/A                                                          |
|    99 | V    |         0.24794 | False     |                          0.63874 |                 75.21 |         0     | N/A                                                          |
|   100 | P    |         0.26392 | False     |                          0.83731 |                 63.35 |         0     | N/A                                                          |
|   101 | S    |         0.31714 | False     |                          0.84144 |                 62.7  |         0     | N/A                                                          |
|   102 | Q    |         0.33399 | False     |                          0.81635 |                 57.85 |         0     | N/A                                                          |
|   103 | K    |         0.39995 | False     |                          0.91938 |                 49.22 |         0     | N/A                                                          |
|   104 | R    |         0.23321 | False     |                          0.98003 |                 52.96 |         0     | N/A                                                          |
|   105 | T    |         0.20515 | False     |                          1.27086 |                 47.84 |         0     | N/A                                                          |


# Detailed Data for P16035


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: P16035
- **Gene Name**: TIMP-2
- **Protein Name**: Metalloproteinase inhibitor 2
- **Swiss Prot**: TIMP2_HUMAN
- **Family**: other
- **Biomarker Application**: efficacy,prognosis,unspecified application
- **Number of Isoforms**: 0
- **Regulation**: 2
- **(transcriptomics) AUC**: nan
- **(transcriptomics) Fold Change**: nan
- **(transcriptomics) Regulation**: Downregulated
- **Discotope Epitope Count**: 51
- **Max n_uniprots (Homo)**: 1
- **Max n_uniprots (Hetero)**: 2


## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| TIMP2             | MMP14             |   0.999 |
| TIMP2             | MMP2              |   0.999 |
| TIMP2             | MMP9              |   0.998 |
| TIMP2             | MMP10             |   0.981 |
| TIMP2             | MMP3              |   0.967 |
| TIMP2             | MMP13             |   0.963 |
| TIMP2             | MMP7              |   0.951 |
| TIMP2             | HPX               |   0.94  |
| TIMP2             | MMP1              |   0.936 |
| TIMP2             | TIMP3             |   0.923 |
| TIMP2             | MMP16             |   0.913 |

## Homologs

| uniprot_id   | gene_id   |
|:-------------|:----------|
| P35625       | TIMP3     |
| Q99727       | TIMP4     |
| Q6FGX5       | TIMP1     |

## Biological Assemblies

|   Unnamed: 0 |   assembly |   n_uniprots | composition   | crystal_id   |
|-------------:|-----------:|-------------:|:--------------|:-------------|
|            0 |          1 |            1 | Homo          | 2tmp         |
|            0 |          1 |            2 | Hetero        | 4ilw         |
|            1 |          2 |            2 | Hetero        | 4ilw         |
|            0 |          1 |            2 | Hetero        | 1gxd         |
|            1 |          2 |            2 | Hetero        | 1gxd         |
|            0 |          1 |            1 | Homo          | 1br9         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification   |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:---------------|
|     1 | M    |         0.14145 | False     |                          1.27341 |                 50.9  |         0     | N/A            |
|     2 | G    |         0.2383  | False     |                          0.56496 |                 63.58 |         0     | N/A            |
|     3 | A    |         0.16302 | False     |                          0.73308 |                 70.99 |         0     | N/A            |
|     4 | A    |         0.15052 | False     |                          0.75783 |                 72.22 |         0     | N/A            |
|     5 | A    |         0.10325 | False     |                          0.53027 |                 73.05 |         0     | N/A            |
|     6 | R    |         0.14817 | False     |                          0.71472 |                 74.7  |         0     | N/A            |
|     7 | T    |         0.18479 | False     |                          0.58569 |                 77.39 |         0     | N/A            |
|     8 | L    |         0.14483 | False     |                          0.79433 |                 79.71 |         0     | N/A            |
|     9 | R    |         0.15856 | False     |                          0.75853 |                 81.93 |         0     | N/A            |
|    10 | L    |         0.17384 | False     |                          0.79611 |                 83.34 |        29.463 | N/A            |
|    11 | A    |         0.14035 | False     |                          0.56645 |                 83.72 |        34.854 | N/A            |
|    12 | L    |         0.22172 | False     |                          0.62475 |                 84.74 |        52.303 | N/A            |
|    13 | G    |         0.15774 | False     |                          0.42991 |                 82.59 |        55.433 | N/A            |
|    14 | L    |         0.18423 | False     |                          0.79023 |                 81.4  |        86.251 | N/A            |
|    15 | L    |         0.17099 | False     |                          0.69164 |                 82.15 |        91.264 | N/A            |
|    16 | L    |         0.15448 | False     |                          0.62794 |                 79.37 |        91.991 | N/A            |
|    17 | L    |         0.19684 | False     |                          0.64807 |                 75.04 |        91.062 | N/A            |
|    18 | A    |         0.19098 | False     |                          0.59932 |                 72.01 |        84.912 | N/A            |
|    19 | T    |         0.23104 | False     |                          0.71658 |                 71.41 |        76.377 | N/A            |
|    20 | L    |         0.21598 | False     |                          0.79636 |                 66.45 |        70.934 | N/A            |
|    21 | L    |         0.24425 | False     |                          0.81465 |                 59.67 |        59.975 | N/A            |
|    22 | R    |         0.20629 | False     |                          0.85049 |                 61.17 |         0     | N/A            |
|    23 | P    |         0.19032 | False     |                          0.92138 |                 59.72 |         0     | N/A            |
|    24 | A    |         0.16759 | False     |                          0.8689  |                 61.43 |         0     | N/A            |
|    25 | D    |         0.23276 | False     |                          0.67903 |                 60.87 |         0     | N/A            |
|    26 | A    |         0.31514 | True      |                          0.63485 |                 75.21 |         0     | N/A            |
|    27 | C    |         0.12557 | False     |                          0.16274 |                 87.65 |         0     | N/A            |
|    28 | S    |         0.3794  | True      |                          0.87315 |                 90.22 |         0     | N/A            |
|    29 | C    |         0.22168 | False     |                          0.35884 |                 92.71 |         0     | N/A            |
|    30 | S    |         0.30717 | True      |                          0.6908  |                 92.24 |         0     | N/A            |
|    31 | P    |         0.27396 | False     |                          0.28526 |                 93.54 |         0     | N/A            |
|    32 | V    |         0.12946 | False     |                          0.4305  |                 95.63 |         0     | N/A            |
|    33 | H    |         0.03486 | False     |                          0.01104 |                 97.54 |         0     | N/A            |
|    34 | P    |         0.05385 | False     |                          0.06107 |                 97.68 |         0     | N/A            |
|    35 | Q    |         0.01319 | False     |                          0.00644 |                 97.88 |         0     | N/A            |
|    36 | Q    |         0.15436 | False     |                          0.21839 |                 97.73 |         0     | N/A            |
|    37 | A    |         0.05678 | False     |                          0.12887 |                 97.87 |         0     | N/A            |
|    38 | F    |         0.0488  | False     |                          0.02499 |                 98.43 |         0     | N/A            |
|    39 | C    |         0.12373 | False     |                          0.16899 |                 97.97 |         0     | N/A            |
|    40 | N    |         0.16902 | False     |                          0.50829 |                 97.17 |         0     | N/A            |
|    41 | A    |         0.06374 | False     |                          0.06079 |                 98.3  |         0     | N/A            |
|    42 | D    |         0.14286 | False     |                          0.36768 |                 98    |         0     | N/A            |
|    43 | V    |         0.00401 | False     |                          0.0019  |                 98.47 |         0     | N/A            |
|    44 | V    |         0.00627 | False     |                          0.00571 |                 98.63 |         0     | N/A            |
|    45 | I    |         0.00943 | False     |                          0       |                 98.57 |         0     | N/A            |
|    46 | R    |         0.29249 | False     |                          0.23757 |                 98.5  |         0     | N/A            |
|    47 | A    |         0.00554 | False     |                          0       |                 98.4  |         0     | N/A            |
|    48 | K    |         0.16793 | False     |                          0.19757 |                 98.26 |         0     | N/A            |
|    49 | A    |         0.01142 | False     |                          0.00533 |                 98.21 |         0     | N/A            |
|    50 | V    |         0.16924 | False     |                          0.44826 |                 97.85 |         0     | N/A            |
|    51 | S    |         0.20041 | False     |                          0.37113 |                 97.7  |         0     | N/A            |
|    52 | E    |         0.24123 | False     |                          0.46868 |                 97.52 |         0     | N/A            |
|    53 | K    |         0.39392 | True      |                          0.56458 |                 97.31 |         0     | N/A            |
|    54 | E    |         0.42645 | True      |                          0.48497 |                 96.88 |         0     | N/A            |
|    55 | V    |         0.29779 | False     |                          0.23596 |                 96.53 |         0     | N/A            |
|    56 | D    |         0.48801 | True      |                          0.63083 |                 93.49 |         0     | N/A            |
|    57 | S    |         0.39183 | True      |                          0.38607 |                 88.95 |         0     | N/A            |
|    58 | G    |         0.4598  | True      |                          0.55495 |                 89.67 |         0     | N/A            |
|    59 | N    |         0.43568 | True      |                          0.63511 |                 90.12 |         0     | N/A            |
|    60 | D    |         0.45179 | True      |                          0.32444 |                 87.93 |         0     | N/A            |
|    61 | I    |         0.58222 | True      |                          1.02915 |                 88.91 |         0     | N/A            |
|    62 | Y    |         0.58685 | True      |                          0.86043 |                 91.18 |         0     | N/A            |
|    63 | G    |         0.43227 | True      |                          0.58302 |                 89.47 |         0     | N/A            |
|    64 | N    |         0.44582 | True      |                          0.50988 |                 89.99 |         0     | N/A            |
|    65 | P    |         0.40731 | True      |                          0.53931 |                 89.99 |         0     | N/A            |
|    66 | I    |         0.54024 | True      |                          0.47438 |                 91.34 |         0     | N/A            |
|    67 | K    |         0.36038 | True      |                          0.46019 |                 94.17 |         0     | N/A            |
|    68 | R    |         0.48608 | True      |                          0.19308 |                 96.9  |         0     | N/A            |
|    69 | I    |         0.34521 | True      |                          0.15599 |                 97.97 |         0     | N/A            |
|    70 | Q    |         0.15214 | False     |                          0.09018 |                 98.13 |         0     | N/A            |
|    71 | Y    |         0.07909 | False     |                          0.01759 |                 98.51 |         0     | N/A            |
|    72 | E    |         0.23235 | False     |                          0.4147  |                 98.13 |         0     | N/A            |
|    73 | I    |         0.14232 | False     |                          0.08118 |                 97.92 |         0     | N/A            |
|    74 | K    |         0.4495  | True      |                          0.64068 |                 97.74 |         0     | N/A            |
|    75 | Q    |         0.1232  | False     |                          0.18842 |                 98.1  |         0     | N/A            |
|    76 | I    |         0.20586 | False     |                          0.43081 |                 97.67 |         0     | N/A            |
|    77 | K    |         0.2175  | False     |                          0.44638 |                 97.82 |         0     | N/A            |
|    78 | M    |         0.18093 | False     |                          0.2499  |                 97.85 |         0     | N/A            |
|    79 | F    |         0.13205 | False     |                          0.15033 |                 97.83 |         0     | N/A            |
|    80 | K    |         0.11116 | False     |                          0.25268 |                 97.48 |         0     | N/A            |
|    81 | G    |         0.12342 | False     |                          0.45474 |                 96.22 |         0     | N/A            |
|    82 | P    |         0.17404 | False     |                          0.46942 |                 95.22 |         0     | N/A            |
|    83 | E    |         0.26689 | False     |                          0.97015 |                 94.41 |         0     | N/A            |
|    84 | K    |         0.23291 | False     |                          0.47189 |                 95.48 |         0     | N/A            |
|    85 | D    |         0.19991 | False     |                          0.5019  |                 97.24 |         0     | N/A            |
|    86 | I    |         0.04491 | False     |                          0.0208  |                 98.34 |         0     | N/A            |
|    87 | E    |         0.21058 | False     |                          0.39115 |                 97.72 |         0     | N/A            |
|    88 | F    |         0.31837 | True      |                          0.28536 |                 98.27 |         0     | N/A            |
|    89 | I    |         0.00419 | False     |                          0       |                 98.48 |         0     | N/A            |
|    90 | Y    |         0.24126 | False     |                          0.14735 |                 98.19 |         0     | N/A            |
|    91 | T    |         0.04107 | False     |                          0.01428 |                 98.03 |         0     | N/A            |
|    92 | A    |         0.23699 | False     |                          0.26357 |                 96.01 |         0     | N/A            |
|    93 | P    |         0.50368 | True      |                          0.46765 |                 94    |         0     | N/A            |
|    94 | S    |         0.57572 | True      |                          0.4064  |                 93.42 |         0     | N/A            |
|    95 | S    |         0.18385 | False     |                          0.42035 |                 93.21 |         0     | N/A            |
|    96 | A    |         0.23399 | False     |                          0.59943 |                 91.08 |         0.132 | N/A            |
|    97 | V    |         0.52229 | True      |                          0.6163  |                 92.23 |         0.132 | N/A            |
|    98 | C    |         0.2271  | False     |                          0.26347 |                 95.15 |         0.132 | N/A            |
|    99 | G    |         0.08017 | False     |                          0.04728 |                 96.39 |         0.132 | N/A            |
|   100 | V    |         0.09604 | False     |                          0.09563 |                 97.21 |         0.132 | N/A            |
|   101 | S    |         0.34336 | True      |                          0.83546 |                 96.39 |         0     | N/A            |
|   102 | L    |         0.05423 | False     |                          0.06137 |                 97.39 |         0     | N/A            |
|   103 | D    |         0.24512 | False     |                          0.45338 |                 97.34 |         0     | N/A            |
|   104 | V    |         0.26031 | False     |                          0.51344 |                 95.77 |         0     | N/A            |
|   105 | G    |         0.2045  | False     |                          0.61294 |                 93.47 |         0     | N/A            |
|   106 | G    |         0.25565 | False     |                          0.29755 |                 88.24 |         0     | N/A            |
|   107 | K    |         0.24267 | False     |                          0.89294 |                 92.81 |         0     | N/A            |
|   108 | K    |         0.217   | False     |                          0.39417 |                 97.42 |         0     | N/A            |
|   109 | E    |         0.19201 | False     |                          0.18667 |                 98.18 |         0     | N/A            |
|   110 | Y    |         0.11582 | False     |                          0.0588  |                 98.66 |         0.977 | N/A            |
|   111 | L    |         0.01299 | False     |                          0.00247 |                 98.6  |         0.977 | N/A            |
|   112 | I    |         0.00351 | False     |                          0.0024  |                 98.67 |         0.977 | N/A            |
|   113 | A    |         0.01651 | False     |                          0.01786 |                 98.52 |         0.977 | N/A            |
|   114 | G    |         0.00457 | False     |                          0       |                 98.27 |         0.977 | N/A            |
|   115 | K    |         0.1209  | False     |                          0.37144 |                 98.3  |         0     | N/A            |
|   116 | A    |         0.1768  | False     |                          0.44419 |                 97.81 |         0     | N/A            |
|   117 | E    |         0.51006 | True      |                          0.38049 |                 95.64 |         0     | N/A            |
|   118 | G    |         0.24853 | False     |                          0.4646  |                 93.6  |         0     | N/A            |
|   119 | D    |         0.31319 | True      |                          0.60287 |                 93.16 |         0     | N/A            |
|   120 | G    |         0.0603  | False     |                          0.04405 |                 96.59 |         0     | N/A            |
|   121 | K    |         0.35124 | True      |                          0.33574 |                 97.78 |         0     | N/A            |
|   122 | M    |         0.00785 | False     |                          0       |                 98.3  |         0.299 | N/A            |
|   123 | H    |         0.34139 | True      |                          0.30015 |                 98.1  |         0.569 | N/A            |
|   124 | I    |         0.05391 | False     |                          0.01005 |                 98.4  |         0.569 | N/A            |
|   125 | T    |         0.20807 | False     |                          0.32833 |                 97.48 |         0.569 | N/A            |
|   126 | L    |         0.15    | False     |                          0.4276  |                 96.15 |         0.569 | N/A            |
|   127 | C    |         0.17898 | False     |                          0.48359 |                 95.75 |         0.569 | N/A            |
|   128 | D    |         0.08725 | False     |                          0.23579 |                 97.83 |         0     | N/A            |
|   129 | F    |         0.11536 | False     |                          0.19794 |                 97.13 |         0     | N/A            |
|   130 | I    |         0.28832 | False     |                          0.20474 |                 97.92 |         0     | N/A            |
|   131 | V    |         0.2666  | False     |                          0.24183 |                 97.27 |         0     | N/A            |
|   132 | P    |         0.23353 | False     |                          0.32208 |                 97.84 |         0     | N/A            |
|   133 | W    |         0.10395 | False     |                          0.12886 |                 98.08 |         0     | N/A            |
|   134 | D    |         0.25488 | False     |                          0.76042 |                 96.82 |         0     | N/A            |
|   135 | T    |         0.3185  | True      |                          0.64926 |                 96.44 |         0     | N/A            |
|   136 | L    |         0.12053 | False     |                          0.0796  |                 97.06 |         0     | N/A            |
|   137 | S    |         0.22545 | False     |                          0.14263 |                 95.56 |         0     | N/A            |
|   138 | T    |         0.18075 | False     |                          0.63377 |                 94.15 |         0     | N/A            |
|   139 | T    |         0.10209 | False     |                          0.06167 |                 93.89 |         0     | N/A            |
|   140 | Q    |         0.04596 | False     |                          0.03924 |                 96.61 |         0     | N/A            |
|   141 | K    |         0.31006 | True      |                          0.25801 |                 96.23 |         0     | N/A            |
|   142 | K    |         0.33515 | True      |                          0.49829 |                 93.9  |         0     | N/A            |
|   143 | S    |         0.00767 | False     |                          0.00472 |                 95.85 |         0     | N/A            |
|   144 | L    |         0.02971 | False     |                          0.01642 |                 96.8  |         0     | N/A            |
|   145 | N    |         0.2527  | False     |                          0.35505 |                 93.64 |         0     | N/A            |
|   146 | H    |         0.38052 | True      |                          0.70084 |                 87.65 |         0     | N/A            |
|   147 | R    |         0.12436 | False     |                          0.05359 |                 90.64 |         0     | N/A            |
|   148 | Y    |         0.01439 | False     |                          0.01387 |                 96.49 |         0     | N/A            |
|   149 | Q    |         0.17432 | False     |                          0.50964 |                 95.31 |         0     | N/A            |
|   150 | M    |         0.39175 | True      |                          0.45924 |                 92.91 |         0     | N/A            |
|   151 | G    |         0.01796 | False     |                          0.00833 |                 95.57 |         0     | N/A            |
|   152 | C    |         0.12614 | False     |                          0.28552 |                 97.21 |         0     | N/A            |
|   153 | E    |         0.17146 | False     |                          0.65807 |                 96.35 |         0     | N/A            |
|   154 | C    |         0.06284 | False     |                          0.04483 |                 97.54 |         0     | N/A            |
|   155 | K    |         0.11953 | False     |                          0.53492 |                 97.29 |         0     | N/A            |
|   156 | I    |         0.09025 | False     |                          0.11722 |                 97.88 |         0     | N/A            |
|   157 | T    |         0.12599 | False     |                          0.24087 |                 96.42 |         0     | N/A            |
|   158 | R    |         0.21822 | False     |                          0.29582 |                 95.56 |         0     | N/A            |
|   159 | C    |         0.00687 | False     |                          0.001   |                 95.56 |         0     | N/A            |
|   160 | P    |         0.25476 | False     |                          0.64788 |                 92.56 |         0     | N/A            |
|   161 | M    |         0.32685 | True      |                          0.78256 |                 94.34 |         0     | N/A            |
|   162 | I    |         0.5684  | True      |                          0.71918 |                 92.82 |         0     | N/A            |
|   163 | P    |         0.57267 | True      |                          0.93373 |                 94.53 |         0     | N/A            |
|   164 | C    |         0.21791 | False     |                          0.25483 |                 94.75 |         0     | N/A            |
|   165 | Y    |         0.49832 | True      |                          0.79198 |                 93.83 |         0     | N/A            |
|   166 | I    |         0.42158 | True      |                          0.46833 |                 93.63 |         0     | N/A            |
|   167 | S    |         0.21573 | False     |                          0.71239 |                 93.96 |         0     | N/A            |
|   168 | S    |         0.16719 | False     |                          0.3197  |                 95.53 |         0     | N/A            |
|   169 | P    |         0.26581 | False     |                          0.67548 |                 94.82 |         0     | N/A            |
|   170 | D    |         0.19968 | False     |                          0.34087 |                 95.75 |         0     | N/A            |
|   171 | E    |         0.04384 | False     |                          0.03863 |                 97.33 |         0     | N/A            |
|   172 | C    |         0.03192 | False     |                          0.02671 |                 97.84 |         0     | N/A            |
|   173 | L    |         0.18642 | False     |                          0.2163  |                 96.68 |         0     | N/A            |
|   174 | W    |         0.06893 | False     |                          0.02158 |                 97.33 |         0     | N/A            |
|   175 | M    |         0.34485 | True      |                          0.25097 |                 95.45 |         0     | N/A            |
|   176 | D    |         0.07599 | False     |                          0.01113 |                 96.42 |         0     | N/A            |
|   177 | W    |         0.36884 | True      |                          0.46099 |                 95.13 |         0     | N/A            |
|   178 | V    |         0.35937 | True      |                          0.31381 |                 95    |         0     | N/A            |
|   179 | T    |         0.43858 | True      |                          0.66336 |                 92.9  |         0     | N/A            |
|   180 | E    |         0.48197 | True      |                          0.44172 |                 93.81 |         0     | N/A            |
|   181 | K    |         0.41384 | True      |                          0.85077 |                 92.72 |         0     | N/A            |
|   182 | N    |         0.45111 | True      |                          0.42465 |                 92.51 |         0     | N/A            |
|   183 | I    |         0.33848 | True      |                          0.44758 |                 91.89 |         0     | N/A            |
|   184 | N    |         0.24878 | False     |                          0.43205 |                 92.37 |         0     | N/A            |
|   185 | G    |         0.07041 | False     |                          0.01694 |                 94.23 |         0     | N/A            |
|   186 | H    |         0.47481 | True      |                          0.52032 |                 94.44 |         0     | N/A            |
|   187 | Q    |         0.14485 | False     |                          0.11301 |                 95.78 |         0     | N/A            |
|   188 | A    |         0.01059 | False     |                          0.00444 |                 96.64 |         0     | N/A            |
|   189 | K    |         0.17365 | False     |                          0.3276  |                 95.69 |         0     | N/A            |
|   190 | F    |         0.29288 | False     |                          0.38555 |                 96.15 |         0.831 | N/A            |
|   191 | F    |         0.25165 | False     |                          0.10972 |                 96.14 |         0.831 | N/A            |
|   192 | A    |         0.01592 | False     |                          0.01441 |                 96.58 |         0.831 | N/A            |
|   193 | C    |         0.00335 | False     |                          0       |                 97.01 |         0.831 | N/A            |
|   194 | I    |         0.00889 | False     |                          0.0048  |                 95.48 |         0.831 | N/A            |
|   195 | K    |         0.07865 | False     |                          0.38738 |                 94.74 |         0     | N/A            |
|   196 | R    |         0.21623 | False     |                          0.068   |                 92.37 |         0     | N/A            |
|   197 | S    |         0.28196 | False     |                          0.67617 |                 90.81 |         0     | N/A            |
|   198 | D    |         0.26439 | False     |                          0.45046 |                 91.4  |         0     | N/A            |
|   199 | G    |         0.0903  | False     |                          0.33331 |                 91.11 |         0     | N/A            |
|   200 | S    |         0.10513 | False     |                          0.07271 |                 95.17 |         0.224 | N/A            |
|   201 | C    |         0.075   | False     |                          0.08922 |                 96.4  |         0.224 | N/A            |
|   202 | A    |         0.25053 | False     |                          0.27932 |                 95.11 |         0.224 | N/A            |
|   203 | W    |         0.12853 | False     |                          0.19357 |                 95.14 |         0.224 | N/A            |
|   204 | Y    |         0.24668 | False     |                          0.10656 |                 92.56 |         0.224 | N/A            |
|   205 | R    |         0.44725 | True      |                          0.69883 |                 89.43 |         0     | N/A            |
|   206 | G    |         0.2558  | False     |                          0.29268 |                 81.61 |         0     | N/A            |
|   207 | A    |         0.27114 | False     |                          0.31533 |                 73.55 |         0     | N/A            |
|   208 | A    |         0.27062 | False     |                          0.57984 |                 75.54 |         0     | N/A            |
|   209 | P    |         0.27949 | False     |                          0.774   |                 72.18 |         0     | N/A            |
|   210 | P    |         0.29517 | False     |                          0.16161 |                 72.42 |         0     | N/A            |
|   211 | K    |         0.39617 | True      |                          0.71319 |                 80.81 |         0     | N/A            |
|   212 | Q    |         0.30159 | False     |                          0.59126 |                 74.01 |         0     | N/A            |
|   213 | E    |         0.20179 | False     |                          0.65475 |                 77.4  |         0     | N/A            |
|   214 | F    |         0.48981 | True      |                          0.212   |                 77.19 |         0     | N/A            |
|   215 | L    |         0.24966 | False     |                          0.28007 |                 76.33 |         0     | N/A            |
|   216 | D    |         0.20261 | False     |                          0.40265 |                 77.78 |         0     | N/A            |
|   217 | I    |         0.25476 | False     |                          0.59639 |                 75.71 |         0     | N/A            |
|   218 | E    |         0.15657 | False     |                          0.71475 |                 61.49 |         0     | N/A            |
|   219 | D    |         0.17685 | False     |                          0.68416 |                 59.6  |         0     | N/A            |
|   220 | P    |         0.14428 | False     |                          1.36436 |                 50.31 |         0     | N/A            |


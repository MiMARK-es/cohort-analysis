# Detailed Data for P08833


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: P08833
- **Gene Name**: IGFBP-I
- **Protein Name**: Insulin-like growth factor-binding protein 1
- **Swiss Prot**: IBP1_HUMAN
- **Family**: other
- **Biomarker Application**: diagnosis,efficacy
- **Number of Isoforms**: 0
- **Regulation**: 1
- **(transcriptomics) AUC**: nan
- **(transcriptomics) Fold Change**: nan
- **(transcriptomics) Regulation**: Downregulated
- **Discotope Epitope Count**: 33
- **Max n_uniprots (Homo)**: 1
- **Max n_uniprots (Hetero)**: 3


## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| IGFBP1            | IGF2              |   0.999 |
| IGFBP1            | IGF1              |   0.999 |
| IGFBP1            | INS               |   0.994 |
| IGFBP1            | IGFBP4            |   0.972 |
| IGFBP1            | IGFBP6            |   0.956 |

## Homologs

| uniprot_id   | gene_id   |
|:-------------|:----------|
| P22692       | IGFBP4    |
| P24593       | IGFBP5    |
| H7C1H0       | IGFBP2    |
| B3KWK7       | IGFBP3    |
| F8VYK9       | IGFBP6    |

## Biological Assemblies

|   Unnamed: 0 |   assembly |   n_uniprots | composition   | crystal_id   |
|-------------:|-----------:|-------------:|:--------------|:-------------|
|            0 |          1 |            1 | Homo          | 1zt3         |
|            0 |          1 |            1 | Homo          | 1zt5         |
|            0 |          1 |            3 | Hetero        | 2dsq         |
|            1 |          2 |            3 | Hetero        | 2dsq         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification                |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:----------------------------|
|     1 | M    |         0.1509  | False     |                          1.33978 |                 46.15 |         0     | N/A                         |
|     2 | S    |         0.16928 | False     |                          0.81617 |                 50.85 |         0     | N/A                         |
|     3 | E    |         0.19939 | False     |                          0.92004 |                 59.75 |         0     | N/A                         |
|     4 | V    |         0.20123 | False     |                          0.81667 |                 59.94 |         0     | N/A                         |
|     5 | P    |         0.15868 | False     |                          0.5728  |                 62.28 |         0     | N/A                         |
|     6 | V    |         0.1273  | False     |                          0.77693 |                 65.61 |         0     | N/A                         |
|     7 | A    |         0.09403 | False     |                          0.6385  |                 61.25 |         0     | N/A                         |
|     8 | R    |         0.16132 | False     |                          0.70567 |                 62.6  |         0     | N/A                         |
|     9 | V    |         0.08482 | False     |                          0.61694 |                 67.72 |        86.762 | N/A                         |
|    10 | W    |         0.20188 | False     |                          0.74953 |                 66.79 |        94.131 | N/A                         |
|    11 | L    |         0.12542 | False     |                          0.68634 |                 65.02 |        99.019 | N/A                         |
|    12 | V    |         0.07629 | False     |                          0.60146 |                 64.77 |        99.906 | N/A                         |
|    13 | L    |         0.14793 | False     |                          0.65359 |                 65.02 |        99.978 | N/A                         |
|    14 | L    |         0.12422 | False     |                          0.68309 |                 64.38 |        99.964 | N/A                         |
|    15 | L    |         0.13584 | False     |                          0.75714 |                 63.13 |        99.807 | N/A                         |
|    16 | L    |         0.12249 | False     |                          0.73329 |                 62.62 |        98.898 | N/A                         |
|    17 | T    |         0.15184 | False     |                          0.66764 |                 61.12 |        93.889 | N/A                         |
|    18 | V    |         0.17965 | False     |                          0.86809 |                 59.53 |        90.907 | N/A                         |
|    19 | Q    |         0.16704 | False     |                          0.77439 |                 61.08 |        55.794 | N/A                         |
|    20 | V    |         0.16091 | False     |                          0.87157 |                 61.2  |        54.419 | N/A                         |
|    21 | G    |         0.16305 | False     |                          0.72271 |                 52.44 |        38.229 | N/A                         |
|    22 | V    |         0.13345 | False     |                          0.91288 |                 57.21 |        36.772 | N/A                         |
|    23 | T    |         0.14092 | False     |                          0.91824 |                 55.84 |        19.62  | N/A                         |
|    24 | A    |         0.1204  | False     |                          0.84914 |                 59.43 |         9.413 | N/A                         |
|    25 | G    |         0.14607 | False     |                          0.8391  |                 55.42 |         0.782 | N/A                         |
|    26 | A    |         0.12675 | False     |                          0.80319 |                 63.77 |         0.005 | N/A                         |
|    27 | P    |         0.14518 | False     |                          0.74461 |                 80.79 |         0.001 | N/A                         |
|    28 | W    |         0.17204 | False     |                          0.91949 |                 82.74 |         0     | N/A                         |
|    29 | Q    |         0.20138 | False     |                          0.73617 |                 89.49 |         0     | N/A                         |
|    30 | C    |         0.24189 | False     |                          0.44534 |                 92.17 |         0     | N/A                         |
|    31 | A    |         0.13341 | False     |                          0.72442 |                 91.01 |         0     | N/A                         |
|    32 | P    |         0.19784 | False     |                          0.95367 |                 93.52 |         0     | N/A                         |
|    33 | C    |         0.16978 | False     |                          0.24848 |                 93.28 |         0     | N/A                         |
|    34 | S    |         0.13529 | False     |                          0.4809  |                 93.91 |         0     | N/A                         |
|    35 | A    |         0.1347  | False     |                          0.79759 |                 95.09 |         0     | N/A                         |
|    36 | E    |         0.14924 | False     |                          0.70483 |                 93.53 |         0     | N/A                         |
|    37 | K    |         0.29574 | True      |                          0.56184 |                 91.19 |         0     | N/A                         |
|    38 | L    |         0.21    | False     |                          0.49197 |                 93.5  |         0     | N/A                         |
|    39 | A    |         0.21098 | False     |                          0.83513 |                 93.99 |         0     | N/A                         |
|    40 | L    |         0.29475 | True      |                          0.89859 |                 94.9  |         0     | N/A                         |
|    41 | C    |         0.23065 | False     |                          0.17152 |                 94.31 |         0     | N/A                         |
|    42 | P    |         0.17712 | False     |                          0.67307 |                 93.27 |         0     | N/A                         |
|    43 | P    |         0.18938 | False     |                          0.9617  |                 91.64 |         0     | N/A                         |
|    44 | V    |         0.11592 | False     |                          0.32443 |                 92.15 |         0     | N/A                         |
|    45 | S    |         0.20518 | False     |                          0.5175  |                 91.54 |         0     | Phosphoserine; by FAM20C    |
|    46 | A    |         0.1773  | False     |                          1.10705 |                 91.21 |         0     | N/A                         |
|    47 | S    |         0.20692 | False     |                          0.80927 |                 92.9  |         0     | N/A                         |
|    48 | C    |         0.14342 | False     |                          0.17974 |                 94.43 |         0     | N/A                         |
|    49 | S    |         0.1628  | False     |                          0.89217 |                 92.88 |         0     | N/A                         |
|    50 | E    |         0.15325 | False     |                          0.14132 |                 95.79 |         0     | N/A                         |
|    51 | V    |         0.1373  | False     |                          0.61183 |                 94.7  |         0     | N/A                         |
|    52 | T    |         0.09396 | False     |                          0.16662 |                 92.92 |         0     | N/A                         |
|    53 | R    |         0.21848 | False     |                          0.4221  |                 89.72 |         0     | N/A                         |
|    54 | S    |         0.0972  | False     |                          0.0674  |                 90.33 |         0     | N/A                         |
|    55 | A    |         0.11917 | False     |                          0.23968 |                 88.39 |         0     | N/A                         |
|    56 | G    |         0.19454 | False     |                          0.6022  |                 89.72 |         0     | N/A                         |
|    57 | C    |         0.25867 | True      |                          0.53405 |                 93.01 |         0     | N/A                         |
|    58 | G    |         0.15076 | False     |                          0.33372 |                 90.63 |         0     | N/A                         |
|    59 | C    |         0.11411 | False     |                          0.10631 |                 93.72 |         0     | N/A                         |
|    60 | C    |         0.14035 | False     |                          0.25326 |                 94.4  |         0     | N/A                         |
|    61 | P    |         0.13623 | False     |                          0.36326 |                 93.68 |         0     | N/A                         |
|    62 | M    |         0.12269 | False     |                          0.44468 |                 94.34 |         0     | N/A                         |
|    63 | C    |         0.08455 | False     |                          0.34614 |                 95.83 |         0     | N/A                         |
|    64 | A    |         0.07226 | False     |                          0.11075 |                 96.79 |         0     | N/A                         |
|    65 | L    |         0.13748 | False     |                          0.21681 |                 96.39 |         0     | N/A                         |
|    66 | P    |         0.13514 | False     |                          0.63124 |                 96.11 |         0     | N/A                         |
|    67 | L    |         0.23975 | False     |                          0.6598  |                 96.74 |         0     | N/A                         |
|    68 | G    |         0.10535 | False     |                          0.65632 |                 96.39 |         0     | N/A                         |
|    69 | A    |         0.09495 | False     |                          0.23579 |                 97.17 |         0     | N/A                         |
|    70 | A    |         0.13793 | False     |                          0.6707  |                 97.29 |         0     | N/A                         |
|    71 | C    |         0.01188 | False     |                          0.00501 |                 97.68 |         0     | N/A                         |
|    72 | G    |         0.09681 | False     |                          0.14473 |                 96.22 |         0     | N/A                         |
|    73 | V    |         0.23324 | False     |                          0.72438 |                 95.29 |         0     | N/A                         |
|    74 | A    |         0.15497 | False     |                          0.82911 |                 92.31 |         0     | N/A                         |
|    75 | T    |         0.18834 | False     |                          0.28323 |                 94.38 |         0     | N/A                         |
|    76 | A    |         0.05866 | False     |                          0.19987 |                 94.76 |         0     | N/A                         |
|    77 | R    |         0.0964  | False     |                          0.48527 |                 95.69 |         0     | N/A                         |
|    78 | C    |         0.10545 | False     |                          0.12544 |                 96.5  |         0     | N/A                         |
|    79 | A    |         0.08794 | False     |                          0.20462 |                 96.03 |         0     | N/A                         |
|    80 | R    |         0.26845 | True      |                          0.82021 |                 95.38 |         0     | N/A                         |
|    81 | G    |         0.13187 | False     |                          0.55635 |                 95.46 |         0     | N/A                         |
|    82 | L    |         0.11199 | False     |                          0.18796 |                 96.63 |         0     | N/A                         |
|    83 | S    |         0.11796 | False     |                          0.28449 |                 96.26 |         0     | N/A                         |
|    84 | C    |         0.09038 | False     |                          0.31426 |                 97.12 |         0     | N/A                         |
|    85 | R    |         0.22872 | False     |                          0.25022 |                 97.31 |         0     | N/A                         |
|    86 | A    |         0.08371 | False     |                          0.2283  |                 96.67 |         0     | N/A                         |
|    87 | L    |         0.18477 | False     |                          0.61509 |                 94.46 |         0     | N/A                         |
|    88 | P    |         0.20268 | False     |                          0.99869 |                 92.81 |         0     | N/A                         |
|    89 | G    |         0.19643 | False     |                          0.80043 |                 92.57 |         0     | N/A                         |
|    90 | E    |         0.20871 | False     |                          0.35077 |                 93    |         0     | N/A                         |
|    91 | Q    |         0.30913 | True      |                          0.80588 |                 94.07 |         0     | N/A                         |
|    92 | Q    |         0.42841 | True      |                          0.56855 |                 92.68 |         0     | N/A                         |
|    93 | P    |         0.18922 | False     |                          0.4861  |                 95.05 |         0     | N/A                         |
|    94 | L    |         0.2448  | False     |                          0.88042 |                 96.41 |         0     | N/A                         |
|    95 | H    |         0.20766 | False     |                          0.49029 |                 94.08 |         0     | N/A                         |
|    96 | A    |         0.04639 | False     |                          0.02078 |                 94    |         0     | N/A                         |
|    97 | L    |         0.20507 | False     |                          0.20774 |                 96.39 |         0     | N/A                         |
|    98 | T    |         0.21481 | False     |                          0.58147 |                 95.83 |         0     | N/A                         |
|    99 | R    |         0.22733 | False     |                          0.61404 |                 94.49 |         0     | N/A                         |
|   100 | G    |         0.09285 | False     |                          0.20558 |                 95.79 |         0     | N/A                         |
|   101 | Q    |         0.13479 | False     |                          0.41434 |                 97    |         0     | N/A                         |
|   102 | G    |         0.05085 | False     |                          0.03688 |                 96.71 |         0     | N/A                         |
|   103 | A    |         0.15332 | False     |                          0.12372 |                 97.84 |         0     | N/A                         |
|   104 | C    |         0.01203 | False     |                          0.00074 |                 97.64 |         0     | N/A                         |
|   105 | V    |         0.11454 | False     |                          0.28467 |                 97.36 |         0     | N/A                         |
|   106 | Q    |         0.15714 | False     |                          0.45131 |                 95.66 |         0     | N/A                         |
|   107 | E    |         0.30586 | True      |                          0.54328 |                 82.05 |         0     | N/A                         |
|   108 | S    |         0.20221 | False     |                          0.68327 |                 71.87 |         0     | N/A                         |
|   109 | D    |         0.27094 | True      |                          0.61509 |                 58.61 |         0     | N/A                         |
|   110 | A    |         0.39689 | True      |                          0.605   |                 51.98 |         0     | N/A                         |
|   111 | S    |         0.2716  | True      |                          0.73277 |                 43.87 |         0     | N/A                         |
|   112 | A    |         0.24014 | False     |                          0.79735 |                 38.69 |         0     | N/A                         |
|   113 | P    |         0.24211 | False     |                          0.85382 |                 41.18 |         0     | N/A                         |
|   114 | H    |         0.28956 | True      |                          0.98617 |                 42.11 |         0     | N/A                         |
|   115 | A    |         0.26778 | True      |                          0.92003 |                 34.48 |         0     | N/A                         |
|   116 | A    |         0.2831  | True      |                          0.75468 |                 40.14 |         0     | N/A                         |
|   117 | E    |         0.20063 | False     |                          0.92479 |                 36.03 |         0     | N/A                         |
|   118 | A    |         0.24906 | False     |                          0.96969 |                 39.72 |         0     | N/A                         |
|   119 | G    |         0.18089 | False     |                          0.86628 |                 34.11 |         0     | N/A                         |
|   120 | S    |         0.15776 | False     |                          0.90741 |                 30.35 |         0     | Phosphoserine               |
|   121 | P    |         0.30103 | True      |                          0.83476 |                 42.55 |         0     | N/A                         |
|   122 | E    |         0.18313 | False     |                          0.83505 |                 37.64 |         0     | N/A                         |
|   123 | S    |         0.16867 | False     |                          0.84076 |                 32.39 |         0     | Phosphoserine               |
|   124 | P    |         0.22221 | False     |                          0.82015 |                 39.7  |         0     | N/A                         |
|   125 | E    |         0.23467 | False     |                          0.77251 |                 38.63 |         0     | N/A                         |
|   126 | S    |         0.13085 | False     |                          0.83633 |                 35.83 |         0     | Phosphoserine               |
|   127 | T    |         0.2759  | True      |                          0.91052 |                 49.72 |         0     | N/A                         |
|   128 | E    |         0.17542 | False     |                          0.87761 |                 50.39 |         0     | N/A                         |
|   129 | I    |         0.20057 | False     |                          0.72405 |                 53.19 |         0     | N/A                         |
|   130 | T    |         0.1315  | False     |                          0.59265 |                 66.86 |         0     | N/A                         |
|   131 | E    |         0.12562 | False     |                          0.78682 |                 57.7  |         0     | N/A                         |
|   132 | E    |         0.1353  | False     |                          0.75528 |                 56.56 |         0     | N/A                         |
|   133 | E    |         0.11382 | False     |                          0.52642 |                 53.26 |         0     | N/A                         |
|   134 | L    |         0.08497 | False     |                          0.60278 |                 53.88 |         0     | N/A                         |
|   135 | L    |         0.12885 | False     |                          0.73979 |                 53.92 |         0     | N/A                         |
|   136 | D    |         0.14384 | False     |                          0.62088 |                 46.59 |         0     | N/A                         |
|   137 | N    |         0.16814 | False     |                          0.53826 |                 49.66 |         0     | N/A                         |
|   138 | F    |         0.13534 | False     |                          0.7342  |                 48.49 |         0     | N/A                         |
|   139 | H    |         0.18793 | False     |                          0.82111 |                 50.03 |         0     | N/A                         |
|   140 | L    |         0.25283 | True      |                          0.89744 |                 49.06 |         0     | N/A                         |
|   141 | M    |         0.17362 | False     |                          0.84385 |                 42.55 |         0     | N/A                         |
|   142 | A    |         0.11353 | False     |                          0.77601 |                 48.7  |         0     | N/A                         |
|   143 | P    |         0.13444 | False     |                          0.90198 |                 44.8  |         0     | N/A                         |
|   144 | S    |         0.09734 | False     |                          0.57688 |                 43.53 |         0     | Phosphoserine               |
|   145 | E    |         0.14433 | False     |                          0.86759 |                 52.07 |         0     | N/A                         |
|   146 | E    |         0.07646 | False     |                          0.4132  |                 50.77 |         0     | N/A                         |
|   147 | D    |         0.11655 | False     |                          0.9412  |                 51.28 |         0     | N/A                         |
|   148 | H    |         0.12227 | False     |                          0.51016 |                 57.29 |         0     | N/A                         |
|   149 | S    |         0.07478 | False     |                          0.27108 |                 72.89 |         0     | N/A                         |
|   150 | I    |         0.07506 | False     |                          0.62557 |                 80.03 |         0     | N/A                         |
|   151 | L    |         0.01755 | False     |                          0.01319 |                 82.22 |         0     | N/A                         |
|   152 | W    |         0.1404  | False     |                          0.40447 |                 81.8  |         0     | N/A                         |
|   153 | D    |         0.05776 | False     |                          0.39378 |                 83.42 |         0     | N/A                         |
|   154 | A    |         0.05891 | False     |                          0.18427 |                 81.93 |         0     | N/A                         |
|   155 | I    |         0.12377 | False     |                          0.12239 |                 84.18 |         0     | N/A                         |
|   156 | S    |         0.06224 | False     |                          0.45089 |                 83.87 |         0     | Phosphoserine; by FAM20C    |
|   157 | T    |         0.09302 | False     |                          0.66519 |                 82.55 |         0     | Phosphothreonine; by FAM20C |
|   158 | Y    |         0.10306 | False     |                          0.03998 |                 79.81 |         0     | Phosphotyrosine             |
|   159 | D    |         0.23236 | False     |                          0.53202 |                 82.87 |         0     | N/A                         |
|   160 | G    |         0.15064 | False     |                          0.91234 |                 80.46 |         0     | N/A                         |
|   161 | S    |         0.1047  | False     |                          0.20471 |                 77.49 |         0     | N/A                         |
|   162 | K    |         0.28753 | True      |                          0.37868 |                 79.39 |         0     | N/A                         |
|   163 | A    |         0.17228 | False     |                          0.84533 |                 71.33 |         0     | N/A                         |
|   164 | L    |         0.20816 | False     |                          0.78147 |                 70.27 |         0     | N/A                         |
|   165 | H    |         0.12506 | False     |                          0.16099 |                 67.78 |         0     | N/A                         |
|   166 | V    |         0.23111 | False     |                          0.58106 |                 69.97 |         0     | N/A                         |
|   167 | T    |         0.19103 | False     |                          0.73139 |                 70.81 |         0     | N/A                         |
|   168 | N    |         0.19925 | False     |                          0.33121 |                 72.28 |         0     | N/A                         |
|   169 | I    |         0.22472 | False     |                          0.18389 |                 70.34 |         0     | N/A                         |
|   170 | K    |         0.23738 | False     |                          0.99335 |                 69.37 |         0     | N/A                         |
|   171 | K    |         0.34762 | True      |                          0.82046 |                 74.86 |         0     | N/A                         |
|   172 | W    |         0.2665  | True      |                          0.25977 |                 73.42 |         0     | N/A                         |
|   173 | K    |         0.28864 | True      |                          0.89896 |                 83.45 |         0     | N/A                         |
|   174 | E    |         0.25759 | True      |                          0.19432 |                 89.34 |         0     | N/A                         |
|   175 | P    |         0.12673 | False     |                          0.30583 |                 93.76 |         0     | N/A                         |
|   176 | C    |         0.00608 | False     |                          0       |                 95.68 |         0     | N/A                         |
|   177 | R    |         0.20823 | False     |                          0.31336 |                 91.92 |         0     | N/A                         |
|   178 | I    |         0.13546 | False     |                          0.15679 |                 91.21 |         3.553 | N/A                         |
|   179 | E    |         0.17626 | False     |                          0.29607 |                 94.05 |         3.874 | N/A                         |
|   180 | L    |         0.1473  | False     |                          0.30913 |                 93.57 |         4.276 | N/A                         |
|   181 | Y    |         0.09683 | False     |                          0.15201 |                 90.59 |         4.276 | N/A                         |
|   182 | R    |         0.17357 | False     |                          0.59296 |                 91.86 |         4.276 | N/A                         |
|   183 | V    |         0.09985 | False     |                          0.21778 |                 93.02 |         4.276 | N/A                         |
|   184 | V    |         0.0448  | False     |                          0.05046 |                 91.58 |         3.993 | N/A                         |
|   185 | E    |         0.11473 | False     |                          0.38321 |                 89.76 |         0.402 | N/A                         |
|   186 | S    |         0.08069 | False     |                          0.54059 |                 90.25 |         0.402 | N/A                         |
|   187 | L    |         0.0785  | False     |                          0.12036 |                 90.47 |         0.402 | N/A                         |
|   188 | A    |         0.10427 | False     |                          0.13569 |                 87.13 |         0.184 | N/A                         |
|   189 | K    |         0.1388  | False     |                          0.69967 |                 87.85 |         0     | N/A                         |
|   190 | A    |         0.05252 | False     |                          0.34127 |                 86.57 |         0     | N/A                         |
|   191 | Q    |         0.15274 | False     |                          0.42648 |                 82.15 |         0     | N/A                         |
|   192 | E    |         0.20122 | False     |                          0.79718 |                 81.2  |         0     | N/A                         |
|   193 | T    |         0.1337  | False     |                          0.78275 |                 76.64 |         0     | Phosphothreonine; by FAM20C |
|   194 | S    |         0.09128 | False     |                          0.32786 |                 62.2  |         0     | Phosphoserine; by FAM20C    |
|   195 | G    |         0.13587 | False     |                          1.11276 |                 61.49 |         0     | N/A                         |
|   196 | E    |         0.14995 | False     |                          0.69927 |                 65.33 |         0     | N/A                         |
|   197 | E    |         0.23244 | False     |                          0.83694 |                 69.05 |         0     | N/A                         |
|   198 | I    |         0.10694 | False     |                          0.181   |                 78.78 |         0     | N/A                         |
|   199 | S    |         0.19754 | False     |                          0.34398 |                 82.89 |         0     | Phosphoserine; by FAM20C    |
|   200 | K    |         0.10215 | False     |                          0.41686 |                 87.46 |         0     | N/A                         |
|   201 | F    |         0.06066 | False     |                          0.05421 |                 91.32 |         0     | N/A                         |
|   202 | Y    |         0.25026 | False     |                          0.26316 |                 93.42 |         0     | N/A                         |
|   203 | L    |         0.02905 | False     |                          0.1795  |                 94.68 |         0     | N/A                         |
|   204 | P    |         0.05327 | False     |                          0.03307 |                 95.92 |         0     | N/A                         |
|   205 | N    |         0.1213  | False     |                          0.40726 |                 95.31 |         0     | N/A                         |
|   206 | C    |         0.16638 | False     |                          0.2479  |                 95.21 |         0     | N/A                         |
|   207 | N    |         0.20952 | False     |                          0.26001 |                 92.28 |         0     | N/A                         |
|   208 | K    |         0.24145 | False     |                          0.92284 |                 90.9  |         0     | N/A                         |
|   209 | N    |         0.21228 | False     |                          0.56181 |                 89.02 |         0     | N/A                         |
|   210 | G    |         0.02341 | False     |                          0.01127 |                 91.09 |         0     | N/A                         |
|   211 | F    |         0.13994 | False     |                          0.35557 |                 94.46 |         0     | N/A                         |
|   212 | Y    |         0.08432 | False     |                          0.0548  |                 95.05 |         0     | N/A                         |
|   213 | H    |         0.17443 | False     |                          0.44628 |                 95.55 |         0     | N/A                         |
|   214 | S    |         0.18423 | False     |                          0.20703 |                 95.03 |         0     | N/A                         |
|   215 | R    |         0.26788 | True      |                          0.4567  |                 95.63 |         0     | N/A                         |
|   216 | Q    |         0.00458 | False     |                          0.00068 |                 96.43 |         0     | N/A                         |
|   217 | C    |         0.1244  | False     |                          0.28094 |                 95.89 |         0     | N/A                         |
|   218 | E    |         0.13854 | False     |                          0.26248 |                 93.93 |         0     | N/A                         |
|   219 | T    |         0.04052 | False     |                          0.16299 |                 90.03 |         0     | N/A                         |
|   220 | S    |         0.14988 | False     |                          0.17091 |                 85.29 |         0     | N/A                         |
|   221 | M    |         0.14538 | False     |                          0.51865 |                 79.9  |         0     | N/A                         |
|   222 | D    |         0.17266 | False     |                          0.61472 |                 80.82 |         0     | N/A                         |
|   223 | G    |         0.26372 | True      |                          0.88942 |                 77.17 |         0     | N/A                         |
|   224 | E    |         0.1897  | False     |                          0.41173 |                 80.71 |         0     | N/A                         |
|   225 | A    |         0.28393 | True      |                          0.55911 |                 84.27 |         0     | N/A                         |
|   226 | G    |         0.05651 | False     |                          0.14533 |                 86.86 |         0     | N/A                         |
|   227 | L    |         0.20847 | False     |                          0.39298 |                 93.86 |         2.729 | N/A                         |
|   228 | C    |         0.11249 | False     |                          0.06922 |                 96.13 |         2.729 | N/A                         |
|   229 | W    |         0.21708 | False     |                          0.21829 |                 96.6  |         2.729 | N/A                         |
|   230 | C    |         0.01684 | False     |                          0       |                 97.01 |         2.729 | N/A                         |
|   231 | V    |         0.03485 | False     |                          0.01428 |                 96.35 |         2.729 | N/A                         |
|   232 | Y    |         0.17714 | False     |                          0.14057 |                 94.54 |         0     | N/A                         |
|   233 | P    |         0.2752  | True      |                          0.29723 |                 93.54 |         0     | N/A                         |
|   234 | W    |         0.25312 | True      |                          0.65472 |                 90.42 |         0     | N/A                         |
|   235 | N    |         0.14947 | False     |                          0.35125 |                 92.3  |         0     | N/A                         |
|   236 | G    |         0.13009 | False     |                          0.24183 |                 94.1  |         0     | N/A                         |
|   237 | K    |         0.13223 | False     |                          0.68619 |                 95.49 |         0     | N/A                         |
|   238 | R    |         0.20682 | False     |                          0.4763  |                 94.86 |         0     | N/A                         |
|   239 | I    |         0.08891 | False     |                          0.01356 |                 93.8  |         0     | N/A                         |
|   240 | P    |         0.21637 | False     |                          0.75071 |                 92.18 |         0     | N/A                         |
|   241 | G    |         0.26985 | True      |                          0.86902 |                 88.36 |         0     | N/A                         |
|   242 | S    |         0.0806  | False     |                          0.04546 |                 90.62 |         0     | Phosphoserine; by FAM20C    |
|   243 | P    |         0.24776 | False     |                          0.34494 |                 92.23 |         0     | N/A                         |
|   244 | E    |         0.28816 | True      |                          0.41573 |                 94.37 |         0     | N/A                         |
|   245 | I    |         0.32161 | True      |                          0.43118 |                 93.67 |         0     | N/A                         |
|   246 | R    |         0.37174 | True      |                          0.45422 |                 91.03 |         0     | N/A                         |
|   247 | G    |         0.23806 | False     |                          0.40952 |                 86.77 |         0     | N/A                         |
|   248 | D    |         0.26295 | True      |                          0.46671 |                 90.18 |         0     | N/A                         |
|   249 | P    |         0.07303 | False     |                          0.02954 |                 92.09 |         0     | N/A                         |
|   250 | N    |         0.26167 | True      |                          0.40371 |                 91.68 |         0     | N/A                         |
|   251 | C    |         0.1143  | False     |                          0.05474 |                 92.06 |         0.177 | N/A                         |
|   252 | Q    |         0.27686 | True      |                          0.54402 |                 87.22 |         0.317 | N/A                         |
|   253 | I    |         0.22681 | False     |                          0.57657 |                 85.81 |         4.264 | N/A                         |
|   254 | Y    |         0.20345 | False     |                          0.23541 |                 81.63 |         4.264 | N/A                         |
|   255 | F    |         0.1787  | False     |                          0.35333 |                 70.33 |         4.264 | N/A                         |
|   256 | N    |         0.18315 | False     |                          0.77035 |                 59.27 |         4.087 | N/A                         |
|   257 | V    |         0.1575  | False     |                          0.80269 |                 53.42 |         4.087 | N/A                         |
|   258 | Q    |         0.16827 | False     |                          0.59848 |                 48.06 |         0.355 | N/A                         |
|   259 | N    |         0.09827 | False     |                          1.20232 |                 38.63 |         0     | N/A                         |


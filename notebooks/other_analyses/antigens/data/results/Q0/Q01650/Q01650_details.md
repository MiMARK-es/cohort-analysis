# Detailed Data for Q01650


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: Q01650
- **Gene Name**: SLC7A5
- **Protein Name**: solute carrier family 7 (amino acid transporter light chain, L system), member 5
- **Swiss Prot**: LAT1_HUMAN
- **Family**: transporter
- **Biomarker Application**: diagnosis
- **Number of Isoforms**: 0
- **Regulation**: 2
- **(transcriptomics) AUC**: nan
- **(transcriptomics) Fold Change**: nan
- **(transcriptomics) Regulation**: Downregulated
- **Discotope Epitope Count**: 122
- **Max n_uniprots (Homo)**: N/A
- **Max n_uniprots (Hetero)**: 6


## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| SLC7A5            | SLC3A2            |   0.999 |
| SLC7A5            | SLC3A1            |   0.925 |
| SLC7A5            | SLC43A1           |   0.915 |

## Homologs

| uniprot_id   | gene_id   |
|:-------------|:----------|
| Q8TBB6       | SLC7A14   |
| O43246       | SLC7A4    |
| E7EPZ8       | SLC7A6    |
| Q8WY07       | SLC7A3    |
| P30825       | SLC7A1    |
| K7EK24       | SLC7A10   |
| A0A9H4ATX5   | SLC7A2    |
| E9PIC3       | SLC7A8    |
| Q9UPY5       | SLC7A11   |
| P82251       | SLC7A9    |
| Q8TCU3       | SLC7A13   |
| G3V2H8       | SLC7A7    |

## Biological Assemblies

|   Unnamed: 0 |   assembly |   n_uniprots | composition   | crystal_id   |
|-------------:|-----------:|-------------:|:--------------|:-------------|
|            0 |          1 |            6 | Hetero        | 7dsk         |
|            0 |          1 |            6 | Hetero        | 7dsq         |
|            0 |          1 |            6 | Hetero        | 6irs         |
|            0 |          1 |            6 | Hetero        | 7dsn         |
|            0 |          1 |            5 | Hetero        | 6jmq         |
|            0 |          1 |            6 | Hetero        | 7dsl         |
|            0 |          1 |            6 | Hetero        | 6irt         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification     |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:-----------------|
|     1 | M    |         0.08401 | False     |                          1.30374 |                 37.02 |         0     | N/A              |
|     2 | A    |         0.16311 | True      |                          1.06648 |                 39.46 |         0     | N/A              |
|     3 | G    |         0.19379 | True      |                          1.01767 |                 37.5  |         0     | N/A              |
|     4 | A    |         0.15812 | True      |                          1.09041 |                 39.67 |         0     | N/A              |
|     5 | G    |         0.26937 | True      |                          0.86822 |                 40.45 |         0     | N/A              |
|     6 | P    |         0.15552 | True      |                          1.02663 |                 42.21 |         0     | N/A              |
|     7 | K    |         0.17084 | True      |                          1.01582 |                 40.58 |         0     | N/A              |
|     8 | R    |         0.1635  | True      |                          0.97407 |                 38.06 |         0     | N/A              |
|     9 | R    |         0.23019 | True      |                          0.97687 |                 38.36 |         0     | N/A              |
|    10 | A    |         0.21555 | True      |                          0.94578 |                 37.51 |         0     | N/A              |
|    11 | L    |         0.18124 | True      |                          1.16128 |                 38.29 |         0     | N/A              |
|    12 | A    |         0.17059 | True      |                          0.86195 |                 43.74 |         0     | N/A              |
|    13 | A    |         0.11992 | False     |                          0.6613  |                 46.06 |         0     | N/A              |
|    14 | P    |         0.16381 | True      |                          0.77378 |                 49.38 |         0     | N/A              |
|    15 | A    |         0.13044 | False     |                          0.69417 |                 50.75 |         0     | N/A              |
|    16 | A    |         0.09577 | False     |                          0.64398 |                 55.33 |         0     | N/A              |
|    17 | E    |         0.1511  | True      |                          0.63431 |                 61.95 |         0     | N/A              |
|    18 | E    |         0.15171 | True      |                          0.67087 |                 62.96 |         0     | N/A              |
|    19 | K    |         0.1916  | True      |                          0.79928 |                 62.99 |         0     | N/A              |
|    20 | E    |         0.12515 | False     |                          0.59417 |                 67.14 |         0     | N/A              |
|    21 | E    |         0.114   | False     |                          0.47202 |                 69.73 |         0     | N/A              |
|    22 | A    |         0.09509 | False     |                          0.53524 |                 69.55 |         0     | N/A              |
|    23 | R    |         0.15267 | True      |                          0.70403 |                 69.52 |         0     | N/A              |
|    24 | E    |         0.14357 | False     |                          0.5815  |                 70.78 |         0     | N/A              |
|    25 | K    |         0.09234 | False     |                          0.64731 |                 70.07 |         0     | N/A              |
|    26 | M    |         0.15111 | True      |                          0.75178 |                 57.81 |         0     | N/A              |
|    27 | L    |         0.09998 | False     |                          0.67423 |                 61.98 |         0     | N/A              |
|    28 | A    |         0.11279 | False     |                          0.59646 |                 62.87 |         0     | N/A              |
|    29 | A    |         0.10395 | False     |                          0.65837 |                 59.01 |         0     | N/A              |
|    30 | K    |         0.17655 | True      |                          0.79398 |                 51.82 |         0     | N/A              |
|    31 | S    |         0.22341 | True      |                          0.71799 |                 49.18 |         0     | Phosphoserine    |
|    32 | A    |         0.21248 | True      |                          0.84804 |                 51.5  |         0     | N/A              |
|    33 | D    |         0.18818 | True      |                          0.68572 |                 45.85 |         0     | N/A              |
|    34 | G    |         0.16299 | True      |                          1.11925 |                 35.25 |         0     | N/A              |
|    35 | S    |         0.19096 | True      |                          0.72537 |                 39.13 |         0     | Phosphoserine    |
|    36 | A    |         0.16599 | True      |                          0.85711 |                 36.09 |         0     | N/A              |
|    37 | P    |         0.23612 | True      |                          0.98609 |                 34.83 |         0     | N/A              |
|    38 | A    |         0.27639 | True      |                          0.90971 |                 39.72 |         0     | N/A              |
|    39 | G    |         0.22251 | True      |                          0.76684 |                 32.16 |         0     | N/A              |
|    40 | E    |         0.25789 | True      |                          0.96428 |                 30.68 |         0     | N/A              |
|    41 | G    |         0.22079 | True      |                          0.94818 |                 33.47 |         0     | N/A              |
|    42 | E    |         0.23473 | True      |                          0.86137 |                 31.34 |         0     | N/A              |
|    43 | G    |         0.22666 | True      |                          0.68244 |                 33.54 |         0     | N/A              |
|    44 | V    |         0.22581 | True      |                          1.10663 |                 39.52 |         0     | N/A              |
|    45 | T    |         0.26386 | True      |                          0.78998 |                 47.14 |         0     | Phosphothreonine |
|    46 | L    |         0.23632 | True      |                          0.53907 |                 56.76 |         0     | N/A              |
|    47 | Q    |         0.27857 | True      |                          0.69261 |                 64.94 |         0     | N/A              |
|    48 | R    |         0.29791 | True      |                          0.58929 |                 75.35 |         0     | N/A              |
|    49 | N    |         0.2603  | True      |                          0.61471 |                 80.94 |         0.29  | N/A              |
|    50 | I    |         0.15739 | True      |                          0.13359 |                 78.61 |         7.669 | N/A              |
|    51 | T    |         0.17368 | True      |                          0.39851 |                 88.42 |         9.53  | N/A              |
|    52 | L    |         0.06655 | False     |                          0.28195 |                 87.57 |        12.96  | N/A              |
|    53 | L    |         0.05531 | False     |                          0.86657 |                 86.32 |        14.237 | N/A              |
|    54 | N    |         0.13294 | False     |                          0.42546 |                 78.85 |        14.467 | N/A              |
|    55 | G    |         0.00518 | False     |                          0       |                 81.1  |        20.491 | N/A              |
|    56 | V    |         0.01583 | False     |                          0.13139 |                 86.45 |        87.153 | N/A              |
|    57 | A    |         0.0067  | False     |                          0.61517 |                 82.12 |        92.531 | N/A              |
|    58 | I    |         0.03685 | False     |                          0.36425 |                 77.9  |        98.863 | N/A              |
|    59 | I    |         0.00224 | False     |                          0.0064  |                 82.57 |        99.43  | N/A              |
|    60 | V    |         0.00875 | False     |                          0.13043 |                 84.47 |        99.328 | N/A              |
|    61 | G    |         0.00935 | False     |                          0.27366 |                 78.54 |        94.178 | N/A              |
|    62 | T    |         0.00963 | False     |                          0.41733 |                 75.46 |        93.718 | N/A              |
|    63 | I    |         0.00662 | False     |                          0.02661 |                 85.36 |        93.461 | N/A              |
|    64 | I    |         0.00668 | False     |                          0.00859 |                 83.04 |        90.071 | N/A              |
|    65 | G    |         0.00604 | False     |                          0.06795 |                 75.45 |        52.969 | N/A              |
|    66 | S    |         0.0058  | False     |                          0.0323  |                 74.09 |        49.635 | N/A              |
|    67 | G    |         0.00315 | False     |                          0.08103 |                 85.88 |        49.221 | N/A              |
|    68 | I    |         0.00154 | False     |                          0       |                 91.94 |        49.187 | N/A              |
|    69 | F    |         0.00461 | False     |                          0.01353 |                 89.85 |        48.841 | N/A              |
|    70 | V    |         0.01828 | False     |                          0.11309 |                 89.12 |        44.764 | N/A              |
|    71 | T    |         0.00118 | False     |                          0       |                 93.16 |         0.32  | N/A              |
|    72 | P    |         0.00635 | False     |                          0.02122 |                 95.02 |         0.142 | N/A              |
|    73 | T    |         0.02693 | False     |                          0.11639 |                 93.25 |         0     | N/A              |
|    74 | G    |         0.01879 | False     |                          0.02736 |                 92    |         0     | N/A              |
|    75 | V    |         0.00103 | False     |                          0.00095 |                 95.13 |         0     | N/A              |
|    76 | L    |         0.00638 | False     |                          0.00082 |                 95.26 |         0     | N/A              |
|    77 | K    |         0.08194 | False     |                          0.53947 |                 93.75 |         0     | N/A              |
|    78 | E    |         0.02787 | False     |                          0.15031 |                 93.3  |         0     | N/A              |
|    79 | A    |         0.00228 | False     |                          0       |                 94.7  |         0     | N/A              |
|    80 | G    |         0.04988 | False     |                          0.20049 |                 92.9  |         0     | N/A              |
|    81 | S    |         0.00666 | False     |                          0       |                 93.4  |         0     | N/A              |
|    82 | P    |         0.0168  | False     |                          0.06163 |                 93.59 |         0.052 | N/A              |
|    83 | G    |         0.01752 | False     |                          0.08187 |                 93.63 |         4.57  | N/A              |
|    84 | L    |         0.04225 | False     |                          0.13602 |                 94.31 |        68.995 | N/A              |
|    85 | A    |         0.00361 | False     |                          0.0102  |                 95.81 |        81.331 | N/A              |
|    86 | L    |         0.01453 | False     |                          0.19367 |                 95.51 |        96.678 | N/A              |
|    87 | V    |         0.01553 | False     |                          0.56631 |                 95.73 |        99.607 | N/A              |
|    88 | V    |         0.00766 | False     |                          0.02761 |                 96.38 |        99.854 | N/A              |
|    89 | W    |         0.00178 | False     |                          0.00256 |                 97.16 |        99.8   | N/A              |
|    90 | A    |         0.00731 | False     |                          0.3788  |                 96.85 |        99.439 | N/A              |
|    91 | A    |         0.00537 | False     |                          0.40333 |                 96.5  |        99.108 | N/A              |
|    92 | C    |         0.00082 | False     |                          0       |                 96.07 |        98.821 | N/A              |
|    93 | G    |         0.00149 | False     |                          0       |                 95.41 |        98.552 | N/A              |
|    94 | V    |         0.01217 | False     |                          0.65217 |                 95.33 |        98.604 | N/A              |
|    95 | F    |         0.00549 | False     |                          0.1142  |                 94.94 |        98.315 | N/A              |
|    96 | S    |         0.001   | False     |                          0.00158 |                 94.39 |        94.731 | N/A              |
|    97 | I    |         0.01733 | False     |                          0.22399 |                 93.93 |        94.288 | N/A              |
|    98 | V    |         0.00389 | False     |                          0.10758 |                 94.4  |        89.429 | N/A              |
|    99 | G    |         0.00081 | False     |                          0       |                 93.73 |        32.21  | N/A              |
|   100 | A    |         0.0014  | False     |                          0.00255 |                 93.06 |        27.061 | N/A              |
|   101 | L    |         0.01127 | False     |                          0.19845 |                 93    |        23.021 | N/A              |
|   102 | C    |         0.00144 | False     |                          0       |                 93.54 |         2.463 | N/A              |
|   103 | Y    |         0.00104 | False     |                          0.00164 |                 91.69 |         1.13  | N/A              |
|   104 | A    |         0.00252 | False     |                          0.00128 |                 90.98 |         0.143 | N/A              |
|   105 | E    |         0.01933 | False     |                          0.01006 |                 92.38 |         0     | N/A              |
|   106 | L    |         0.00953 | False     |                          0.00577 |                 90.75 |         0.058 | N/A              |
|   107 | G    |         0.0073  | False     |                          0.0112  |                 86.01 |         0.058 | N/A              |
|   108 | T    |         0.03912 | False     |                          0.06917 |                 86.73 |         0.058 | N/A              |
|   109 | T    |         0.1042  | False     |                          0.17997 |                 89.44 |         0.058 | N/A              |
|   110 | I    |         0.06296 | False     |                          0.07127 |                 85.49 |         0.058 | N/A              |
|   111 | S    |         0.21207 | True      |                          0.57416 |                 76.23 |         0     | N/A              |
|   112 | K    |         0.15627 | True      |                          0.61706 |                 74.65 |         0     | N/A              |
|   113 | S    |         0.09098 | False     |                          0.30974 |                 69.4  |         0     | N/A              |
|   114 | G    |         0.0231  | False     |                          0.05394 |                 72.95 |         0     | N/A              |
|   115 | G    |         0.01092 | False     |                          0.0092  |                 81.64 |         0     | N/A              |
|   116 | D    |         0.00782 | False     |                          0.04506 |                 85.19 |         0     | N/A              |
|   117 | Y    |         0.01445 | False     |                          0.01323 |                 89.49 |         0.483 | N/A              |
|   118 | A    |         0.00799 | False     |                          0.04836 |                 87.63 |         0.483 | N/A              |
|   119 | Y    |         0.01178 | False     |                          0.01613 |                 90.22 |         0.483 | N/A              |
|   120 | M    |         0.00522 | False     |                          0.03955 |                 92.54 |         0.483 | N/A              |
|   121 | L    |         0.05974 | False     |                          0.26376 |                 93.29 |         0.483 | N/A              |
|   122 | E    |         0.06367 | False     |                          0.31377 |                 91.66 |         0     | N/A              |
|   123 | V    |         0.0487  | False     |                          0.08486 |                 93.33 |         0     | N/A              |
|   124 | Y    |         0.08153 | False     |                          0.34102 |                 94.33 |         0     | N/A              |
|   125 | G    |         0.0858  | False     |                          0.32424 |                 93.04 |         0     | N/A              |
|   126 | S    |         0.09362 | False     |                          0.32522 |                 92.97 |         0     | N/A              |
|   127 | L    |         0.08375 | False     |                          0.35497 |                 94.53 |         0     | N/A              |
|   128 | P    |         0.02344 | False     |                          0.3178  |                 94.72 |         0.523 | N/A              |
|   129 | A    |         0.00259 | False     |                          0       |                 93.77 |        43.165 | N/A              |
|   130 | F    |         0.01343 | False     |                          0.02166 |                 94.95 |        93.622 | N/A              |
|   131 | L    |         0.01074 | False     |                          0.18795 |                 95.47 |        97.738 | N/A              |
|   132 | K    |         0.00718 | False     |                          0.03482 |                 94.11 |        98.491 | N/A              |
|   133 | L    |         0.00257 | False     |                          0.0033  |                 93.61 |        98.491 | N/A              |
|   134 | W    |         0.01306 | False     |                          0.20084 |                 95.01 |        98.491 | N/A              |
|   135 | I    |         0.0073  | False     |                          0.0512  |                 94.47 |        98.491 | N/A              |
|   136 | E    |         0.00465 | False     |                          0.08746 |                 92.37 |        98.491 | N/A              |
|   137 | L    |         0.00505 | False     |                          0.04308 |                 93.09 |        98.424 | N/A              |
|   138 | L    |         0.0113  | False     |                          0.17616 |                 94.22 |        98.055 | N/A              |
|   139 | I    |         0.00302 | False     |                          0       |                 93.78 |        96.039 | N/A              |
|   140 | I    |         0.00876 | False     |                          0.0768  |                 92.39 |        87.985 | N/A              |
|   141 | R    |         0.0044  | False     |                          0.03532 |                 90.92 |         0     | N/A              |
|   142 | P    |         0.00055 | False     |                          0.00099 |                 94.31 |         0     | N/A              |
|   143 | S    |         0.0021  | False     |                          0       |                 94.12 |         0.016 | N/A              |
|   144 | S    |         0.00321 | False     |                          0.17287 |                 92.19 |         0.37  | N/A              |
|   145 | Q    |         0.00239 | False     |                          0.00741 |                 93.1  |         3.22  | N/A              |
|   146 | Y    |         0.0027  | False     |                          0.01542 |                 95.63 |        75.995 | N/A              |
|   147 | I    |         0.0028  | False     |                          0.0016  |                 93.58 |        97.634 | N/A              |
|   148 | V    |         0.00567 | False     |                          0.10568 |                 92.52 |        99.608 | N/A              |
|   149 | A    |         0.00059 | False     |                          0       |                 94.66 |        99.767 | N/A              |
|   150 | L    |         0.02309 | False     |                          0.12283 |                 94.74 |        99.949 | N/A              |
|   151 | V    |         0.0032  | False     |                          0.03332 |                 92.92 |        99.961 | N/A              |
|   152 | F    |         0.01931 | False     |                          0.14204 |                 93.05 |        99.663 | N/A              |
|   153 | A    |         0.00092 | False     |                          0       |                 94.98 |        95.897 | N/A              |
|   154 | T    |         0.03305 | False     |                          0.13172 |                 93.43 |        92.74  | N/A              |
|   155 | Y    |         0.01613 | False     |                          0.00771 |                 92.18 |        90.857 | N/A              |
|   156 | L    |         0.01361 | False     |                          0.55121 |                 93.3  |        84.365 | N/A              |
|   157 | L    |         0.0687  | False     |                          0.13025 |                 93.88 |        71.305 | N/A              |
|   158 | K    |         0.07178 | False     |                          0.06505 |                 91.55 |         0     | N/A              |
|   159 | P    |         0.11517 | False     |                          0.45944 |                 89.76 |         0     | N/A              |
|   160 | L    |         0.23128 | True      |                          0.80361 |                 91.5  |         0     | N/A              |
|   161 | F    |         0.1976  | True      |                          0.34289 |                 91.32 |         0     | N/A              |
|   162 | P    |         0.31186 | True      |                          0.60963 |                 84.23 |         0     | N/A              |
|   163 | T    |         0.33964 | True      |                          0.91591 |                 84.92 |         0     | N/A              |
|   164 | C    |         0.25662 | True      |                          0.48612 |                 89.95 |         0     | N/A              |
|   165 | P    |         0.27777 | True      |                          0.736   |                 90.12 |         0     | N/A              |
|   166 | V    |         0.05659 | False     |                          0.0835  |                 93.15 |         0     | N/A              |
|   167 | P    |         0.20018 | True      |                          0.44733 |                 94.76 |         0     | N/A              |
|   168 | E    |         0.15634 | True      |                          0.45574 |                 92.47 |         0     | N/A              |
|   169 | E    |         0.20175 | True      |                          0.6237  |                 93.84 |         0.086 | N/A              |
|   170 | A    |         0.09126 | False     |                          0.32835 |                 95.68 |         0.086 | N/A              |
|   171 | A    |         0.01285 | False     |                          0.04974 |                 95.23 |         0.09  | N/A              |
|   172 | K    |         0.02356 | False     |                          0.13156 |                 96.32 |         0.108 | N/A              |
|   173 | L    |         0.02824 | False     |                          0.7781  |                 97.07 |        58.796 | N/A              |
|   174 | V    |         0.00811 | False     |                          0.23226 |                 96.91 |        69.54  | N/A              |
|   175 | A    |         0.0029  | False     |                          0.00342 |                 96.38 |        71.669 | N/A              |
|   176 | C    |         0.00717 | False     |                          0.17196 |                 97.19 |        74.187 | N/A              |
|   177 | L    |         0.02326 | False     |                          0.71331 |                 97.07 |        86.118 | N/A              |
|   178 | C    |         0.0074  | False     |                          0.03148 |                 94.87 |        88.237 | N/A              |
|   179 | V    |         0.00327 | False     |                          0.01142 |                 95.64 |        97.811 | N/A              |
|   180 | L    |         0.01343 | False     |                          0.53517 |                 96.56 |        98.513 | N/A              |
|   181 | L    |         0.02405 | False     |                          0.58318 |                 94.01 |        98.389 | N/A              |
|   182 | L    |         0.00615 | False     |                          0.00989 |                 91.92 |        96.717 | N/A              |
|   183 | T    |         0.01618 | False     |                          0.06284 |                 93.14 |        87.322 | N/A              |
|   184 | A    |         0.01214 | False     |                          0.45695 |                 92.96 |        80.933 | N/A              |
|   185 | V    |         0.01018 | False     |                          0.34484 |                 89.84 |        75.474 | N/A              |
|   186 | N    |         0.01082 | False     |                          0.03003 |                 87.64 |         5.946 | N/A              |
|   187 | C    |         0.06132 | False     |                          0.13433 |                 89.52 |         3.208 | N/A              |
|   188 | Y    |         0.16244 | True      |                          0.72144 |                 89.57 |         2.714 | N/A              |
|   189 | S    |         0.20617 | True      |                          0.29627 |                 82.92 |         1.038 | N/A              |
|   190 | V    |         0.07142 | False     |                          0.32849 |                 75.34 |         0.958 | N/A              |
|   191 | K    |         0.27396 | True      |                          0.79128 |                 76.97 |         0     | N/A              |
|   192 | A    |         0.05195 | False     |                          0.39412 |                 74.2  |         0     | N/A              |
|   193 | A    |         0.01075 | False     |                          0.02215 |                 70.12 |         0     | N/A              |
|   194 | T    |         0.06473 | False     |                          0.3978  |                 73.15 |         0     | N/A              |
|   195 | R    |         0.05408 | False     |                          0.75558 |                 74.74 |         0     | N/A              |
|   196 | V    |         0.01708 | False     |                          0.36356 |                 74.99 |         0.004 | N/A              |
|   197 | Q    |         0.01897 | False     |                          0.26689 |                 73.91 |         0.006 | N/A              |
|   198 | D    |         0.02079 | False     |                          0.61547 |                 73.46 |         0.146 | N/A              |
|   199 | A    |         0.01256 | False     |                          0.57295 |                 78.51 |         0.146 | N/A              |
|   200 | F    |         0.01136 | False     |                          0.13899 |                 80.52 |         0.146 | N/A              |
|   201 | A    |         0.01098 | False     |                          0.30842 |                 75.27 |         0.146 | N/A              |
|   202 | A    |         0.01046 | False     |                          0.50816 |                 79.57 |         0.146 | N/A              |
|   203 | A    |         0.00753 | False     |                          0.08091 |                 81.83 |         0.146 | N/A              |
|   204 | K    |         0.01467 | False     |                          0.06566 |                 80.33 |         0.146 | N/A              |
|   205 | L    |         0.01187 | False     |                          0.52305 |                 83.96 |        69.919 | N/A              |
|   206 | L    |         0.0177  | False     |                          0.64357 |                 85.21 |        82.698 | N/A              |
|   207 | A    |         0.00359 | False     |                          0       |                 85.47 |        89.097 | N/A              |
|   208 | L    |         0.00947 | False     |                          0.01978 |                 90.61 |        96.665 | N/A              |
|   209 | A    |         0.00659 | False     |                          0.42036 |                 90.72 |        98.049 | N/A              |
|   210 | L    |         0.03579 | False     |                          0.29619 |                 90.73 |        99.668 | N/A              |
|   211 | I    |         0.00263 | False     |                          0       |                 92.34 |        99.947 | N/A              |
|   212 | I    |         0.02935 | False     |                          0.13053 |                 93.74 |        99.957 | N/A              |
|   213 | L    |         0.02137 | False     |                          0.69967 |                 93.99 |        99.776 | N/A              |
|   214 | L    |         0.15305 | True      |                          0.19372 |                 92.43 |        98.763 | N/A              |
|   215 | G    |         0.01115 | False     |                          0.00729 |                 92.15 |        93.161 | N/A              |
|   216 | F    |         0.03763 | False     |                          0.5159  |                 92.89 |        92.655 | N/A              |
|   217 | V    |         0.12782 | False     |                          0.575   |                 92.4  |        86.573 | N/A              |
|   218 | Q    |         0.13138 | False     |                          0.09406 |                 90.3  |        14.998 | N/A              |
|   219 | I    |         0.20744 | True      |                          0.41021 |                 89.59 |        12.195 | N/A              |
|   220 | G    |         0.14773 | True      |                          0.83144 |                 89.28 |         1.008 | N/A              |
|   221 | K    |         0.31059 | True      |                          0.74106 |                 89.67 |         0.001 | N/A              |
|   222 | G    |         0.26054 | True      |                          0.38182 |                 83.43 |         0.001 | N/A              |
|   223 | D    |         0.32828 | True      |                          0.88782 |                 78.7  |         0.001 | N/A              |
|   224 | V    |         0.20983 | True      |                          0.21687 |                 81.53 |         0.001 | N/A              |
|   225 | S    |         0.30316 | True      |                          0.57493 |                 77.98 |         0     | N/A              |
|   226 | N    |         0.16412 | True      |                          0.23075 |                 74.59 |         0     | N/A              |
|   227 | L    |         0.1108  | False     |                          0.28472 |                 79.17 |         0     | N/A              |
|   228 | D    |         0.24852 | True      |                          0.27913 |                 82.45 |         0     | N/A              |
|   229 | P    |         0.2161  | True      |                          0.84371 |                 79.31 |         0     | N/A              |
|   230 | N    |         0.36574 | True      |                          0.77836 |                 79.78 |         0     | N/A              |
|   231 | F    |         0.31094 | True      |                          0.61049 |                 83.12 |         0     | N/A              |
|   232 | S    |         0.06968 | False     |                          0.07963 |                 86.07 |         0     | N/A              |
|   233 | F    |         0.13268 | False     |                          0.57702 |                 90.9  |         0     | N/A              |
|   234 | E    |         0.35105 | True      |                          0.65379 |                 86.84 |         0     | N/A              |
|   235 | G    |         0.16548 | True      |                          0.67    |                 86.43 |         0     | N/A              |
|   236 | T    |         0.12994 | False     |                          0.26042 |                 91.96 |         0     | N/A              |
|   237 | K    |         0.15204 | True      |                          0.43965 |                 90.28 |         0.024 | N/A              |
|   238 | L    |         0.16327 | True      |                          0.8123  |                 89.41 |         0.024 | N/A              |
|   239 | D    |         0.19612 | True      |                          0.40462 |                 91.07 |         0.024 | N/A              |
|   240 | V    |         0.0465  | False     |                          0.51467 |                 90.64 |         1.261 | N/A              |
|   241 | G    |         0.01063 | False     |                          0       |                 88.18 |         1.36  | N/A              |
|   242 | N    |         0.06149 | False     |                          0.17457 |                 91.09 |         4.563 | N/A              |
|   243 | I    |         0.03504 | False     |                          0.30079 |                 92.04 |        89.446 | N/A              |
|   244 | V    |         0.00176 | False     |                          0.00286 |                 90.1  |        96.84  | N/A              |
|   245 | L    |         0.02011 | False     |                          0.11598 |                 88.38 |        97.362 | N/A              |
|   246 | A    |         0.00109 | False     |                          0       |                 92.75 |        97.446 | N/A              |
|   247 | L    |         0.00685 | False     |                          0.20774 |                 93.15 |        97.521 | N/A              |
|   248 | Y    |         0.00247 | False     |                          0.00622 |                 89.94 |        93.075 | N/A              |
|   249 | S    |         0.00384 | False     |                          0.03479 |                 91.04 |        76.366 | N/A              |
|   250 | G    |         0.00054 | False     |                          0       |                 93.86 |        74.314 | N/A              |
|   251 | L    |         0.0038  | False     |                          0.03182 |                 93.23 |        74.33  | N/A              |
|   252 | F    |         0.00518 | False     |                          0.11223 |                 91.17 |        73.333 | N/A              |
|   253 | A    |         0.00352 | False     |                          0.02118 |                 92.65 |        60.875 | N/A              |
|   254 | Y    |         0.00154 | False     |                          0.00234 |                 91.46 |        50.345 | N/A              |
|   255 | G    |         0.01838 | False     |                          0.34988 |                 85.78 |        14.002 | N/A              |
|   256 | G    |         0.01053 | False     |                          0.08715 |                 81.79 |        10.707 | N/A              |
|   257 | W    |         0.00924 | False     |                          0.03766 |                 86.95 |        10.571 | N/A              |
|   258 | N    |         0.0156  | False     |                          0.13425 |                 84.5  |         5.102 | N/A              |
|   259 | Y    |         0.02007 | False     |                          0.29033 |                 71.02 |         5.377 | N/A              |
|   260 | L    |         0.01366 | False     |                          0       |                 74.93 |         4.695 | N/A              |
|   261 | N    |         0.02987 | False     |                          0.05418 |                 76.74 |         0.852 | N/A              |
|   262 | F    |         0.07429 | False     |                          0.23117 |                 69.42 |         0.84  | N/A              |
|   263 | V    |         0.05501 | False     |                          0.12377 |                 70.64 |         0.785 | N/A              |
|   264 | T    |         0.07062 | False     |                          0.05272 |                 74.64 |         0.169 | N/A              |
|   265 | E    |         0.14166 | False     |                          0.33043 |                 73.5  |         0     | N/A              |
|   266 | E    |         0.10909 | False     |                          0.24585 |                 78.09 |         0     | N/A              |
|   267 | M    |         0.01536 | False     |                          0       |                 80.27 |         0     | N/A              |
|   268 | I    |         0.17875 | True      |                          0.43278 |                 86.32 |         0     | N/A              |
|   269 | N    |         0.18255 | True      |                          0.47103 |                 86.79 |         0     | N/A              |
|   270 | P    |         0.0514  | False     |                          0.06859 |                 84.42 |         0     | N/A              |
|   271 | Y    |         0.17226 | True      |                          0.50003 |                 87.64 |         0     | N/A              |
|   272 | R    |         0.20621 | True      |                          0.63755 |                 89.29 |         0     | N/A              |
|   273 | N    |         0.04291 | False     |                          0.11705 |                 88.58 |         0     | N/A              |
|   274 | L    |         0.00772 | False     |                          0       |                 87.15 |         0     | N/A              |
|   275 | P    |         0.05925 | False     |                          0.15408 |                 89.73 |         0.917 | N/A              |
|   276 | L    |         0.02423 | False     |                          0.37673 |                 91.28 |        69.424 | N/A              |
|   277 | A    |         0.0036  | False     |                          0       |                 90.42 |        69.475 | N/A              |
|   278 | I    |         0.00292 | False     |                          0.0016  |                 90.97 |        69.475 | N/A              |
|   279 | I    |         0.01438 | False     |                          0.51483 |                 91.81 |        69.475 | N/A              |
|   280 | I    |         0.01624 | False     |                          0.42732 |                 93.29 |        69.398 | N/A              |
|   281 | S    |         0.00213 | False     |                          0       |                 91.68 |         0.331 | N/A              |
|   282 | L    |         0.00121 | False     |                          0       |                 93.85 |         0.001 | N/A              |
|   283 | P    |         0.01161 | False     |                          0.42879 |                 95.19 |         1.067 | N/A              |
|   284 | I    |         0.01055 | False     |                          0.44366 |                 93.61 |        89.705 | N/A              |
|   285 | V    |         0.00042 | False     |                          0       |                 93.97 |        97.909 | N/A              |
|   286 | T    |         0.00825 | False     |                          0.14567 |                 95.66 |        98.606 | N/A              |
|   287 | L    |         0.01448 | False     |                          0.65549 |                 95.65 |        99.766 | N/A              |
|   288 | V    |         0.00515 | False     |                          0.19708 |                 94.84 |        99.968 | N/A              |
|   289 | Y    |         0.00108 | False     |                          0       |                 95.69 |        99.965 | N/A              |
|   290 | V    |         0.01368 | False     |                          0.26372 |                 96.16 |        99.894 | N/A              |
|   291 | L    |         0.00792 | False     |                          0.22856 |                 95.8  |        99.001 | N/A              |
|   292 | T    |         0.00072 | False     |                          0       |                 95.23 |        94.063 | N/A              |
|   293 | N    |         0.00354 | False     |                          0.00637 |                 95.18 |        91.119 | N/A              |
|   294 | L    |         0.02894 | False     |                          0.23989 |                 94.13 |        91.007 | N/A              |
|   295 | A    |         0.00453 | False     |                          0.02734 |                 94.82 |        90.388 | N/A              |
|   296 | Y    |         0.00419 | False     |                          0.00149 |                 94.57 |        89.864 | N/A              |
|   297 | F    |         0.01021 | False     |                          0.00904 |                 93.65 |        88.056 | N/A              |
|   298 | T    |         0.06411 | False     |                          0.05036 |                 92.09 |        65.894 | N/A              |
|   299 | T    |         0.11287 | False     |                          0.1231  |                 90.97 |        52.709 | N/A              |
|   300 | L    |         0.03917 | False     |                          0.04165 |                 91.89 |        44.865 | N/A              |
|   301 | S    |         0.19472 | True      |                          0.30746 |                 91.1  |         2.036 | N/A              |
|   302 | T    |         0.07835 | False     |                          0.1727  |                 90.66 |         0.118 | N/A              |
|   303 | E    |         0.23092 | True      |                          0.61901 |                 90.9  |         0     | N/A              |
|   304 | Q    |         0.13858 | False     |                          0.48836 |                 91.57 |         0     | N/A              |
|   305 | M    |         0.00712 | False     |                          0.00072 |                 92.93 |         0     | N/A              |
|   306 | L    |         0.10289 | False     |                          0.45307 |                 92.33 |         0     | N/A              |
|   307 | S    |         0.21219 | True      |                          0.70202 |                 91.51 |         0     | N/A              |
|   308 | S    |         0.05362 | False     |                          0.06165 |                 90.66 |         0     | N/A              |
|   309 | E    |         0.1024  | False     |                          0.40527 |                 87.08 |         0     | N/A              |
|   310 | A    |         0.00644 | False     |                          0       |                 91.39 |         0     | N/A              |
|   311 | V    |         0.0112  | False     |                          0.02367 |                 92.92 |         0     | N/A              |
|   312 | A    |         0.00128 | False     |                          0       |                 92.57 |         0     | N/A              |
|   313 | V    |         0.02202 | False     |                          0.03523 |                 91.68 |         0     | N/A              |
|   314 | D    |         0.06564 | False     |                          0.20446 |                 91.93 |         0     | N/A              |
|   315 | F    |         0.00582 | False     |                          0       |                 92.86 |         0     | N/A              |
|   316 | G    |         0.00538 | False     |                          0.00161 |                 91.67 |         0     | N/A              |
|   317 | N    |         0.12357 | False     |                          0.46481 |                 90.02 |         0     | N/A              |
|   318 | Y    |         0.30288 | True      |                          0.5952  |                 89.98 |         0.135 | N/A              |
|   319 | H    |         0.10302 | False     |                          0.22885 |                 90.29 |         0.135 | N/A              |
|   320 | L    |         0.10488 | False     |                          0.21297 |                 85.69 |         2.193 | N/A              |
|   321 | G    |         0.16075 | True      |                          0.59881 |                 83.74 |         2.531 | N/A              |
|   322 | V    |         0.1844  | True      |                          1.00763 |                 79.65 |         7.075 | N/A              |
|   323 | M    |         0.09354 | False     |                          0.62655 |                 81.58 |         7.075 | N/A              |
|   324 | S    |         0.05502 | False     |                          0.09723 |                 83.69 |         7.075 | N/A              |
|   325 | W    |         0.12018 | False     |                          0.69885 |                 85.66 |         7.075 | N/A              |
|   326 | I    |         0.02231 | False     |                          0.21359 |                 86.95 |         6.908 | N/A              |
|   327 | I    |         0.00412 | False     |                          0       |                 88.14 |         0.425 | N/A              |
|   328 | P    |         0.03196 | False     |                          0.08191 |                 89.22 |         0.567 | N/A              |
|   329 | V    |         0.01362 | False     |                          0.47289 |                 88.28 |        41.443 | N/A              |
|   330 | F    |         0.01395 | False     |                          0.26434 |                 87.96 |        42.537 | N/A              |
|   331 | V    |         0.00162 | False     |                          0       |                 88.21 |        42.537 | N/A              |
|   332 | G    |         0.0094  | False     |                          0.04913 |                 89.39 |        42.537 | N/A              |
|   333 | L    |         0.00588 | False     |                          0.37415 |                 86.98 |        42.537 | N/A              |
|   334 | S    |         0.00225 | False     |                          0.01465 |                 88.07 |        15.577 | N/A              |
|   335 | C    |         0.001   | False     |                          0       |                 88.82 |        12.006 | N/A              |
|   336 | F    |         0.00614 | False     |                          0.15818 |                 86.65 |        11.313 | N/A              |
|   337 | G    |         0.00348 | False     |                          0.03414 |                 84.61 |         2.041 | N/A              |
|   338 | S    |         0.00836 | False     |                          0.25631 |                 84.83 |         1.287 | N/A              |
|   339 | V    |         0.00185 | False     |                          0.00381 |                 88.22 |         1.193 | N/A              |
|   340 | N    |         0.00513 | False     |                          0.02241 |                 85.67 |         0     | N/A              |
|   341 | G    |         0.00881 | False     |                          0.22348 |                 79.28 |         0     | N/A              |
|   342 | S    |         0.00874 | False     |                          0.16272 |                 83.31 |         0     | N/A              |
|   343 | L    |         0.00294 | False     |                          0       |                 85.19 |         0     | N/A              |
|   344 | F    |         0.05196 | False     |                          0.34029 |                 75.99 |         0     | N/A              |
|   345 | T    |         0.01617 | False     |                          0.25499 |                 76.78 |         0     | N/A              |
|   346 | S    |         0.00416 | False     |                          0.0052  |                 82.23 |         0     | N/A              |
|   347 | S    |         0.02664 | False     |                          0.07405 |                 80.61 |         0     | N/A              |
|   348 | R    |         0.14338 | False     |                          0.4233  |                 76.86 |         0     | N/A              |
|   349 | L    |         0.02035 | False     |                          0.0596  |                 83.24 |        11.647 | N/A              |
|   350 | F    |         0.00225 | False     |                          0.0026  |                 88.8  |        12.673 | N/A              |
|   351 | F    |         0.09372 | False     |                          0.17896 |                 83.02 |        12.673 | N/A              |
|   352 | V    |         0.03694 | False     |                          0.12663 |                 83.29 |        12.673 | N/A              |
|   353 | G    |         0.00607 | False     |                          0       |                 88.47 |        12.673 | N/A              |
|   354 | S    |         0.03538 | False     |                          0.14647 |                 89.14 |         6.624 | N/A              |
|   355 | R    |         0.14466 | True      |                          0.72043 |                 85.82 |         0     | N/A              |
|   356 | E    |         0.09212 | False     |                          0.3946  |                 88.52 |         0     | N/A              |
|   357 | G    |         0.12519 | False     |                          0.56393 |                 88.04 |         0     | N/A              |
|   358 | H    |         0.05488 | False     |                          0.07108 |                 90.93 |         0     | N/A              |
|   359 | L    |         0.01803 | False     |                          0.11124 |                 91.32 |         0     | N/A              |
|   360 | P    |         0.08488 | False     |                          0.59049 |                 90.56 |         0     | N/A              |
|   361 | S    |         0.07592 | False     |                          0.50393 |                 89.27 |         0.65  | N/A              |
|   362 | I    |         0.08724 | False     |                          0.14606 |                 91.54 |         5.9   | N/A              |
|   363 | L    |         0.01277 | False     |                          0.13681 |                 91.11 |         5.9   | N/A              |
|   364 | S    |         0.03269 | False     |                          0.08212 |                 89.59 |         5.9   | N/A              |
|   365 | M    |         0.05178 | False     |                          0.02876 |                 91.19 |         5.9   | N/A              |
|   366 | I    |         0.12095 | False     |                          0.23279 |                 90.4  |         5.9   | N/A              |
|   367 | H    |         0.09182 | False     |                          0.10845 |                 89.87 |         0     | N/A              |
|   368 | P    |         0.19897 | True      |                          0.4216  |                 87.4  |         0     | N/A              |
|   369 | Q    |         0.23502 | True      |                          0.72648 |                 87.16 |         0     | N/A              |
|   370 | L    |         0.1327  | False     |                          0.41904 |                 86.25 |         0     | N/A              |
|   371 | L    |         0.21651 | True      |                          0.79225 |                 87.48 |         0     | N/A              |
|   372 | T    |         0.01665 | False     |                          0       |                 86.1  |         0     | N/A              |
|   373 | P    |         0.04457 | False     |                          0.1014  |                 90.48 |         0     | N/A              |
|   374 | V    |         0.03926 | False     |                          0.14091 |                 92.13 |         0     | N/A              |
|   375 | P    |         0.01791 | False     |                          0.04473 |                 93.36 |         0.105 | N/A              |
|   376 | S    |         0.00253 | False     |                          0.00646 |                 92.49 |         8.749 | N/A              |
|   377 | L    |         0.00813 | False     |                          0.0305  |                 92.53 |        78.401 | N/A              |
|   378 | V    |         0.00783 | False     |                          0.39225 |                 94.48 |        91.156 | N/A              |
|   379 | F    |         0.00511 | False     |                          0.26808 |                 95.12 |        92.239 | N/A              |
|   380 | T    |         0.00471 | False     |                          0.02427 |                 94.15 |        92.327 | N/A              |
|   381 | C    |         0.0123  | False     |                          0.05217 |                 95.59 |        92.47  | N/A              |
|   382 | V    |         0.01341 | False     |                          0.5267  |                 96.74 |        93.231 | N/A              |
|   383 | M    |         0.0134  | False     |                          0.21627 |                 96.06 |        93.154 | N/A              |
|   384 | T    |         0.00273 | False     |                          0.00451 |                 96.4  |        93.041 | N/A              |
|   385 | L    |         0.01858 | False     |                          0.27836 |                 96.84 |        93.022 | N/A              |
|   386 | L    |         0.01963 | False     |                          0.56605 |                 96.12 |        92.516 | N/A              |
|   387 | Y    |         0.01619 | False     |                          0.15322 |                 95.23 |        89.669 | N/A              |
|   388 | A    |         0.01406 | False     |                          0.15571 |                 94.57 |        79.854 | N/A              |
|   389 | F    |         0.09866 | False     |                          0.8511  |                 93.24 |        71.552 | N/A              |
|   390 | S    |         0.03907 | False     |                          0.20013 |                 91.01 |        34.37  | N/A              |
|   391 | K    |         0.20658 | True      |                          0.92051 |                 85.74 |         0.051 | N/A              |
|   392 | D    |         0.24164 | True      |                          0.39543 |                 86.9  |         0.051 | N/A              |
|   393 | I    |         0.0321  | False     |                          0.17877 |                 88.03 |        19.792 | N/A              |
|   394 | F    |         0.03673 | False     |                          0.23669 |                 85.16 |        20.168 | N/A              |
|   395 | S    |         0.05063 | False     |                          0.25542 |                 87.91 |        20.569 | N/A              |
|   396 | V    |         0.0091  | False     |                          0.04665 |                 91.3  |        53.918 | N/A              |
|   397 | I    |         0.00283 | False     |                          0.0032  |                 88.76 |        56.98  | N/A              |
|   398 | N    |         0.01548 | False     |                          0.13811 |                 85.6  |        57.277 | N/A              |
|   399 | F    |         0.02364 | False     |                          0.09551 |                 89.2  |        71.787 | N/A              |
|   400 | F    |         0.0071  | False     |                          0.10128 |                 91.91 |        76.708 | N/A              |
|   401 | S    |         0.00176 | False     |                          0.00682 |                 89.74 |        78.753 | N/A              |
|   402 | F    |         0.01303 | False     |                          0.01167 |                 89.4  |        95.418 | N/A              |
|   403 | F    |         0.00245 | False     |                          0.00064 |                 91.75 |        96.748 | N/A              |
|   404 | N    |         0.00547 | False     |                          0.16821 |                 92.38 |        96.52  | N/A              |
|   405 | W    |         0.00622 | False     |                          0.03017 |                 92.36 |        99.355 | N/A              |
|   406 | L    |         0.01194 | False     |                          0.19125 |                 92.71 |        99.458 | N/A              |
|   407 | C    |         0.00426 | False     |                          0.01598 |                 93    |        99.215 | N/A              |
|   408 | V    |         0.00442 | False     |                          0.01523 |                 93.14 |        98.998 | N/A              |
|   409 | A    |         0.00861 | False     |                          0.01148 |                 94.69 |        95.961 | N/A              |
|   410 | L    |         0.01221 | False     |                          0.39487 |                 94.88 |        93.395 | N/A              |
|   411 | A    |         0.00479 | False     |                          0.02124 |                 93.62 |        79.368 | N/A              |
|   412 | I    |         0.00299 | False     |                          0       |                 94.43 |        78.867 | N/A              |
|   413 | I    |         0.0302  | False     |                          0.36913 |                 95.94 |        74.902 | N/A              |
|   414 | G    |         0.00624 | False     |                          0.00322 |                 93.83 |        35.291 | N/A              |
|   415 | M    |         0.02943 | False     |                          0.01848 |                 93.79 |        34.419 | N/A              |
|   416 | I    |         0.05229 | False     |                          0.16879 |                 94.43 |        33.685 | N/A              |
|   417 | W    |         0.09153 | False     |                          0.38525 |                 94.54 |        25.932 | N/A              |
|   418 | L    |         0.03892 | False     |                          0.01814 |                 93.18 |        18.756 | N/A              |
|   419 | R    |         0.20948 | True      |                          0.12826 |                 92.11 |         0     | N/A              |
|   420 | H    |         0.19648 | True      |                          0.70923 |                 91.73 |         0     | N/A              |
|   421 | R    |         0.2419  | True      |                          0.67225 |                 92.82 |         0     | N/A              |
|   422 | K    |         0.22925 | True      |                          0.3204  |                 91.69 |         0     | N/A              |
|   423 | P    |         0.34    | True      |                          0.64897 |                 90.06 |         0     | N/A              |
|   424 | E    |         0.4374  | True      |                          0.67893 |                 91.09 |         0     | N/A              |
|   425 | L    |         0.2718  | True      |                          0.38347 |                 89.34 |         0     | N/A              |
|   426 | E    |         0.22892 | True      |                          0.73963 |                 88.63 |         0     | N/A              |
|   427 | R    |         0.21052 | True      |                          0.16229 |                 89.56 |         0     | N/A              |
|   428 | P    |         0.19123 | True      |                          0.39981 |                 87.34 |         0     | N/A              |
|   429 | I    |         0.10013 | False     |                          0.14159 |                 88.08 |         0     | N/A              |
|   430 | K    |         0.19597 | True      |                          0.73166 |                 91.15 |         0     | N/A              |
|   431 | V    |         0.09328 | False     |                          0.12802 |                 93.26 |         0     | N/A              |
|   432 | N    |         0.1583  | True      |                          0.67856 |                 94.32 |         0     | N/A              |
|   433 | L    |         0.1388  | False     |                          0.4302  |                 92.87 |         0     | N/A              |
|   434 | A    |         0.0444  | False     |                          0.62274 |                 94.42 |         0     | N/A              |
|   435 | L    |         0.0338  | False     |                          0.37013 |                 94.27 |         0     | N/A              |
|   436 | P    |         0.00601 | False     |                          0       |                 95.21 |         1.11  | N/A              |
|   437 | V    |         0.02817 | False     |                          0.43555 |                 95.34 |        91.622 | N/A              |
|   438 | F    |         0.01649 | False     |                          0.61273 |                 95.32 |        99.313 | N/A              |
|   439 | F    |         0.00384 | False     |                          0.00064 |                 95.41 |        99.94  | N/A              |
|   440 | I    |         0.04727 | False     |                          0.096   |                 95.68 |        99.991 | N/A              |
|   441 | L    |         0.02132 | False     |                          0.68075 |                 95.66 |        99.996 | N/A              |
|   442 | A    |         0.00928 | False     |                          0.2411  |                 94.54 |        99.996 | N/A              |
|   443 | C    |         0.00204 | False     |                          0       |                 94.1  |        99.996 | N/A              |
|   444 | L    |         0.02124 | False     |                          0.48924 |                 94.04 |        99.997 | N/A              |
|   445 | F    |         0.05375 | False     |                          0.53852 |                 93.57 |        99.997 | N/A              |
|   446 | L    |         0.00887 | False     |                          0.03792 |                 91.52 |        99.983 | N/A              |
|   447 | I    |         0.02584 | False     |                          0.0632  |                 91.07 |        99.908 | N/A              |
|   448 | A    |         0.01665 | False     |                          0.56935 |                 92.52 |        99.09  | N/A              |
|   449 | V    |         0.0308  | False     |                          0.1133  |                 90.79 |        98.399 | N/A              |
|   450 | S    |         0.00782 | False     |                          0.01144 |                 86.93 |        90.262 | N/A              |
|   451 | F    |         0.05076 | False     |                          0.44771 |                 88.45 |        89.252 | N/A              |
|   452 | W    |         0.18473 | True      |                          0.82268 |                 89    |        84.725 | N/A              |
|   453 | K    |         0.19389 | True      |                          0.46128 |                 87.16 |         0     | N/A              |
|   454 | T    |         0.12314 | False     |                          0.17241 |                 84.68 |         0     | N/A              |
|   455 | P    |         0.14285 | False     |                          0.56617 |                 90.34 |         0     | N/A              |
|   456 | V    |         0.15898 | True      |                          0.76989 |                 90.28 |         0     | N/A              |
|   457 | E    |         0.05986 | False     |                          0.19879 |                 87.32 |         0     | N/A              |
|   458 | C    |         0.01613 | False     |                          0.02189 |                 87.77 |         0.287 | N/A              |
|   459 | G    |         0.03406 | False     |                          0.42859 |                 91.46 |         1.665 | N/A              |
|   460 | I    |         0.07917 | False     |                          0.57693 |                 91    |        43.934 | N/A              |
|   461 | G    |         0.00545 | False     |                          0       |                 89.56 |        48.048 | N/A              |
|   462 | F    |         0.02242 | False     |                          0.31404 |                 92.35 |        87.409 | N/A              |
|   463 | T    |         0.02762 | False     |                          0.62813 |                 94.02 |        87.789 | N/A              |
|   464 | I    |         0.03065 | False     |                          0.27199 |                 92.87 |        87.837 | N/A              |
|   465 | I    |         0.01796 | False     |                          0.1096  |                 92.93 |        87.289 | N/A              |
|   466 | L    |         0.0355  | False     |                          0.64137 |                 94.41 |        80.683 | N/A              |
|   467 | S    |         0.01309 | False     |                          0.38401 |                 95.74 |         9.908 | N/A              |
|   468 | G    |         0.00293 | False     |                          0       |                 94.45 |         0.778 | N/A              |
|   469 | L    |         0.05336 | False     |                          0.30171 |                 95.16 |         0     | N/A              |
|   470 | P    |         0.09168 | False     |                          0.62905 |                 95.17 |         1.148 | N/A              |
|   471 | V    |         0.02401 | False     |                          0.42934 |                 94.28 |        90.124 | N/A              |
|   472 | Y    |         0.06558 | False     |                          0.07895 |                 94.51 |        97.649 | N/A              |
|   473 | F    |         0.19393 | True      |                          0.48353 |                 94.13 |        98.638 | N/A              |
|   474 | F    |         0.13876 | False     |                          0.48607 |                 92.7  |        98.703 | N/A              |
|   475 | G    |         0.14699 | True      |                          0.43695 |                 90.33 |        98.645 | N/A              |
|   476 | V    |         0.07346 | False     |                          0.12178 |                 88.24 |        98.213 | N/A              |
|   477 | W    |         0.22873 | True      |                          0.7918  |                 90.31 |        92.704 | N/A              |
|   478 | W    |         0.26399 | True      |                          0.40108 |                 90.77 |        74.654 | N/A              |
|   479 | K    |         0.36379 | True      |                          0.77925 |                 83.69 |         0     | N/A              |
|   480 | N    |         0.31101 | True      |                          0.85552 |                 87.35 |         0     | N/A              |
|   481 | K    |         0.16974 | True      |                          0.15504 |                 88.87 |         0     | N/A              |
|   482 | P    |         0.22019 | True      |                          0.32904 |                 90.89 |         0     | N/A              |
|   483 | K    |         0.31514 | True      |                          0.88923 |                 90.89 |         0     | N/A              |
|   484 | W    |         0.23661 | True      |                          0.82242 |                 93.96 |         5.349 | N/A              |
|   485 | L    |         0.07242 | False     |                          0.15415 |                 92.2  |         6.417 | N/A              |
|   486 | L    |         0.14387 | False     |                          0.53321 |                 90.81 |         6.814 | N/A              |
|   487 | Q    |         0.2458  | True      |                          0.56258 |                 93.08 |         6.814 | N/A              |
|   488 | G    |         0.11325 | False     |                          0.39565 |                 93.7  |         8.508 | N/A              |
|   489 | I    |         0.11624 | False     |                          0.45983 |                 91.82 |        27.587 | N/A              |
|   490 | F    |         0.21179 | True      |                          0.65508 |                 93.28 |        29.31  | N/A              |
|   491 | S    |         0.15894 | True      |                          0.42712 |                 94.92 |        28.183 | N/A              |
|   492 | T    |         0.05371 | False     |                          0.57388 |                 94.75 |        28.07  | N/A              |
|   493 | T    |         0.0508  | False     |                          0.16293 |                 93.98 |        28.07  | N/A              |
|   494 | V    |         0.11844 | False     |                          0.28372 |                 94.51 |        27.819 | N/A              |
|   495 | L    |         0.17146 | True      |                          0.71931 |                 95.78 |        23.912 | N/A              |
|   496 | C    |         0.02705 | False     |                          0.24808 |                 94.76 |         2.187 | N/A              |
|   497 | Q    |         0.14001 | False     |                          0.20074 |                 93.81 |         0     | N/A              |
|   498 | K    |         0.31732 | True      |                          0.7924  |                 94.4  |         0     | N/A              |
|   499 | L    |         0.12565 | False     |                          0.86523 |                 95.4  |         0     | N/A              |
|   500 | M    |         0.10585 | False     |                          0.27675 |                 93.26 |         0     | N/A              |
|   501 | Q    |         0.17283 | True      |                          0.48774 |                 94.3  |         0     | N/A              |
|   502 | V    |         0.04411 | False     |                          0.04713 |                 92.87 |         0     | N/A              |
|   503 | V    |         0.25722 | True      |                          0.49032 |                 91.32 |         0     | N/A              |
|   504 | P    |         0.21889 | True      |                          0.60695 |                 87.75 |         0     | N/A              |
|   505 | Q    |         0.22978 | True      |                          0.41609 |                 77.66 |         0     | N/A              |
|   506 | E    |         0.32782 | True      |                          0.94297 |                 73.01 |         0     | N/A              |
|   507 | T    |         0.13638 | False     |                          1.38131 |                 54.06 |         0     | N/A              |


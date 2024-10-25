# Detailed Data for Q9Y6M1


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: Q9Y6M1
- **Gene Name**: IGF2BP2
- **Protein Name**: Insulin-like growth factor 2 mRNA-binding protein 2 / IMP2
- **Swiss Prot**: IF2B2_HUMAN
- **Family**: translation regulator
- **Biomarker Application**:  
- **Number of Isoforms**: 0
- **Regulation**: 2
- **(transcriptomics) AUC**: nan
- **(transcriptomics) Fold Change**: nan
- **(transcriptomics) Regulation**: Downregulated
- **Discotope Epitope Count**: 130
- **Max n_uniprots (Homo)**: 1
- **Max n_uniprots (Hetero)**: 5


## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| IGF2BP2           | HMGA2             |   0.996 |
| IGF2BP2           | IGF2              |   0.994 |
| IGF2BP2           | FTO               |   0.914 |
| IGF2BP2           | HHEX              |   0.908 |

## Homologs

| uniprot_id   | gene_id   |
|:-------------|:----------|
| Q9UNW9       | NOVA2     |
| Q53SS8       | PCBP1     |
| O00425       | IGF2BP3   |
| C9J0A4       | PCBP4     |
| A0A8V8TNQ2   | FUBP3     |
| E9PFP8       | PCBP3     |
| F8VRH0       | PCBP2     |
| A0A994J6T5   | HNRNPK    |
| H0YHZ1       | NOVA1     |
| M0R263       | KHSRP     |
| Q9NZI8       | IGF2BP1   |
| Q96AE4       | FUBP1     |

## Biological Assemblies

|   Unnamed: 0 |   assembly |   n_uniprots | composition   | crystal_id   |
|-------------:|-----------:|-------------:|:--------------|:-------------|
|            0 |          1 |            1 | Homo          | 6rol         |
|            1 |          2 |            1 | Homo          | 6rol         |
|            2 |          3 |            1 | Homo          | 6rol         |
|            3 |          4 |            1 | Homo          | 6rol         |
|            0 |          1 |            5 | Hetero        | 7q99         |
|            0 |          1 |            3 | Hetero        | 7q98         |
|            1 |          2 |            3 | Hetero        | 7q98         |
|            2 |          3 |            3 | Hetero        | 7q98         |
|            3 |          4 |            3 | Hetero        | 7q98         |
|            4 |          5 |            3 | Hetero        | 7q98         |
|            0 |          1 |            1 | Homo          | 2cqh         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification       |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:-------------------|
|     1 | M    |         0.08932 | False     |                          1.24612 |                 43.06 |         0     | N-acetylmethionine |
|     2 | M    |         0.08654 | False     |                          0.91511 |                 53.53 |         0     | N/A                |
|     3 | N    |         0.05735 | False     |                          0.17696 |                 72.08 |         0     | N/A                |
|     4 | K    |         0.05147 | False     |                          0.32824 |                 83.99 |         0     | N/A                |
|     5 | L    |         0.00699 | False     |                          0       |                 86.77 |         0     | N/A                |
|     6 | Y    |         0.04357 | False     |                          0.28167 |                 87.64 |         0     | N/A                |
|     7 | I    |         0.00322 | False     |                          0       |                 89.5  |         0     | N/A                |
|     8 | G    |         0.02207 | False     |                          0.01609 |                 87.45 |         0     | N/A                |
|     9 | N    |         0.05241 | False     |                          0.40204 |                 88.75 |         0     | N/A                |
|    10 | L    |         0.01117 | False     |                          0.01369 |                 87.74 |         0     | N/A                |
|    11 | S    |         0.04137 | False     |                          0.12808 |                 86.25 |         0     | Phosphoserine      |
|    12 | P    |         0.13457 | True      |                          0.79208 |                 83.12 |         0     | N/A                |
|    13 | A    |         0.08717 | False     |                          0.63004 |                 86.51 |         0     | N/A                |
|    14 | V    |         0.02671 | False     |                          0.04997 |                 87.63 |         0     | N/A                |
|    15 | T    |         0.1038  | False     |                          0.4773  |                 89.84 |         0     | N/A                |
|    16 | A    |         0.07153 | False     |                          0.33933 |                 87.04 |         0     | N/A                |
|    17 | D    |         0.19505 | True      |                          0.6263  |                 88.5  |         0     | N/A                |
|    18 | D    |         0.16312 | True      |                          0.22369 |                 89.76 |         0     | N/A                |
|    19 | L    |         0.00327 | False     |                          0       |                 88.84 |         0     | N/A                |
|    20 | R    |         0.18406 | True      |                          0.42802 |                 88.6  |         0     | N/A                |
|    21 | Q    |         0.19342 | True      |                          0.60716 |                 89.1  |         0     | N/A                |
|    22 | L    |         0.04774 | False     |                          0.14226 |                 89.22 |         0     | N/A                |
|    23 | F    |         0.00698 | False     |                          0.00137 |                 88.31 |         0     | N/A                |
|    24 | G    |         0.10709 | False     |                          0.56337 |                 87.36 |         0     | N/A                |
|    25 | D    |         0.20475 | True      |                          0.64119 |                 88.27 |         0     | N/A                |
|    26 | R    |         0.1688  | True      |                          0.49921 |                 86.78 |         0     | N/A                |
|    27 | K    |         0.24901 | True      |                          0.85005 |                 86.58 |         0     | N/A                |
|    28 | L    |         0.02562 | False     |                          0.06436 |                 85.61 |         0     | N/A                |
|    29 | P    |         0.15821 | True      |                          0.36938 |                 83.62 |         0     | N/A                |
|    30 | L    |         0.0884  | False     |                          0.27221 |                 81.96 |         0.131 | N/A                |
|    31 | A    |         0.1925  | True      |                          0.40558 |                 73.31 |         0.131 | N/A                |
|    32 | G    |         0.11041 | False     |                          0.57912 |                 72.23 |         0.131 | N/A                |
|    33 | Q    |         0.2244  | True      |                          0.67263 |                 76.08 |         0.131 | N/A                |
|    34 | V    |         0.08925 | False     |                          0.108   |                 86    |         0.284 | N/A                |
|    35 | L    |         0.09344 | False     |                          0.52807 |                 86.03 |         0.284 | N/A                |
|    36 | L    |         0.10594 | False     |                          0.3591  |                 87.82 |         0.284 | N/A                |
|    37 | K    |         0.16153 | True      |                          0.61385 |                 84.78 |         0.153 | N/A                |
|    38 | S    |         0.15599 | True      |                          0.75669 |                 81.99 |         0.889 | N/A                |
|    39 | G    |         0.05588 | False     |                          0.30176 |                 83.26 |         6.829 | N/A                |
|    40 | Y    |         0.0452  | False     |                          0.29224 |                 90.23 |         6.829 | N/A                |
|    41 | A    |         0.00383 | False     |                          0       |                 90.24 |         6.829 | N/A                |
|    42 | F    |         0.04141 | False     |                          0.25134 |                 89.87 |         6.829 | N/A                |
|    43 | V    |         0.01033 | False     |                          0.00666 |                 89.07 |         6.829 | N/A                |
|    44 | D    |         0.0302  | False     |                          0.14035 |                 86.17 |         0.153 | N/A                |
|    45 | Y    |         0.01683 | False     |                          0.01936 |                 84.05 |         0     | N/A                |
|    46 | P    |         0.1085  | False     |                          0.54931 |                 77.39 |         0     | N/A                |
|    47 | D    |         0.1518  | True      |                          0.34586 |                 76.3  |         0     | N/A                |
|    48 | Q    |         0.16565 | True      |                          0.5468  |                 74.61 |         0     | N/A                |
|    49 | N    |         0.16375 | True      |                          0.67346 |                 75.35 |         0     | N/A                |
|    50 | W    |         0.06951 | False     |                          0.35096 |                 86.91 |         0     | N/A                |
|    51 | A    |         0.00318 | False     |                          0       |                 82.86 |         0     | N/A                |
|    52 | I    |         0.16369 | True      |                          0.40318 |                 78.19 |         0     | N/A                |
|    53 | R    |         0.21698 | True      |                          0.56235 |                 85.02 |         0     | N/A                |
|    54 | A    |         0.00495 | False     |                          0       |                 86.37 |         0     | N/A                |
|    55 | I    |         0.09593 | False     |                          0.19394 |                 83.43 |         0     | N/A                |
|    56 | E    |         0.13752 | True      |                          0.53576 |                 84.74 |         0     | N/A                |
|    57 | T    |         0.07118 | False     |                          0.3484  |                 87.69 |         0     | N/A                |
|    58 | L    |         0.00368 | False     |                          0       |                 89.26 |         0     | N/A                |
|    59 | S    |         0.10654 | False     |                          0.27826 |                 86.64 |         0     | N/A                |
|    60 | G    |         0.05815 | False     |                          0.59805 |                 85.64 |         0     | N/A                |
|    61 | K    |         0.20929 | True      |                          0.73456 |                 87.16 |         0     | N/A                |
|    62 | V    |         0.05058 | False     |                          0.05983 |                 87.26 |         0     | N/A                |
|    63 | E    |         0.10564 | False     |                          0.57496 |                 87.89 |         0     | N/A                |
|    64 | L    |         0.08774 | False     |                          0.13269 |                 85.88 |         0     | N/A                |
|    65 | H    |         0.16751 | True      |                          0.50376 |                 85.7  |         0     | N/A                |
|    66 | G    |         0.11601 | False     |                          0.75606 |                 82.84 |         0     | N/A                |
|    67 | K    |         0.0962  | False     |                          0.40646 |                 84.79 |         0     | N/A                |
|    68 | I    |         0.13689 | True      |                          0.5554  |                 87.02 |         0     | N/A                |
|    69 | M    |         0.00782 | False     |                          0.00144 |                 87.74 |         0     | N/A                |
|    70 | E    |         0.02887 | False     |                          0.53408 |                 84.7  |         0     | N/A                |
|    71 | V    |         0.0144  | False     |                          0.02427 |                 87.78 |         0     | N/A                |
|    72 | D    |         0.07146 | False     |                          0.41535 |                 80.33 |         0     | N/A                |
|    73 | Y    |         0.10328 | False     |                          0.32901 |                 78.69 |         0     | N/A                |
|    74 | S    |         0.09094 | False     |                          0.22821 |                 69.88 |         0     | N/A                |
|    75 | V    |         0.07521 | False     |                          0.22161 |                 56.34 |         0     | N/A                |
|    76 | S    |         0.10972 | False     |                          0.54003 |                 47.38 |         0     | N/A                |
|    77 | K    |         0.08917 | False     |                          0.88482 |                 45.63 |         0     | N/A                |
|    78 | K    |         0.10016 | False     |                          0.67931 |                 43.26 |         0     | N/A                |
|    79 | L    |         0.06282 | False     |                          0.50569 |                 49.97 |         0     | N/A                |
|    80 | R    |         0.07565 | False     |                          0.54501 |                 54.54 |         0     | N/A                |
|    81 | S    |         0.0207  | False     |                          0.0162  |                 67.05 |         0     | N/A                |
|    82 | R    |         0.04833 | False     |                          0.37048 |                 85.46 |         0     | N/A                |
|    83 | K    |         0.05228 | False     |                          0.38618 |                 85.31 |         0     | N/A                |
|    84 | I    |         0.00464 | False     |                          0       |                 88.13 |         0     | N/A                |
|    85 | Q    |         0.02727 | False     |                          0.11364 |                 87.51 |         0     | N/A                |
|    86 | I    |         0.00267 | False     |                          0.0008  |                 89.63 |         0     | N/A                |
|    87 | R    |         0.14526 | True      |                          0.50408 |                 88.27 |         0     | N/A                |
|    88 | N    |         0.03817 | False     |                          0.23943 |                 87.05 |         0     | N/A                |
|    89 | I    |         0.0168  | False     |                          0.0256  |                 86.72 |         0     | N/A                |
|    90 | P    |         0.01797 | False     |                          0.00955 |                 84.44 |         0     | N/A                |
|    91 | P    |         0.1984  | True      |                          0.66919 |                 78.91 |         0     | N/A                |
|    92 | H    |         0.19552 | True      |                          0.5526  |                 81.85 |         0     | N/A                |
|    93 | L    |         0.06589 | False     |                          0.13954 |                 83.28 |         0     | N/A                |
|    94 | Q    |         0.21018 | True      |                          0.62888 |                 81.68 |         0     | N/A                |
|    95 | W    |         0.15045 | True      |                          0.49014 |                 80.92 |         0     | N/A                |
|    96 | E    |         0.10593 | False     |                          0.6486  |                 81.16 |         0     | N/A                |
|    97 | V    |         0.14109 | True      |                          0.53701 |                 84.95 |         0     | N/A                |
|    98 | L    |         0.00969 | False     |                          0.02555 |                 86.67 |         0     | N/A                |
|    99 | D    |         0.05916 | False     |                          0.38252 |                 83.48 |         0     | N/A                |
|   100 | G    |         0.09419 | False     |                          0.44436 |                 85.86 |         0     | N/A                |
|   101 | L    |         0.05345 | False     |                          0.12708 |                 87.54 |         0     | N/A                |
|   102 | L    |         0.00692 | False     |                          0.00412 |                 90.45 |         0     | N/A                |
|   103 | A    |         0.07233 | False     |                          0.60703 |                 88.44 |         0     | N/A                |
|   104 | Q    |         0.1895  | True      |                          0.64708 |                 88.17 |         0     | N/A                |
|   105 | Y    |         0.09664 | False     |                          0.17293 |                 88.27 |         0     | N/A                |
|   106 | G    |         0.01736 | False     |                          0.20202 |                 85.6  |         0     | N/A                |
|   107 | T    |         0.07368 | False     |                          0.61679 |                 88.05 |         0     | N/A                |
|   108 | V    |         0.027   | False     |                          0.26852 |                 88.02 |         0     | N/A                |
|   109 | E    |         0.05843 | False     |                          0.51514 |                 86.7  |         0     | N/A                |
|   110 | N    |         0.07452 | False     |                          0.52433 |                 84.98 |         0     | N/A                |
|   111 | V    |         0.06952 | False     |                          0.26729 |                 87.52 |         0     | N/A                |
|   112 | E    |         0.05675 | False     |                          0.28809 |                 82.6  |         0     | N/A                |
|   113 | Q    |         0.0838  | False     |                          0.61428 |                 84.68 |         0     | N/A                |
|   114 | V    |         0.04939 | False     |                          0.31849 |                 81.66 |         0     | N/A                |
|   115 | N    |         0.15936 | True      |                          0.91467 |                 76.27 |         0     | N/A                |
|   116 | T    |         0.11179 | False     |                          0.32212 |                 75.89 |         0     | N/A                |
|   117 | D    |         0.25737 | True      |                          0.93516 |                 74.81 |         0     | N/A                |
|   118 | T    |         0.18178 | True      |                          0.55448 |                 74.57 |         0     | N/A                |
|   119 | E    |         0.17344 | True      |                          0.8452  |                 81.38 |         0     | N/A                |
|   120 | T    |         0.0521  | False     |                          0.13847 |                 84.73 |         8.451 | N/A                |
|   121 | A    |         0.05115 | False     |                          0.19153 |                 84.17 |        22.702 | N/A                |
|   122 | V    |         0.01498 | False     |                          0.0676  |                 87.52 |        37.18  | N/A                |
|   123 | V    |         0.00749 | False     |                          0.00952 |                 89.89 |        38.289 | N/A                |
|   124 | N    |         0.0368  | False     |                          0.16664 |                 90.88 |        38.289 | N/A                |
|   125 | V    |         0.00252 | False     |                          0.00177 |                 90.12 |        39.522 | N/A                |
|   126 | T    |         0.02688 | False     |                          0.1089  |                 89.96 |        38.34  | N/A                |
|   127 | Y    |         0.00544 | False     |                          0       |                 89.69 |        36.206 | N/A                |
|   128 | A    |         0.03513 | False     |                          0.31531 |                 83.81 |        28.5   | N/A                |
|   129 | T    |         0.06247 | False     |                          0.42097 |                 82.9  |        11.73  | N/A                |
|   130 | R    |         0.04553 | False     |                          0.36112 |                 79.99 |         0     | N/A                |
|   131 | E    |         0.12284 | False     |                          0.55929 |                 79.65 |         0     | N/A                |
|   132 | E    |         0.03732 | False     |                          0.17033 |                 88.31 |         0     | N/A                |
|   133 | A    |         0.00181 | False     |                          0       |                 85.62 |         0     | N/A                |
|   134 | K    |         0.0649  | False     |                          0.53234 |                 82.83 |         0     | N/A                |
|   135 | I    |         0.07993 | False     |                          0.47998 |                 85.18 |         0     | N/A                |
|   136 | A    |         0.00231 | False     |                          0       |                 87.53 |         0     | N/A                |
|   137 | M    |         0.01874 | False     |                          0.19565 |                 84.14 |         0     | N/A                |
|   138 | E    |         0.11152 | False     |                          0.53986 |                 79.91 |         0     | N/A                |
|   139 | K    |         0.13275 | True      |                          0.6336  |                 84.43 |         0     | N/A                |
|   140 | L    |         0.00396 | False     |                          0.00082 |                 82.41 |         0     | N/A                |
|   141 | S    |         0.10913 | False     |                          0.50742 |                 72    |         0     | N/A                |
|   142 | G    |         0.06431 | False     |                          0.58229 |                 67.3  |         0     | N/A                |
|   143 | H    |         0.13853 | True      |                          0.32027 |                 74.84 |         0     | N/A                |
|   144 | Q    |         0.17191 | True      |                          0.65573 |                 71.55 |         0     | N/A                |
|   145 | F    |         0.15762 | True      |                          0.30379 |                 71.91 |         0     | N/A                |
|   146 | E    |         0.2528  | True      |                          0.59634 |                 74.49 |         0     | N/A                |
|   147 | N    |         0.18799 | True      |                          0.95931 |                 79.36 |         0     | N/A                |
|   148 | Y    |         0.09231 | False     |                          0.28762 |                 81.67 |         0     | N/A                |
|   149 | S    |         0.07857 | False     |                          0.31417 |                 82.46 |         0     | N/A                |
|   150 | F    |         0.01423 | False     |                          0.02042 |                 84.64 |         0     | N/A                |
|   151 | K    |         0.04948 | False     |                          0.6705  |                 81.15 |         0     | N/A                |
|   152 | I    |         0.05338 | False     |                          0.15361 |                 85.33 |         0     | N/A                |
|   153 | S    |         0.04984 | False     |                          0.39937 |                 78.92 |         0     | N/A                |
|   154 | Y    |         0.06686 | False     |                          0.13037 |                 77.5  |         0     | N/A                |
|   155 | I    |         0.09608 | False     |                          0.23759 |                 70.93 |         0     | N/A                |
|   156 | P    |         0.05328 | False     |                          0.51969 |                 55.83 |         0     | N/A                |
|   157 | D    |         0.04924 | False     |                          0.34564 |                 55.42 |         0     | N/A                |
|   158 | E    |         0.12314 | False     |                          0.91648 |                 47.27 |         0     | N/A                |
|   159 | E    |         0.11226 | False     |                          0.68765 |                 39.83 |         0     | N/A                |
|   160 | V    |         0.0768  | False     |                          0.91965 |                 33.55 |         0     | N/A                |
|   161 | S    |         0.10803 | False     |                          0.83888 |                 31.07 |         0     | N/A                |
|   162 | S    |         0.1076  | False     |                          0.69977 |                 30.74 |         0     | Phosphoserine      |
|   163 | P    |         0.10594 | False     |                          0.96449 |                 35.98 |         0     | N/A                |
|   164 | S    |         0.09877 | False     |                          0.77166 |                 34.28 |         0     | Phosphoserine      |
|   165 | P    |         0.07044 | False     |                          0.85642 |                 36.15 |         0     | N/A                |
|   166 | P    |         0.09935 | False     |                          0.94011 |                 42.53 |         0     | N/A                |
|   167 | Q    |         0.13276 | True      |                          0.93394 |                 40.2  |         0     | N/A                |
|   168 | R    |         0.15178 | True      |                          0.95071 |                 37.25 |         0     | N/A                |
|   169 | A    |         0.16649 | True      |                          0.96129 |                 37.99 |         0     | N/A                |
|   170 | Q    |         0.11903 | False     |                          0.87711 |                 35.65 |         0     | N/A                |
|   171 | R    |         0.15121 | True      |                          0.97367 |                 39.66 |         0     | N/A                |
|   172 | G    |         0.06443 | False     |                          0.86989 |                 35.34 |         0     | N/A                |
|   173 | D    |         0.1318  | True      |                          0.82077 |                 36.87 |         0     | N/A                |
|   174 | H    |         0.11921 | False     |                          0.86811 |                 41.57 |         0     | N/A                |
|   175 | S    |         0.10877 | False     |                          0.71665 |                 41.63 |         0     | N/A                |
|   176 | S    |         0.15683 | True      |                          0.78077 |                 42.37 |         0     | N/A                |
|   177 | R    |         0.17833 | True      |                          0.8658  |                 39.23 |         0     | N/A                |
|   178 | E    |         0.10278 | False     |                          0.73462 |                 38.52 |         0     | N/A                |
|   179 | Q    |         0.06646 | False     |                          0.91765 |                 38.83 |         0     | N/A                |
|   180 | G    |         0.07648 | False     |                          0.9362  |                 36.48 |         0     | N/A                |
|   181 | H    |         0.09935 | False     |                          1.03915 |                 35.84 |         0     | N/A                |
|   182 | A    |         0.11773 | False     |                          0.95054 |                 38.39 |         0     | N/A                |
|   183 | P    |         0.14308 | True      |                          0.96738 |                 36.79 |         0     | N/A                |
|   184 | G    |         0.15923 | True      |                          1.02483 |                 29.35 |         0     | N/A                |
|   185 | G    |         0.11277 | False     |                          0.88535 |                 30.46 |         0     | N/A                |
|   186 | T    |         0.10359 | False     |                          0.90442 |                 31.53 |         0     | N/A                |
|   187 | S    |         0.08329 | False     |                          0.92563 |                 32.04 |         0     | N/A                |
|   188 | Q    |         0.08945 | False     |                          0.8506  |                 34    |         0     | N/A                |
|   189 | A    |         0.07937 | False     |                          0.87638 |                 40.73 |         0     | N/A                |
|   190 | R    |         0.1216  | False     |                          0.90863 |                 47.36 |         0     | N/A                |
|   191 | Q    |         0.10261 | False     |                          0.77603 |                 55.38 |         0     | N/A                |
|   192 | I    |         0.09498 | False     |                          0.35497 |                 62.64 |         0     | N/A                |
|   193 | D    |         0.04019 | False     |                          0.64294 |                 77.04 |         0     | N/A                |
|   194 | F    |         0.03908 | False     |                          0.17606 |                 88.5  |         0     | N/A                |
|   195 | P    |         0.02815 | False     |                          0.28288 |                 93.33 |         0     | N/A                |
|   196 | L    |         0.00249 | False     |                          0.00165 |                 96.3  |         0     | N/A                |
|   197 | R    |         0.03209 | False     |                          0.25145 |                 95.52 |         0     | N/A                |
|   198 | I    |         0.01385 | False     |                          0.0112  |                 96.73 |         0     | N/A                |
|   199 | L    |         0.03374 | False     |                          0.19487 |                 94.15 |         0     | N/A                |
|   200 | V    |         0.0023  | False     |                          0.00381 |                 94.18 |         0     | N/A                |
|   201 | P    |         0.03187 | False     |                          0.20776 |                 91.98 |         0     | N/A                |
|   202 | T    |         0.05872 | False     |                          0.39372 |                 89.72 |         0.819 | N/A                |
|   203 | Q    |         0.15822 | True      |                          0.49878 |                 89.96 |         2.197 | N/A                |
|   204 | F    |         0.03344 | False     |                          0.01656 |                 93.15 |        37.386 | N/A                |
|   205 | V    |         0.02009 | False     |                          0.04951 |                 92.84 |        39.882 | N/A                |
|   206 | G    |         0.09275 | False     |                          0.56017 |                 92.56 |        39.967 | N/A                |
|   207 | A    |         0.05058 | False     |                          0.241   |                 94.41 |        39.967 | N/A                |
|   208 | I    |         0.00372 | False     |                          0.0008  |                 95.3  |        39.967 | N/A                |
|   209 | I    |         0.09584 | False     |                          0.17279 |                 94.5  |        35.094 | N/A                |
|   210 | G    |         0.05134 | False     |                          0.21144 |                 92.83 |        14.14  | N/A                |
|   211 | K    |         0.22372 | True      |                          0.916   |                 93.18 |         0     | N/A                |
|   212 | E    |         0.29142 | True      |                          0.86194 |                 91.64 |         0     | N/A                |
|   213 | G    |         0.05595 | False     |                          0.14494 |                 92.25 |         0     | N/A                |
|   214 | L    |         0.22754 | True      |                          0.77737 |                 95.93 |         0     | N/A                |
|   215 | T    |         0.06468 | False     |                          0.28448 |                 96.53 |         0     | N/A                |
|   216 | I    |         0.03872 | False     |                          0.16399 |                 95.81 |         0     | N/A                |
|   217 | K    |         0.17241 | True      |                          0.6288  |                 96.01 |         0     | N/A                |
|   218 | N    |         0.11885 | False     |                          0.39159 |                 96.97 |         0     | N/A                |
|   219 | I    |         0.00771 | False     |                          0.004   |                 96.71 |         0     | N/A                |
|   220 | T    |         0.06686 | False     |                          0.3567  |                 95.72 |         0     | N/A                |
|   221 | K    |         0.18447 | True      |                          0.81823 |                 96.02 |         0     | N/A                |
|   222 | Q    |         0.13066 | True      |                          0.58457 |                 96.05 |         0     | N/A                |
|   223 | T    |         0.03868 | False     |                          0.06016 |                 95.39 |         0     | N/A                |
|   224 | Q    |         0.15698 | True      |                          0.83889 |                 94.08 |         0     | N/A                |
|   225 | S    |         0.0129  | False     |                          0.03861 |                 94.14 |         0     | N/A                |
|   226 | R    |         0.06132 | False     |                          0.62679 |                 94.34 |         0     | N/A                |
|   227 | V    |         0.02864 | False     |                          0.09685 |                 95.31 |         0     | N/A                |
|   228 | D    |         0.05669 | False     |                          0.26668 |                 92.95 |         0     | N/A                |
|   229 | I    |         0.10602 | False     |                          0.16424 |                 92.15 |         0     | N/A                |
|   230 | H    |         0.0895  | False     |                          0.34736 |                 86.34 |         0     | N/A                |
|   231 | R    |         0.23776 | True      |                          0.43287 |                 73.8  |         0     | N/A                |
|   232 | K    |         0.21088 | True      |                          0.94373 |                 60.08 |         0     | N/A                |
|   233 | E    |         0.15379 | True      |                          0.81168 |                 60.69 |         0     | N/A                |
|   234 | N    |         0.08302 | False     |                          0.28236 |                 59.2  |         0     | N/A                |
|   235 | S    |         0.0908  | False     |                          0.7636  |                 58.34 |         0     | N/A                |
|   236 | G    |         0.21767 | True      |                          0.95716 |                 64.13 |         0     | N/A                |
|   237 | A    |         0.16667 | True      |                          0.38203 |                 75.05 |         0     | N/A                |
|   238 | A    |         0.10056 | False     |                          0.80917 |                 84.33 |         0     | N/A                |
|   239 | E    |         0.10044 | False     |                          0.21731 |                 89.68 |         0     | N/A                |
|   240 | K    |         0.04337 | False     |                          0.13774 |                 89.21 |         0     | N/A                |
|   241 | P    |         0.01922 | False     |                          0.13022 |                 92.12 |         0     | N/A                |
|   242 | V    |         0.00244 | False     |                          0.00095 |                 95.04 |         0     | N/A                |
|   243 | T    |         0.01869 | False     |                          0.05522 |                 95.64 |         0     | N/A                |
|   244 | I    |         0.00291 | False     |                          0       |                 96.94 |         0     | N/A                |
|   245 | H    |         0.05071 | False     |                          0.30964 |                 94.48 |         0     | N/A                |
|   246 | A    |         0.01551 | False     |                          0.35353 |                 92.8  |         0     | N/A                |
|   247 | T    |         0.03153 | False     |                          0.48054 |                 94.08 |         0     | N/A                |
|   248 | P    |         0.02203 | False     |                          0.40481 |                 92.96 |         0     | N/A                |
|   249 | E    |         0.09721 | False     |                          0.64526 |                 94.07 |         0     | N/A                |
|   250 | G    |         0.02409 | False     |                          0.09958 |                 94.94 |         0     | N/A                |
|   251 | T    |         0.00317 | False     |                          0.02187 |                 94.94 |         0     | N/A                |
|   252 | S    |         0.01149 | False     |                          0.10965 |                 95.21 |         0     | N/A                |
|   253 | E    |         0.04949 | False     |                          0.32562 |                 96.84 |         0     | N/A                |
|   254 | A    |         0.00063 | False     |                          0       |                 97.26 |         0     | N/A                |
|   255 | C    |         0.00083 | False     |                          0.001   |                 97.39 |         0     | N/A                |
|   256 | R    |         0.07719 | False     |                          0.36518 |                 96.77 |         0     | N/A                |
|   257 | M    |         0.03768 | False     |                          0.14107 |                 97.2  |         0     | N/A                |
|   258 | I    |         0.0023  | False     |                          0       |                 96.92 |         0     | N/A                |
|   259 | L    |         0.01465 | False     |                          0.05014 |                 96.05 |         0     | N/A                |
|   260 | E    |         0.0968  | False     |                          0.36163 |                 95.38 |         0     | N/A                |
|   261 | I    |         0.06286 | False     |                          0.20562 |                 95.2  |         0     | N/A                |
|   262 | M    |         0.01656 | False     |                          0.01855 |                 94.26 |         0     | N/A                |
|   263 | Q    |         0.03635 | False     |                          0.23705 |                 92.97 |         0     | N/A                |
|   264 | K    |         0.12748 | True      |                          0.64502 |                 92.92 |         0     | N/A                |
|   265 | E    |         0.05755 | False     |                          0.27383 |                 92.48 |         0     | N/A                |
|   266 | A    |         0.00815 | False     |                          0.00377 |                 91.31 |         0     | N/A                |
|   267 | D    |         0.15358 | True      |                          0.56039 |                 90.06 |         0     | N/A                |
|   268 | E    |         0.14866 | True      |                          0.61919 |                 89.37 |         0     | N/A                |
|   269 | T    |         0.09401 | False     |                          0.41598 |                 86.71 |         0     | N/A                |
|   270 | K    |         0.18081 | True      |                          0.9292  |                 80.3  |         0     | N/A                |
|   271 | L    |         0.29994 | True      |                          0.66382 |                 69.4  |         0     | N/A                |
|   272 | A    |         0.12722 | True      |                          0.37632 |                 67.33 |         0     | N/A                |
|   273 | E    |         0.20657 | True      |                          0.93392 |                 69.34 |         0     | N/A                |
|   274 | E    |         0.10104 | False     |                          0.46993 |                 80.43 |         0     | N/A                |
|   275 | I    |         0.04134 | False     |                          0.09886 |                 88.55 |         0     | N/A                |
|   276 | P    |         0.03191 | False     |                          0.25665 |                 93.53 |         0     | N/A                |
|   277 | L    |         0.00548 | False     |                          0.01884 |                 97.03 |         0     | N/A                |
|   278 | K    |         0.01715 | False     |                          0.22333 |                 96.99 |         0     | N/A                |
|   279 | I    |         0.00278 | False     |                          0.0024  |                 97.43 |         0     | N/A                |
|   280 | L    |         0.02146 | False     |                          0.11613 |                 93.77 |         0     | N/A                |
|   281 | A    |         0.01438 | False     |                          0.05102 |                 92.63 |         0     | N/A                |
|   282 | H    |         0.0987  | False     |                          0.50183 |                 86.56 |         0     | N/A                |
|   283 | N    |         0.01147 | False     |                          0.01292 |                 83.03 |         0     | N/A                |
|   284 | G    |         0.05036 | False     |                          0.21595 |                 80.73 |         0     | N/A                |
|   285 | L    |         0.02758 | False     |                          0.08799 |                 88.45 |         0     | N/A                |
|   286 | V    |         0.0027  | False     |                          0       |                 89.55 |         0     | N/A                |
|   287 | G    |         0.04698 | False     |                          0.23071 |                 84.12 |         0     | N/A                |
|   288 | R    |         0.05483 | False     |                          0.37641 |                 87.02 |         0     | N/A                |
|   289 | L    |         0.00649 | False     |                          0.00142 |                 91.97 |         0     | N/A                |
|   290 | I    |         0.07659 | False     |                          0.26319 |                 88.77 |         0     | N/A                |
|   291 | G    |         0.05027 | False     |                          0.17008 |                 82.23 |         0     | N/A                |
|   292 | K    |         0.17849 | True      |                          0.61042 |                 79.67 |         0     | N/A                |
|   293 | E    |         0.23066 | True      |                          0.75943 |                 81    |         0     | N/A                |
|   294 | G    |         0.05377 | False     |                          0.15183 |                 83.39 |         0     | N/A                |
|   295 | R    |         0.19822 | True      |                          0.66598 |                 89.49 |         0     | N/A                |
|   296 | N    |         0.04774 | False     |                          0.35196 |                 91.39 |         0     | N/A                |
|   297 | L    |         0.02464 | False     |                          0.14179 |                 92.75 |         0     | N/A                |
|   298 | K    |         0.14394 | True      |                          0.6385  |                 93.37 |         0     | N/A                |
|   299 | K    |         0.12575 | True      |                          0.58557 |                 95.28 |         0     | N/A                |
|   300 | I    |         0.02092 | False     |                          0.0312  |                 95.82 |         0     | N/A                |
|   301 | E    |         0.04295 | False     |                          0.13307 |                 95.68 |         0     | N/A                |
|   302 | H    |         0.18996 | True      |                          0.86534 |                 95.17 |         0     | N/A                |
|   303 | E    |         0.11436 | False     |                          0.52986 |                 95.91 |         0     | N/A                |
|   304 | T    |         0.04943 | False     |                          0.12551 |                 95.77 |         0     | N/A                |
|   305 | G    |         0.13191 | True      |                          0.78123 |                 94.96 |         0     | N/A                |
|   306 | T    |         0.0202  | False     |                          0.07419 |                 96.17 |         0     | N/A                |
|   307 | K    |         0.06385 | False     |                          0.57794 |                 96.23 |         0     | N/A                |
|   308 | I    |         0.02212 | False     |                          0.03134 |                 96.4  |         1.024 | N/A                |
|   309 | T    |         0.07739 | False     |                          0.46413 |                 94.3  |         1.024 | N/A                |
|   310 | I    |         0.07159 | False     |                          0.19787 |                 92.49 |         1.024 | N/A                |
|   311 | S    |         0.02867 | False     |                          0.23039 |                 88.73 |         1.024 | N/A                |
|   312 | S    |         0.08897 | False     |                          0.37626 |                 80.24 |         1.024 | N/A                |
|   313 | L    |         0.03591 | False     |                          0.18028 |                 73.65 |         1.024 | N/A                |
|   314 | Q    |         0.10188 | False     |                          0.43297 |                 66.95 |         0     | N/A                |
|   315 | D    |         0.11383 | False     |                          0.54949 |                 70.71 |         0     | N/A                |
|   316 | L    |         0.0244  | False     |                          0.03244 |                 64    |         0     | N/A                |
|   317 | S    |         0.04929 | False     |                          0.22965 |                 57.44 |         0     | N/A                |
|   318 | I    |         0.16434 | True      |                          0.5896  |                 52    |         0     | N/A                |
|   319 | Y    |         0.21648 | True      |                          0.75367 |                 50.95 |         0     | N/A                |
|   320 | N    |         0.10099 | False     |                          0.42969 |                 68.44 |         0     | N/A                |
|   321 | P    |         0.0661  | False     |                          0.41055 |                 73.7  |         0     | N/A                |
|   322 | E    |         0.03415 | False     |                          0.18509 |                 84.89 |         0     | N/A                |
|   323 | R    |         0.0167  | False     |                          0.08398 |                 89.67 |         0     | N/A                |
|   324 | T    |         0.02551 | False     |                          0.1716  |                 93.29 |         0     | N/A                |
|   325 | I    |         0.00231 | False     |                          0       |                 96.56 |         0     | N/A                |
|   326 | T    |         0.01657 | False     |                          0.14147 |                 96.74 |         0     | N/A                |
|   327 | V    |         0.00163 | False     |                          0       |                 97.58 |         0     | N/A                |
|   328 | K    |         0.04463 | False     |                          0.46725 |                 95.43 |         0     | N/A                |
|   329 | G    |         0.01799 | False     |                          0.29272 |                 92.92 |         0     | N/A                |
|   330 | T    |         0.03584 | False     |                          0.64135 |                 93.95 |         0     | N/A                |
|   331 | V    |         0.02156 | False     |                          0.18977 |                 93.8  |         0     | N/A                |
|   332 | E    |         0.10498 | False     |                          0.59741 |                 94.43 |         0     | N/A                |
|   333 | A    |         0.02348 | False     |                          0.1722  |                 96.1  |         0     | N/A                |
|   334 | C    |         0.00409 | False     |                          0.01704 |                 96.61 |         0     | N/A                |
|   335 | A    |         0.01171 | False     |                          0.09566 |                 95.71 |         0     | N/A                |
|   336 | S    |         0.03808 | False     |                          0.4002  |                 96.53 |         0     | N/A                |
|   337 | A    |         0.00086 | False     |                          0       |                 97.3  |         0     | N/A                |
|   338 | E    |         0.00131 | False     |                          0.00259 |                 97.4  |         0     | N/A                |
|   339 | I    |         0.04635 | False     |                          0.49358 |                 96.44 |         0     | N/A                |
|   340 | E    |         0.03891 | False     |                          0.24904 |                 96.36 |         0     | N/A                |
|   341 | I    |         0.00228 | False     |                          0       |                 96.97 |         0     | N/A                |
|   342 | M    |         0.00879 | False     |                          0.013   |                 95.41 |         0     | N/A                |
|   343 | K    |         0.06373 | False     |                          0.4729  |                 94.38 |         0     | N/A                |
|   344 | K    |         0.04483 | False     |                          0.31898 |                 93.53 |         0     | N/A                |
|   345 | L    |         0.00652 | False     |                          0.00824 |                 94.02 |         0     | N/A                |
|   346 | R    |         0.03018 | False     |                          0.17461 |                 92.88 |         0     | N/A                |
|   347 | E    |         0.0416  | False     |                          0.32372 |                 91.16 |         0     | N/A                |
|   348 | A    |         0.01401 | False     |                          0.02716 |                 87.89 |         0     | N/A                |
|   349 | F    |         0.04662 | False     |                          0.36829 |                 88.73 |         0     | N/A                |
|   350 | E    |         0.03124 | False     |                          0.37281 |                 87.09 |         0     | N/A                |
|   351 | N    |         0.06931 | False     |                          0.55298 |                 84.48 |         0     | N/A                |
|   352 | D    |         0.05904 | False     |                          0.35161 |                 77.69 |         0     | N/A                |
|   353 | M    |         0.04571 | False     |                          0.41079 |                 76.76 |         0     | N/A                |
|   354 | L    |         0.06727 | False     |                          0.54242 |                 77.7  |         0     | N/A                |
|   355 | A    |         0.06398 | False     |                          0.52866 |                 70.02 |         0     | N/A                |
|   356 | V    |         0.11679 | False     |                          0.77225 |                 62.56 |         0     | N/A                |
|   357 | N    |         0.08934 | False     |                          0.4916  |                 56.89 |         0     | N/A                |
|   358 | Q    |         0.09896 | False     |                          0.56683 |                 53.94 |         0     | N/A                |
|   359 | Q    |         0.0872  | False     |                          0.518   |                 46.28 |         0     | N/A                |
|   360 | A    |         0.10823 | False     |                          0.73749 |                 42.38 |         0     | N/A                |
|   361 | N    |         0.15044 | True      |                          0.79731 |                 41.14 |         0     | N/A                |
|   362 | L    |         0.15418 | True      |                          0.86257 |                 39.59 |         0     | N/A                |
|   363 | I    |         0.13521 | True      |                          0.4881  |                 38.99 |         0     | N/A                |
|   364 | P    |         0.16843 | True      |                          1.00202 |                 34.92 |         0     | N/A                |
|   365 | G    |         0.16237 | True      |                          1.02911 |                 40.17 |         0     | N/A                |
|   366 | L    |         0.16767 | True      |                          0.52679 |                 39.12 |         0.555 | N/A                |
|   367 | N    |         0.08692 | False     |                          0.64855 |                 42.06 |         0.555 | N/A                |
|   368 | L    |         0.08177 | False     |                          0.30872 |                 43.12 |         3.733 | N/A                |
|   369 | S    |         0.05622 | False     |                          0.82293 |                 38.22 |         4.105 | N/A                |
|   370 | A    |         0.10572 | False     |                          0.79827 |                 38    |         8.725 | N/A                |
|   371 | L    |         0.10039 | False     |                          0.60877 |                 40.94 |        10.768 | N/A                |
|   372 | G    |         0.10461 | False     |                          0.89034 |                 32.63 |        10.955 | N/A                |
|   373 | I    |         0.12784 | True      |                          0.69757 |                 45.9  |        13.695 | N/A                |
|   374 | F    |         0.08885 | False     |                          0.56607 |                 38.04 |        13.721 | N/A                |
|   375 | S    |         0.08446 | False     |                          0.95245 |                 28.18 |         7.885 | N/A                |
|   376 | T    |         0.10283 | False     |                          0.79644 |                 34.91 |         6.949 | N/A                |
|   377 | G    |         0.14518 | True      |                          0.92667 |                 30.09 |         6.543 | N/A                |
|   378 | L    |         0.13904 | True      |                          0.92695 |                 34.1  |         6.543 | N/A                |
|   379 | S    |         0.08824 | False     |                          0.79423 |                 30.28 |         6.151 | N/A                |
|   380 | V    |         0.10653 | False     |                          0.9158  |                 34.07 |         6.151 | N/A                |
|   381 | L    |         0.12057 | False     |                          1.12349 |                 34.83 |         5.42  | N/A                |
|   382 | S    |         0.09045 | False     |                          0.70867 |                 36.31 |         0     | N/A                |
|   383 | P    |         0.08729 | False     |                          0.89824 |                 35.7  |         0     | N/A                |
|   384 | P    |         0.08976 | False     |                          1.00759 |                 43.29 |         0     | N/A                |
|   385 | A    |         0.1445  | True      |                          1.00222 |                 40.53 |         0     | N/A                |
|   386 | G    |         0.13536 | True      |                          0.86074 |                 36.42 |         0     | N/A                |
|   387 | P    |         0.13121 | True      |                          0.88923 |                 41.34 |         0     | N/A                |
|   388 | R    |         0.16159 | True      |                          0.96848 |                 39.49 |         0     | N/A                |
|   389 | G    |         0.15158 | True      |                          1.00246 |                 37.28 |         0     | N/A                |
|   390 | A    |         0.08832 | False     |                          0.97428 |                 42.05 |         0     | N/A                |
|   391 | P    |         0.09659 | False     |                          0.87548 |                 54.64 |         0     | N/A                |
|   392 | P    |         0.15394 | True      |                          0.87947 |                 46.91 |         0     | N/A                |
|   393 | A    |         0.08561 | False     |                          0.95526 |                 44.37 |         0     | N/A                |
|   394 | A    |         0.09423 | False     |                          0.92219 |                 45.54 |         0     | N/A                |
|   395 | P    |         0.09601 | False     |                          0.77541 |                 41.81 |         0     | N/A                |
|   396 | Y    |         0.11112 | False     |                          0.80338 |                 41.03 |         0     | N/A                |
|   397 | H    |         0.15196 | True      |                          0.89718 |                 45.1  |         0     | N/A                |
|   398 | P    |         0.11101 | False     |                          0.79426 |                 39.07 |         0     | N/A                |
|   399 | F    |         0.14107 | True      |                          0.93845 |                 40.89 |         0     | N/A                |
|   400 | T    |         0.10786 | False     |                          0.8032  |                 38.65 |         0     | N/A                |
|   401 | T    |         0.08181 | False     |                          0.74189 |                 37.31 |         0     | N/A                |
|   402 | H    |         0.14162 | True      |                          0.9963  |                 39.69 |         0     | N/A                |
|   403 | S    |         0.07935 | False     |                          0.90139 |                 38.36 |         0     | N/A                |
|   404 | G    |         0.10868 | False     |                          0.62032 |                 38.65 |         0     | N/A                |
|   405 | Y    |         0.17048 | True      |                          0.94644 |                 41.03 |         0.22  | N/A                |
|   406 | F    |         0.06519 | False     |                          0.96147 |                 36.54 |         0.22  | N/A                |
|   407 | S    |         0.09652 | False     |                          0.76362 |                 36.97 |         0.22  | N/A                |
|   408 | S    |         0.08426 | False     |                          0.59442 |                 39.6  |         0.22  | N/A                |
|   409 | L    |         0.1506  | True      |                          1.0924  |                 43.09 |         0.22  | N/A                |
|   410 | Y    |         0.22223 | True      |                          0.78714 |                 39.43 |         0     | N/A                |
|   411 | P    |         0.15012 | True      |                          0.96007 |                 39.78 |         0     | N/A                |
|   412 | H    |         0.05815 | False     |                          0.78412 |                 35.53 |         0     | N/A                |
|   413 | H    |         0.07219 | False     |                          0.96053 |                 42.6  |         0     | N/A                |
|   414 | Q    |         0.11338 | False     |                          0.81789 |                 37    |         0     | N/A                |
|   415 | F    |         0.14262 | True      |                          0.98134 |                 38.62 |         0     | N/A                |
|   416 | G    |         0.13206 | True      |                          0.67035 |                 39.29 |         0     | N/A                |
|   417 | P    |         0.08886 | False     |                          0.98389 |                 39.08 |         0     | N/A                |
|   418 | F    |         0.10155 | False     |                          0.92953 |                 37.67 |         0     | N/A                |
|   419 | P    |         0.06609 | False     |                          0.85337 |                 37.96 |         0     | N/A                |
|   420 | H    |         0.10665 | False     |                          0.89003 |                 34.27 |         0     | N/A                |
|   421 | H    |         0.10037 | False     |                          0.96294 |                 33.99 |         0     | N/A                |
|   422 | H    |         0.11806 | False     |                          0.81846 |                 30.65 |         0     | N/A                |
|   423 | S    |         0.10638 | False     |                          0.80519 |                 32.93 |         0     | N/A                |
|   424 | Y    |         0.14144 | True      |                          0.90238 |                 37.16 |         0     | N/A                |
|   425 | P    |         0.12018 | False     |                          0.70324 |                 52.6  |         0     | N/A                |
|   426 | E    |         0.09159 | False     |                          0.53016 |                 67.94 |         0     | N/A                |
|   427 | Q    |         0.06414 | False     |                          0.69657 |                 82.55 |         0     | N/A                |
|   428 | E    |         0.03281 | False     |                          0.09769 |                 89.47 |         0     | N/A                |
|   429 | I    |         0.05461 | False     |                          0.56659 |                 93.81 |         8.085 | N/A                |
|   430 | V    |         0.00162 | False     |                          0.00286 |                 96.08 |         8.085 | N/A                |
|   431 | N    |         0.02623 | False     |                          0.08337 |                 97.2  |         8.085 | N/A                |
|   432 | L    |         0.00243 | False     |                          0.00082 |                 97.16 |         8.085 | N/A                |
|   433 | F    |         0.03338 | False     |                          0.18624 |                 96.56 |         8.085 | N/A                |
|   434 | I    |         0.00607 | False     |                          0       |                 95.19 |         0.971 | N/A                |
|   435 | P    |         0.02588 | False     |                          0.14513 |                 93.73 |         0.437 | N/A                |
|   436 | T    |         0.06405 | False     |                          0.36754 |                 92.71 |         0     | N/A                |
|   437 | Q    |         0.07987 | False     |                          0.61957 |                 92.27 |         0     | N/A                |
|   438 | A    |         0.00322 | False     |                          0       |                 92.87 |         2.494 | N/A                |
|   439 | V    |         0.02399 | False     |                          0.09045 |                 94.05 |         4.851 | N/A                |
|   440 | G    |         0.13603 | True      |                          0.6147  |                 92.42 |         4.851 | N/A                |
|   441 | A    |         0.09267 | False     |                          0.22725 |                 92.44 |         4.851 | N/A                |
|   442 | I    |         0.00489 | False     |                          0.0024  |                 94    |         4.851 | N/A                |
|   443 | I    |         0.09764 | False     |                          0.35358 |                 92.94 |         4.351 | N/A                |
|   444 | G    |         0.06394 | False     |                          0.24325 |                 90.01 |         0     | N/A                |
|   445 | K    |         0.2974  | True      |                          0.92989 |                 91.57 |         0     | N/A                |
|   446 | K    |         0.30077 | True      |                          1.01236 |                 91.01 |         0     | N/A                |
|   447 | G    |         0.07711 | False     |                          0.12721 |                 90.54 |         0     | N/A                |
|   448 | A    |         0.16958 | True      |                          0.56117 |                 92.89 |         0     | N/A                |
|   449 | H    |         0.11577 | False     |                          0.29883 |                 91.74 |         0     | N/A                |
|   450 | I    |         0.07435 | False     |                          0.13899 |                 94.19 |         0     | N/A                |
|   451 | K    |         0.14782 | True      |                          0.62863 |                 94.49 |         0     | N/A                |
|   452 | Q    |         0.13119 | True      |                          0.56167 |                 93.35 |         0     | N/A                |
|   453 | L    |         0.01889 | False     |                          0.04676 |                 92.84 |         0     | N/A                |
|   454 | A    |         0.02943 | False     |                          0.2228  |                 93.26 |         0     | N/A                |
|   455 | R    |         0.2236  | True      |                          0.73225 |                 93.23 |         0     | N/A                |
|   456 | F    |         0.17877 | True      |                          0.54815 |                 90.04 |         0     | N/A                |
|   457 | A    |         0.01757 | False     |                          0.054   |                 88.25 |         0     | N/A                |
|   458 | G    |         0.12    | False     |                          0.64114 |                 90.91 |         0     | N/A                |
|   459 | A    |         0.01167 | False     |                          0.0907  |                 92.49 |         0     | N/A                |
|   460 | S    |         0.0321  | False     |                          0.41861 |                 95.76 |         0     | N/A                |
|   461 | I    |         0.0585  | False     |                          0.09328 |                 96.18 |         0     | N/A                |
|   462 | K    |         0.08655 | False     |                          0.65105 |                 95.33 |         0     | N/A                |
|   463 | I    |         0.10858 | False     |                          0.19134 |                 94.21 |         0     | N/A                |
|   464 | A    |         0.06207 | False     |                          0.12499 |                 92.52 |         0     | N/A                |
|   465 | P    |         0.17354 | True      |                          0.8391  |                 88.43 |         0     | N/A                |
|   466 | A    |         0.09801 | False     |                          0.46951 |                 84.9  |         0     | N/A                |
|   467 | E    |         0.27259 | True      |                          0.83741 |                 81.35 |         0     | N/A                |
|   468 | G    |         0.15575 | True      |                          0.32339 |                 77.19 |         0     | N/A                |
|   469 | P    |         0.2661  | True      |                          1.01906 |                 72.48 |         0     | N/A                |
|   470 | D    |         0.17825 | True      |                          0.84622 |                 79.83 |         0     | N/A                |
|   471 | V    |         0.08979 | False     |                          0.32726 |                 85.51 |         0     | N/A                |
|   472 | S    |         0.07586 | False     |                          0.67041 |                 90.05 |         0     | N/A                |
|   473 | E    |         0.07239 | False     |                          0.38605 |                 93.05 |         0     | N/A                |
|   474 | R    |         0.06692 | False     |                          0.17395 |                 94.26 |         0     | N/A                |
|   475 | M    |         0.03549 | False     |                          0.23993 |                 95.07 |        62.372 | N/A                |
|   476 | V    |         0.00122 | False     |                          0       |                 96.86 |        62.372 | N/A                |
|   477 | I    |         0.01424 | False     |                          0.29734 |                 96.84 |        62.372 | N/A                |
|   478 | I    |         0.00338 | False     |                          0       |                 96.71 |        62.372 | N/A                |
|   479 | T    |         0.02216 | False     |                          0.21748 |                 96.14 |        62.372 | N/A                |
|   480 | G    |         0.0091  | False     |                          0.07243 |                 92.42 |         0     | N/A                |
|   481 | P    |         0.05574 | False     |                          0.29425 |                 90.69 |         0     | N/A                |
|   482 | P    |         0.03367 | False     |                          0.21023 |                 88.36 |         0     | N/A                |
|   483 | E    |         0.06571 | False     |                          0.57087 |                 89.1  |         0     | N/A                |
|   484 | A    |         0.0073  | False     |                          0.04211 |                 91.09 |         0     | N/A                |
|   485 | Q    |         0.00456 | False     |                          0.0092  |                 92.01 |         0     | N/A                |
|   486 | F    |         0.06729 | False     |                          0.45258 |                 90.71 |         0     | N/A                |
|   487 | K    |         0.03217 | False     |                          0.47301 |                 89.15 |         0     | N/A                |
|   488 | A    |         0.00181 | False     |                          0       |                 94    |         0     | N/A                |
|   489 | Q    |         0.00283 | False     |                          0       |                 94.91 |         0     | N/A                |
|   490 | G    |         0.05476 | False     |                          0.27698 |                 89.99 |         0     | N/A                |
|   491 | R    |         0.09929 | False     |                          0.52273 |                 90.53 |         0     | N/A                |
|   492 | I    |         0.00238 | False     |                          0.0016  |                 94.66 |         0     | N/A                |
|   493 | F    |         0.01771 | False     |                          0.05167 |                 91.42 |         0     | N/A                |
|   494 | G    |         0.05501 | False     |                          0.32725 |                 88.23 |         0     | N/A                |
|   495 | K    |         0.03746 | False     |                          0.22108 |                 89.14 |         0     | N/A                |
|   496 | L    |         0.00425 | False     |                          0.00165 |                 90.8  |         0     | N/A                |
|   497 | K    |         0.10712 | False     |                          0.55811 |                 85.68 |         0     | N/A                |
|   498 | E    |         0.08486 | False     |                          0.61185 |                 85.75 |         0     | N/A                |
|   499 | E    |         0.11989 | False     |                          0.39245 |                 85.22 |         0     | N/A                |
|   500 | N    |         0.14434 | True      |                          0.65462 |                 83.48 |         0     | N/A                |
|   501 | F    |         0.12724 | True      |                          0.28882 |                 84.32 |         0     | N/A                |
|   502 | F    |         0.03521 | False     |                          0.2294  |                 82.89 |         0     | N/A                |
|   503 | N    |         0.1162  | False     |                          0.61072 |                 75.24 |         0     | N/A                |
|   504 | P    |         0.1127  | False     |                          0.79796 |                 69.15 |         0     | N/A                |
|   505 | K    |         0.18932 | True      |                          0.96971 |                 67.2  |         0     | N/A                |
|   506 | E    |         0.12737 | True      |                          0.41926 |                 69.5  |         0     | N/A                |
|   507 | E    |         0.05366 | False     |                          0.28966 |                 78.27 |         0     | N/A                |
|   508 | V    |         0.02151 | False     |                          0.04357 |                 87.07 |         0     | N/A                |
|   509 | K    |         0.03749 | False     |                          0.29249 |                 90.95 |         0     | N/A                |
|   510 | L    |         0.00817 | False     |                          0.04738 |                 94.87 |         0     | N/A                |
|   511 | E    |         0.01202 | False     |                          0.1278  |                 96.84 |         0     | N/A                |
|   512 | A    |         0.00129 | False     |                          0       |                 97.28 |         0     | N/A                |
|   513 | H    |         0.03454 | False     |                          0.14014 |                 96.97 |         0     | N/A                |
|   514 | I    |         0.01803 | False     |                          0.02    |                 95.13 |         0     | N/A                |
|   515 | R    |         0.05273 | False     |                          0.47501 |                 93.22 |         0     | N/A                |
|   516 | V    |         0.00411 | False     |                          0.01619 |                 93.08 |         0     | N/A                |
|   517 | P    |         0.02791 | False     |                          0.23758 |                 92.26 |         0     | N/A                |
|   518 | S    |         0.05515 | False     |                          0.31224 |                 90.98 |         0     | N/A                |
|   519 | S    |         0.11266 | False     |                          0.60237 |                 88.83 |         0     | N/A                |
|   520 | T    |         0.01403 | False     |                          0.01158 |                 89.3  |         0     | N/A                |
|   521 | A    |         0.01122 | False     |                          0.09821 |                 90.99 |         0     | N/A                |
|   522 | G    |         0.07811 | False     |                          0.5693  |                 89.88 |         0     | N/A                |
|   523 | R    |         0.08606 | False     |                          0.50623 |                 91.56 |         0     | N/A                |
|   524 | V    |         0.00108 | False     |                          0       |                 91.24 |         0     | N/A                |
|   525 | I    |         0.0319  | False     |                          0.27199 |                 89.61 |         0     | N/A                |
|   526 | G    |         0.04161 | False     |                          0.15775 |                 88.08 |         0     | N/A                |
|   527 | K    |         0.18458 | True      |                          0.95692 |                 87.08 |         0     | N/A                |
|   528 | G    |         0.13183 | True      |                          0.74182 |                 83.34 |         0     | N/A                |
|   529 | G    |         0.0316  | False     |                          0.16792 |                 84.93 |         0     | N/A                |
|   530 | K    |         0.08478 | False     |                          0.65811 |                 85.4  |         0     | N/A                |
|   531 | T    |         0.02806 | False     |                          0.25841 |                 88.67 |         0     | N/A                |
|   532 | V    |         0.03506 | False     |                          0.11996 |                 90.48 |         0     | N/A                |
|   533 | N    |         0.03262 | False     |                          0.39263 |                 86.12 |         0     | N/A                |
|   534 | E    |         0.0715  | False     |                          0.4645  |                 85.34 |         0     | N/A                |
|   535 | L    |         0.01481 | False     |                          0.04687 |                 88.26 |         0     | N/A                |
|   536 | Q    |         0.04456 | False     |                          0.12899 |                 89.87 |         0     | N/A                |
|   537 | N    |         0.0239  | False     |                          0.18078 |                 80.74 |         0     | N/A                |
|   538 | L    |         0.07904 | False     |                          0.72996 |                 81.54 |         0     | N/A                |
|   539 | T    |         0.01242 | False     |                          0.05555 |                 84.24 |         0     | N/A                |
|   540 | S    |         0.02628 | False     |                          0.22569 |                 84.99 |         0     | N/A                |
|   541 | A    |         0.00181 | False     |                          0       |                 87.95 |         0     | N/A                |
|   542 | E    |         0.01309 | False     |                          0.22635 |                 93    |         0     | N/A                |
|   543 | V    |         0.01684 | False     |                          0.04363 |                 94.01 |         0     | N/A                |
|   544 | I    |         0.0459  | False     |                          0.34238 |                 93.56 |         0     | N/A                |
|   545 | V    |         0.02954 | False     |                          0.12182 |                 92.01 |         0     | N/A                |
|   546 | P    |         0.07334 | False     |                          0.33453 |                 88.76 |         0     | N/A                |
|   547 | R    |         0.20897 | True      |                          0.882   |                 78.54 |         0     | N/A                |
|   548 | D    |         0.13765 | True      |                          0.89884 |                 80.41 |         0     | N/A                |
|   549 | Q    |         0.05044 | False     |                          0.25087 |                 85.39 |         0     | N/A                |
|   550 | T    |         0.11229 | False     |                          0.88561 |                 83.78 |         0     | Phosphothreonine   |
|   551 | P    |         0.0448  | False     |                          0.51693 |                 87.48 |         0     | N/A                |
|   552 | D    |         0.04971 | False     |                          0.30457 |                 88.54 |         0     | N/A                |
|   553 | E    |         0.19849 | True      |                          0.94476 |                 89.38 |         0     | N/A                |
|   554 | N    |         0.11818 | False     |                          0.68782 |                 87.32 |         0     | N/A                |
|   555 | E    |         0.10602 | False     |                          0.63879 |                 90.77 |         0     | N/A                |
|   556 | E    |         0.04213 | False     |                          0.24365 |                 91.86 |         4.09  | N/A                |
|   557 | V    |         0.02163 | False     |                          0.09426 |                 93.96 |         4.09  | N/A                |
|   558 | I    |         0.03003 | False     |                          0.32799 |                 94.08 |         4.09  | N/A                |
|   559 | V    |         0.00152 | False     |                          0       |                 95.91 |         4.09  | N/A                |
|   560 | R    |         0.05441 | False     |                          0.31232 |                 96.72 |         4.09  | N/A                |
|   561 | I    |         0.00118 | False     |                          0       |                 96.63 |         4.559 | N/A                |
|   562 | I    |         0.02164 | False     |                          0.22257 |                 95.42 |         4.285 | N/A                |
|   563 | G    |         0.00558 | False     |                          0.05311 |                 88.98 |         1.289 | N/A                |
|   564 | H    |         0.02326 | False     |                          0.04899 |                 88.48 |         1.019 | N/A                |
|   565 | F    |         0.0354  | False     |                          0.13694 |                 88.57 |         1.019 | N/A                |
|   566 | F    |         0.08298 | False     |                          0.54535 |                 87.23 |         1.019 | N/A                |
|   567 | A    |         0.00726 | False     |                          0.02515 |                 85.03 |         0.467 | N/A                |
|   568 | S    |         0.00126 | False     |                          0.00079 |                 90.9  |         0     | N/A                |
|   569 | Q    |         0.0375  | False     |                          0.07472 |                 91.38 |         0     | N/A                |
|   570 | T    |         0.02406 | False     |                          0.42289 |                 87.67 |         0     | N/A                |
|   571 | A    |         0.00087 | False     |                          0       |                 91.93 |         0     | N/A                |
|   572 | Q    |         0.00716 | False     |                          0.01357 |                 94.39 |         0     | N/A                |
|   573 | R    |         0.10432 | False     |                          0.34405 |                 91.53 |         0     | N/A                |
|   574 | K    |         0.04013 | False     |                          0.38562 |                 91.01 |         0     | N/A                |
|   575 | I    |         0.0026  | False     |                          0       |                 94.13 |         0     | N/A                |
|   576 | R    |         0.05004 | False     |                          0.13855 |                 92.39 |         0     | N/A                |
|   577 | E    |         0.06285 | False     |                          0.36068 |                 90.59 |         0     | N/A                |
|   578 | I    |         0.03222 | False     |                          0.16938 |                 91.01 |         0.147 | N/A                |
|   579 | V    |         0.01799 | False     |                          0.10187 |                 90.59 |         0.147 | N/A                |
|   580 | Q    |         0.05957 | False     |                          0.35499 |                 88.59 |         0.147 | N/A                |
|   581 | Q    |         0.06835 | False     |                          0.51996 |                 87.4  |         0.147 | N/A                |
|   582 | V    |         0.03581 | False     |                          0.08093 |                 85.48 |         0.147 | N/A                |
|   583 | K    |         0.07786 | False     |                          0.48682 |                 83.46 |         0     | N/A                |
|   584 | Q    |         0.06926 | False     |                          0.57852 |                 80.69 |         0     | N/A                |
|   585 | Q    |         0.06736 | False     |                          0.50474 |                 78.34 |         0     | N/A                |
|   586 | E    |         0.09141 | False     |                          0.49325 |                 74.98 |         0     | N/A                |
|   587 | Q    |         0.11646 | False     |                          0.74999 |                 64.64 |         0     | N/A                |
|   588 | K    |         0.12584 | True      |                          0.81307 |                 58.82 |         0     | N/A                |
|   589 | Y    |         0.14719 | True      |                          0.8072  |                 51.38 |         0     | N/A                |
|   590 | P    |         0.08894 | False     |                          0.83149 |                 45.5  |         0     | N/A                |
|   591 | Q    |         0.13173 | True      |                          0.88543 |                 44.32 |         0     | N/A                |
|   592 | G    |         0.10551 | False     |                          0.87426 |                 33.1  |         0     | N/A                |
|   593 | V    |         0.15694 | True      |                          1.04672 |                 35.33 |         0     | N/A                |
|   594 | A    |         0.07045 | False     |                          0.92091 |                 33.62 |         0     | N/A                |
|   595 | S    |         0.07162 | False     |                          0.84425 |                 34.4  |         0     | N/A                |
|   596 | Q    |         0.16483 | True      |                          0.9237  |                 36.05 |         0     | N/A                |
|   597 | R    |         0.17987 | True      |                          1.00227 |                 39.19 |         0     | N/A                |
|   598 | S    |         0.09565 | False     |                          0.83753 |                 37.77 |         0     | N/A                |
|   599 | K    |         0.09472 | False     |                          1.30504 |                 42.96 |         0     | N/A                |


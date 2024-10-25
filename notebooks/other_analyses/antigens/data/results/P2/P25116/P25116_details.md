# Detailed Data for P25116


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: P25116
- **Gene Name**: PAR1
- **Protein Name**: Proteinase-activated receptor 1
- **Swiss Prot**: PAR1_HUMAN
- **Family**: G-protein coupled receptor
- **Biomarker Application**: disease progression,prognosis
- **Number of Isoforms**: 0
- **Regulation**: 1
- **(transcriptomics) AUC**: nan
- **(transcriptomics) Fold Change**: nan
- **(transcriptomics) Regulation**: Downregulated
- **Discotope Epitope Count**: 108
- **Max n_uniprots (Homo)**: 1
- **Max n_uniprots (Hetero)**: 3


## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| F2R               | F2                |   0.998 |
| F2R               | PROCR             |   0.994 |
| F2R               | GNAQ              |   0.991 |
| F2R               | GNA12             |   0.986 |
| F2R               | GNA13             |   0.978 |
| F2R               | THBD              |   0.966 |
| F2R               | ARRB2             |   0.962 |
| F2R               | ARRB1             |   0.962 |
| F2R               | PROC              |   0.96  |
| F2R               | LPAR1             |   0.945 |
| F2R               | AGT               |   0.936 |
| F2R               | LPAR2             |   0.923 |
| F2R               | CHRM2             |   0.919 |
| F2R               | F2RL3             |   0.916 |
| F2R               | LPAR3             |   0.915 |
| F2R               | LPAR5             |   0.907 |
| F2R               | CHRM1             |   0.907 |
| F2R               | LPAR4             |   0.905 |
| F2R               | LPAR6             |   0.904 |
| F2R               | GNAS              |   0.901 |

## Homologs

| uniprot_id   | gene_id   |
|:-------------|:----------|
| D6RJH3       | F2RL1     |
| Q96RI0       | F2RL3     |
| O00254       | F2RL2     |
| A0A1B0GUR3   | P2RY8     |
| Q14330       | GPR18     |
| Q13304       | GPR17     |
| Q9Y271       | CYSLTR1   |
| O00398       | P2RY10    |
| Q9NS75       | CYSLTR2   |
| Q9HC97       | GPR35     |
| Q99677       | LPAR4     |
| P43657       | LPAR6     |
| Q99678       | GPR20     |
| A8K858       | GPR55     |
| P46093       | GPR4      |
| B5B0C2       | GPR65     |

## Biological Assemblies

|   Unnamed: 0 |   assembly |   n_uniprots | composition   | crystal_id   |
|-------------:|-----------:|-------------:|:--------------|:-------------|
|            0 |          1 |            3 | Hetero        | 1nrp         |
|            0 |          1 |            3 | Hetero        | 3hki         |
|            1 |          2 |            3 | Hetero        | 3hki         |
|            0 |          1 |            3 | Hetero        | 1nrq         |
|            0 |          1 |            3 | Hetero        | 3hkj         |
|            1 |          2 |            3 | Hetero        | 3hkj         |
|            0 |          1 |            3 | Hetero        | 1nro         |
|            0 |          1 |            3 | Hetero        | 3bef         |
|            1 |          2 |            3 | Hetero        | 3bef         |
|            0 |          1 |            3 | Hetero        | 3lu9         |
|            1 |          2 |            3 | Hetero        | 3lu9         |
|            0 |          1 |            3 | Hetero        | 1nrn         |
|            0 |          1 |            1 | Homo          | 3vw7         |
|            0 |          1 |            3 | Hetero        | 1nrr         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification   | glycosylation                   |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:---------------|:--------------------------------|
|     1 | M    |         0.11086 | False     |                          1.19601 |                 49.26 |         0     | N/A            | N/A                             |
|     2 | G    |         0.16515 | False     |                          0.48954 |                 61.02 |         0     | N/A            | N/A                             |
|     3 | P    |         0.21016 | True      |                          0.81082 |                 60.52 |         0     | N/A            | N/A                             |
|     4 | R    |         0.20294 | True      |                          0.84447 |                 63.14 |         0     | N/A            | N/A                             |
|     5 | R    |         0.14117 | False     |                          0.75612 |                 63.49 |         0     | N/A            | N/A                             |
|     6 | L    |         0.09706 | False     |                          0.76345 |                 64.71 |        36.099 | N/A            | N/A                             |
|     7 | L    |         0.15318 | False     |                          0.7668  |                 66.88 |        50.953 | N/A            | N/A                             |
|     8 | L    |         0.09257 | False     |                          0.78623 |                 58.33 |        56.506 | N/A            | N/A                             |
|     9 | V    |         0.06738 | False     |                          0.60552 |                 66.88 |        57.48  | N/A            | N/A                             |
|    10 | A    |         0.09566 | False     |                          0.47632 |                 60.12 |        57.48  | N/A            | N/A                             |
|    11 | A    |         0.0702  | False     |                          0.48028 |                 56.54 |        51.023 | N/A            | N/A                             |
|    12 | C    |         0.07108 | False     |                          0.67742 |                 48.04 |        42.83  | N/A            | N/A                             |
|    13 | F    |         0.12891 | False     |                          0.76271 |                 51.66 |        41.217 | N/A            | N/A                             |
|    14 | S    |         0.10541 | False     |                          0.64392 |                 54.31 |        20.914 | N/A            | N/A                             |
|    15 | L    |         0.06096 | False     |                          0.89392 |                 46.07 |        18.091 | N/A            | N/A                             |
|    16 | C    |         0.11971 | False     |                          0.63148 |                 42.15 |         2.688 | N/A            | N/A                             |
|    17 | G    |         0.23519 | True      |                          0.58337 |                 45.83 |         0     | N/A            | N/A                             |
|    18 | P    |         0.21342 | True      |                          0.76799 |                 42.23 |         0     | N/A            | N/A                             |
|    19 | L    |         0.18515 | True      |                          0.89871 |                 41.25 |         0     | N/A            | N/A                             |
|    20 | L    |         0.19721 | True      |                          1.00978 |                 39.16 |         0     | N/A            | N/A                             |
|    21 | S    |         0.19771 | True      |                          0.7736  |                 36.74 |         0     | N/A            | N/A                             |
|    22 | A    |         0.19844 | True      |                          1.00076 |                 34.83 |         0     | N/A            | N/A                             |
|    23 | R    |         0.22985 | True      |                          0.90998 |                 31.46 |         0     | N/A            | N/A                             |
|    24 | T    |         0.15005 | False     |                          0.8997  |                 32.02 |         0     | N/A            | N/A                             |
|    25 | R    |         0.30398 | True      |                          0.91922 |                 28.02 |         0     | N/A            | N/A                             |
|    26 | A    |         0.12691 | False     |                          1.05312 |                 34.29 |         0     | N/A            | N/A                             |
|    27 | R    |         0.14726 | False     |                          0.90287 |                 23.15 |         0     | N/A            | N/A                             |
|    28 | R    |         0.12835 | False     |                          0.8397  |                 28.65 |         0     | N/A            | N/A                             |
|    29 | P    |         0.14624 | False     |                          0.84257 |                 38.75 |         0     | N/A            | N/A                             |
|    30 | E    |         0.13494 | False     |                          0.85768 |                 25.58 |         0     | N/A            | N/A                             |
|    31 | S    |         0.18246 | True      |                          0.90739 |                 32.23 |         0     | N/A            | N/A                             |
|    32 | K    |         0.16996 | False     |                          1.00058 |                 25.96 |         0     | N/A            | N/A                             |
|    33 | A    |         0.21938 | True      |                          0.8915  |                 34.01 |         0     | N/A            | N/A                             |
|    34 | T    |         0.21232 | True      |                          0.91748 |                 30.31 |         0     | N/A            | N/A                             |
|    35 | N    |         0.16406 | False     |                          0.9869  |                 27.03 |         0     | N/A            | N-linked (GlcNAc...) asparagine |
|    36 | A    |         0.17466 | True      |                          0.91077 |                 33.32 |         0     | N/A            | N/A                             |
|    37 | T    |         0.20228 | True      |                          1.01095 |                 26.02 |         0     | N/A            | N/A                             |
|    38 | L    |         0.28245 | True      |                          1.00285 |                 29.83 |         0     | N/A            | N/A                             |
|    39 | D    |         0.14875 | False     |                          0.76766 |                 28.99 |         0     | N/A            | N/A                             |
|    40 | P    |         0.14346 | False     |                          0.66721 |                 29.35 |         0     | N/A            | N/A                             |
|    41 | R    |         0.21998 | True      |                          0.41356 |                 36.96 |         0     | N/A            | N/A                             |
|    42 | S    |         0.06816 | False     |                          0.15028 |                 43.84 |         0     | N/A            | N/A                             |
|    43 | F    |         0.0619  | False     |                          0.14015 |                 42.77 |         0     | N/A            | N/A                             |
|    44 | L    |         0.09838 | False     |                          0.20856 |                 42.74 |         0     | N/A            | N/A                             |
|    45 | L    |         0.10965 | False     |                          0.16642 |                 35.07 |         0     | N/A            | N/A                             |
|    46 | R    |         0.24426 | True      |                          0.56928 |                 36.38 |         0     | N/A            | N/A                             |
|    47 | N    |         0.16697 | False     |                          0.42547 |                 39.51 |         0     | N/A            | N/A                             |
|    48 | P    |         0.25169 | True      |                          0.44168 |                 36.65 |         0     | N/A            | N/A                             |
|    49 | N    |         0.23462 | True      |                          0.62432 |                 37.3  |         0     | N/A            | N/A                             |
|    50 | D    |         0.22899 | True      |                          0.709   |                 38.17 |         0     | N/A            | N/A                             |
|    51 | K    |         0.2337  | True      |                          0.88383 |                 33.72 |         0     | N/A            | N/A                             |
|    52 | Y    |         0.24378 | True      |                          0.97694 |                 32.4  |         0     | N/A            | N/A                             |
|    53 | E    |         0.25323 | True      |                          0.82705 |                 31.16 |         0     | N/A            | N/A                             |
|    54 | P    |         0.16114 | False     |                          0.76489 |                 31.03 |         0     | N/A            | N/A                             |
|    55 | F    |         0.23394 | True      |                          1.04666 |                 24.95 |         0     | N/A            | N/A                             |
|    56 | W    |         0.19138 | True      |                          1.01614 |                 32.64 |         0     | N/A            | N/A                             |
|    57 | E    |         0.15932 | False     |                          0.88893 |                 27.69 |         0     | N/A            | N/A                             |
|    58 | D    |         0.21929 | True      |                          0.85051 |                 28.34 |         0     | N/A            | N/A                             |
|    59 | E    |         0.16924 | False     |                          0.91704 |                 32.31 |         0     | N/A            | N/A                             |
|    60 | E    |         0.15665 | False     |                          0.78166 |                 28.01 |         0     | N/A            | N/A                             |
|    61 | K    |         0.16594 | False     |                          0.87682 |                 31.46 |         0     | N/A            | N/A                             |
|    62 | N    |         0.24135 | True      |                          0.77895 |                 28.37 |         0     | N/A            | N-linked (GlcNAc...) asparagine |
|    63 | E    |         0.25472 | True      |                          0.82429 |                 25.96 |         0     | N/A            | N/A                             |
|    64 | S    |         0.18243 | True      |                          0.94175 |                 29.01 |         0     | N/A            | N/A                             |
|    65 | G    |         0.24014 | True      |                          0.95686 |                 30.31 |         0     | N/A            | N/A                             |
|    66 | L    |         0.17072 | False     |                          1.08491 |                 24.25 |         0     | N/A            | N/A                             |
|    67 | T    |         0.20176 | True      |                          0.76979 |                 27.53 |         0     | N/A            | N/A                             |
|    68 | E    |         0.1142  | False     |                          0.77306 |                 28.63 |         0     | N/A            | N/A                             |
|    69 | Y    |         0.22944 | True      |                          0.89616 |                 23.75 |         0     | N/A            | N/A                             |
|    70 | R    |         0.2026  | True      |                          0.89834 |                 28.26 |         0     | N/A            | N/A                             |
|    71 | L    |         0.12726 | False     |                          0.86604 |                 27.78 |         0     | N/A            | N/A                             |
|    72 | V    |         0.12336 | False     |                          0.89011 |                 29.25 |         0     | N/A            | N/A                             |
|    73 | S    |         0.14175 | False     |                          0.63894 |                 26.09 |         0     | N/A            | N/A                             |
|    74 | I    |         0.18964 | True      |                          0.88095 |                 30.3  |         0     | N/A            | N/A                             |
|    75 | N    |         0.16064 | False     |                          0.79185 |                 27.54 |         0     | N/A            | N-linked (GlcNAc...) asparagine |
|    76 | K    |         0.16124 | False     |                          1.03543 |                 27.07 |         0     | N/A            | N/A                             |
|    77 | S    |         0.16355 | False     |                          0.6693  |                 30.39 |         0     | N/A            | N/A                             |
|    78 | S    |         0.13835 | False     |                          0.69373 |                 30.28 |         0     | N/A            | N/A                             |
|    79 | P    |         0.17047 | False     |                          0.87885 |                 32.24 |         0     | N/A            | N/A                             |
|    80 | L    |         0.18125 | True      |                          0.99812 |                 33.52 |         0     | N/A            | N/A                             |
|    81 | Q    |         0.21019 | True      |                          0.70256 |                 30.15 |         0     | N/A            | N/A                             |
|    82 | K    |         0.24076 | True      |                          0.90922 |                 31.56 |         0     | N/A            | N/A                             |
|    83 | Q    |         0.31576 | True      |                          0.71376 |                 31.19 |         0     | N/A            | N/A                             |
|    84 | L    |         0.18216 | True      |                          0.70232 |                 35.65 |         0     | N/A            | N/A                             |
|    85 | P    |         0.21039 | True      |                          0.52798 |                 42.35 |         0     | N/A            | N/A                             |
|    86 | A    |         0.17016 | False     |                          0.17555 |                 51.89 |         0     | N/A            | N/A                             |
|    87 | F    |         0.26934 | True      |                          0.74982 |                 57.26 |         0     | N/A            | N/A                             |
|    88 | I    |         0.10788 | False     |                          0.09729 |                 65.1  |         0     | N/A            | N/A                             |
|    89 | S    |         0.06444 | False     |                          0.18082 |                 67.79 |         0     | N/A            | N/A                             |
|    90 | E    |         0.23614 | True      |                          0.81327 |                 68.99 |         0     | N/A            | N/A                             |
|    91 | D    |         0.25742 | True      |                          0.4918  |                 68.85 |         0     | N/A            | N/A                             |
|    92 | A    |         0.02941 | False     |                          0       |                 71.72 |         0     | N/A            | N/A                             |
|    93 | S    |         0.12695 | False     |                          0.18337 |                 75.78 |         0     | N/A            | N/A                             |
|    94 | G    |         0.19764 | True      |                          0.47065 |                 79.69 |         0.912 | N/A            | N/A                             |
|    95 | Y    |         0.08858 | False     |                          0.13203 |                 81.45 |        11.571 | N/A            | N/A                             |
|    96 | L    |         0.01012 | False     |                          0.00082 |                 83.62 |        12.962 | N/A            | N/A                             |
|    97 | T    |         0.31871 | True      |                          0.50066 |                 84.47 |        13.197 | N/A            | N/A                             |
|    98 | S    |         0.17961 | True      |                          0.26082 |                 89.95 |        13.598 | N/A            | N/A                             |
|    99 | S    |         0.16173 | False     |                          0.62785 |                 90.32 |        17.195 | N/A            | N/A                             |
|   100 | W    |         0.06608 | False     |                          0.17915 |                 90.31 |        44.022 | N/A            | N/A                             |
|   101 | L    |         0.00633 | False     |                          0       |                 90.6  |        44.218 | N/A            | N/A                             |
|   102 | T    |         0.07857 | False     |                          0.2022  |                 93.5  |        43.985 | N/A            | N/A                             |
|   103 | L    |         0.15739 | False     |                          0.6636  |                 94.28 |        43.844 | N/A            | N/A                             |
|   104 | F    |         0.07233 | False     |                          0.41293 |                 95.01 |        42.634 | N/A            | N/A                             |
|   105 | V    |         0.0034  | False     |                          0       |                 94.45 |         1.471 | N/A            | N/A                             |
|   106 | P    |         0.00845 | False     |                          0       |                 96.7  |         0.261 | N/A            | N/A                             |
|   107 | S    |         0.05516 | False     |                          0.40523 |                 97.18 |         8.995 | N/A            | N/A                             |
|   108 | V    |         0.02302 | False     |                          0.22634 |                 96.77 |        80.784 | N/A            | N/A                             |
|   109 | Y    |         0.01161 | False     |                          0.01682 |                 97.23 |        86.889 | N/A            | N/A                             |
|   110 | T    |         0.0244  | False     |                          0.35729 |                 98.03 |        88.649 | N/A            | N/A                             |
|   111 | G    |         0.02662 | False     |                          0.41024 |                 97.72 |        91.396 | N/A            | N/A                             |
|   112 | V    |         0.00402 | False     |                          0.03579 |                 97.6  |        94.316 | N/A            | N/A                             |
|   113 | F    |         0.02483 | False     |                          0.29288 |                 97.75 |        94.277 | N/A            | N/A                             |
|   114 | V    |         0.02459 | False     |                          0.66016 |                 97.79 |        93.754 | N/A            | N/A                             |
|   115 | V    |         0.01614 | False     |                          0.49458 |                 96.52 |        87.461 | N/A            | N/A                             |
|   116 | S    |         0.00117 | False     |                          0       |                 96.32 |        10.926 | N/A            | N/A                             |
|   117 | L    |         0.01274 | False     |                          0.2539  |                 96.98 |         0.058 | N/A            | N/A                             |
|   118 | P    |         0.02612 | False     |                          0.53829 |                 95.42 |         0.199 | N/A            | N/A                             |
|   119 | L    |         0.01995 | False     |                          0.47848 |                 94.46 |        14.128 | N/A            | N/A                             |
|   120 | N    |         0.00196 | False     |                          0       |                 95.77 |        16.684 | N/A            | N/A                             |
|   121 | I    |         0.03277 | False     |                          0.47278 |                 95.7  |        82.29  | N/A            | N/A                             |
|   122 | M    |         0.04507 | False     |                          0.47133 |                 92.68 |        88.292 | N/A            | N/A                             |
|   123 | A    |         0.0088  | False     |                          0.08017 |                 93    |        93.538 | N/A            | N/A                             |
|   124 | I    |         0.02724 | False     |                          0.19759 |                 94.94 |        99.51  | N/A            | N/A                             |
|   125 | V    |         0.03054 | False     |                          0.44366 |                 93.93 |        99.972 | N/A            | N/A                             |
|   126 | V    |         0.01631 | False     |                          0.01428 |                 91.74 |        99.951 | N/A            | N/A                             |
|   127 | F    |         0.00351 | False     |                          0       |                 92.73 |        99.683 | N/A            | N/A                             |
|   128 | I    |         0.10693 | False     |                          0.50516 |                 94.2  |        96.207 | N/A            | N/A                             |
|   129 | L    |         0.19268 | True      |                          0.6949  |                 92.45 |        81.386 | N/A            | N/A                             |
|   130 | K    |         0.26336 | True      |                          0.51142 |                 88.84 |         0     | N/A            | N/A                             |
|   131 | M    |         0.08463 | False     |                          0.05569 |                 88.14 |         0     | N/A            | N/A                             |
|   132 | K    |         0.14597 | False     |                          0.6733  |                 90.21 |         0     | N/A            | N/A                             |
|   133 | V    |         0.04759 | False     |                          0.2155  |                 89.48 |         0     | N/A            | N/A                             |
|   134 | K    |         0.21419 | True      |                          0.74443 |                 90.01 |         0     | N/A            | N/A                             |
|   135 | K    |         0.13635 | False     |                          0.49869 |                 90.92 |         0     | N/A            | N/A                             |
|   136 | P    |         0.02567 | False     |                          0.11531 |                 93.31 |         0.054 | N/A            | N/A                             |
|   137 | A    |         0.02653 | False     |                          0.14884 |                 91.74 |        24.538 | N/A            | N/A                             |
|   138 | V    |         0.01698 | False     |                          0.01904 |                 92.96 |        74.413 | N/A            | N/A                             |
|   139 | V    |         0.01241 | False     |                          0.03332 |                 96.04 |        75.261 | N/A            | N/A                             |
|   140 | Y    |         0.01625 | False     |                          0.0874  |                 95.37 |        75.293 | N/A            | N/A                             |
|   141 | M    |         0.00659 | False     |                          0.05293 |                 94.25 |        75.293 | N/A            | N/A                             |
|   142 | L    |         0.01824 | False     |                          0.17724 |                 95.65 |        73.042 | N/A            | N/A                             |
|   143 | H    |         0.01658 | False     |                          0.2066  |                 97.35 |        20.813 | N/A            | N/A                             |
|   144 | L    |         0.00102 | False     |                          0.00247 |                 96.16 |        19.7   | N/A            | N/A                             |
|   145 | A    |         0.00062 | False     |                          0       |                 96.32 |        13.599 | N/A            | N/A                             |
|   146 | T    |         0.01396 | False     |                          0.31855 |                 97.05 |         8.467 | N/A            | N/A                             |
|   147 | A    |         0.00114 | False     |                          0.00107 |                 96.94 |         2.568 | N/A            | N/A                             |
|   148 | D    |         0.00154 | False     |                          0.00472 |                 96.54 |         0     | N/A            | N/A                             |
|   149 | V    |         0.00635 | False     |                          0.20279 |                 97.38 |        73.022 | N/A            | N/A                             |
|   150 | L    |         0.01002 | False     |                          0.48279 |                 97.38 |        79.088 | N/A            | N/A                             |
|   151 | F    |         0.00982 | False     |                          0.05688 |                 96.19 |        79.207 | N/A            | N/A                             |
|   152 | V    |         0.00153 | False     |                          0       |                 97.01 |        79.207 | N/A            | N/A                             |
|   153 | S    |         0.03146 | False     |                          0.40916 |                 96.05 |        79.207 | N/A            | N/A                             |
|   154 | V    |         0.02362 | False     |                          0.08734 |                 96.34 |        74.822 | N/A            | N/A                             |
|   155 | L    |         0.00738 | False     |                          0.00989 |                 96.12 |        18.649 | N/A            | N/A                             |
|   156 | P    |         0.05476 | False     |                          0.36638 |                 97.75 |        16.454 | N/A            | N/A                             |
|   157 | F    |         0.06067 | False     |                          0.32304 |                 97.73 |         0     | N/A            | N/A                             |
|   158 | K    |         0.03587 | False     |                          0.08275 |                 95.86 |         0     | N/A            | N/A                             |
|   159 | I    |         0.05945 | False     |                          0.11919 |                 97.28 |         4.877 | N/A            | N/A                             |
|   160 | S    |         0.06018 | False     |                          0.34585 |                 97.79 |         4.877 | N/A            | N/A                             |
|   161 | Y    |         0.02679 | False     |                          0.00365 |                 96.43 |         4.877 | N/A            | N/A                             |
|   162 | Y    |         0.02116 | False     |                          0.01909 |                 95.44 |         4.877 | N/A            | N/A                             |
|   163 | F    |         0.15267 | False     |                          0.52778 |                 96.18 |         4.877 | N/A            | N/A                             |
|   164 | S    |         0.17434 | True      |                          0.35982 |                 95.04 |         0.837 | N/A            | N/A                             |
|   165 | G    |         0.03713 | False     |                          0.27907 |                 92.49 |         0.336 | N/A            | N/A                             |
|   166 | S    |         0.00712 | False     |                          0       |                 92.11 |         0     | N/A            | N/A                             |
|   167 | D    |         0.16452 | False     |                          0.18697 |                 94.62 |         0     | N/A            | N/A                             |
|   168 | W    |         0.05265 | False     |                          0.02994 |                 96.01 |         0     | N/A            | N/A                             |
|   169 | Q    |         0.29649 | True      |                          0.65124 |                 95.59 |         0     | N/A            | N/A                             |
|   170 | F    |         0.18015 | True      |                          0.41129 |                 96.45 |         0     | N/A            | N/A                             |
|   171 | G    |         0.16764 | False     |                          0.49972 |                 95.49 |         0     | N/A            | N/A                             |
|   172 | S    |         0.13107 | False     |                          0.28134 |                 95.62 |         0     | N/A            | N/A                             |
|   173 | E    |         0.23103 | True      |                          0.5856  |                 96.77 |         0     | N/A            | N/A                             |
|   174 | L    |         0.04299 | False     |                          0.29324 |                 97.5  |         0     | N/A            | N/A                             |
|   175 | C    |         0.01166 | False     |                          0       |                 97.33 |         0     | N/A            | N/A                             |
|   176 | R    |         0.08032 | False     |                          0.19743 |                 96.86 |         0     | N/A            | N/A                             |
|   177 | F    |         0.09658 | False     |                          0.54348 |                 97.81 |         4.17  | N/A            | N/A                             |
|   178 | V    |         0.00313 | False     |                          0.00286 |                 97.37 |         4.565 | N/A            | N/A                             |
|   179 | T    |         0.0174  | False     |                          0.01619 |                 94.74 |         4.906 | N/A            | N/A                             |
|   180 | A    |         0.00715 | False     |                          0.01893 |                 96.08 |         5.444 | N/A            | N/A                             |
|   181 | A    |         0.00966 | False     |                          0.1312  |                 96.73 |         8.064 | N/A            | N/A                             |
|   182 | F    |         0.02065 | False     |                          0.09775 |                 93.8  |        11.106 | N/A            | N/A                             |
|   183 | Y    |         0.01598 | False     |                          0.03284 |                 92.66 |        10.518 | N/A            | N/A                             |
|   184 | C    |         0.02156 | False     |                          0.08597 |                 95.83 |         7.863 | N/A            | N/A                             |
|   185 | N    |         0.00821 | False     |                          0.04925 |                 95.14 |         7.986 | N/A            | N/A                             |
|   186 | M    |         0.01413 | False     |                          0.05748 |                 91.96 |        17.203 | N/A            | N/A                             |
|   187 | Y    |         0.0024  | False     |                          0       |                 94.1  |        26.694 | N/A            | N/A                             |
|   188 | A    |         0.00087 | False     |                          0       |                 96.46 |        32.117 | N/A            | N/A                             |
|   189 | S    |         0.00651 | False     |                          0.05288 |                 95.26 |        38.612 | N/A            | N/A                             |
|   190 | I    |         0.00227 | False     |                          0       |                 94.76 |        91.927 | N/A            | N/A                             |
|   191 | L    |         0.00797 | False     |                          0.15577 |                 96.26 |        96.795 | N/A            | N/A                             |
|   192 | L    |         0.00095 | False     |                          0       |                 96.14 |        97.631 | N/A            | N/A                             |
|   193 | M    |         0.00137 | False     |                          0.00473 |                 94.38 |        97.505 | N/A            | N/A                             |
|   194 | T    |         0.00749 | False     |                          0.04284 |                 95.77 |        97.313 | N/A            | N/A                             |
|   195 | V    |         0.00741 | False     |                          0.15328 |                 96.3  |        97.219 | N/A            | N/A                             |
|   196 | I    |         0.00924 | False     |                          0.076   |                 94.25 |        96.015 | N/A            | N/A                             |
|   197 | S    |         0.01304 | False     |                          0.09714 |                 94.29 |        83.825 | N/A            | N/A                             |
|   198 | I    |         0.02478 | False     |                          0.32399 |                 95.75 |        83.293 | N/A            | N/A                             |
|   199 | D    |         0.01214 | False     |                          0.03716 |                 94.25 |        40.798 | N/A            | N/A                             |
|   200 | R    |         0.0452  | False     |                          0.20098 |                 92.3  |        40.798 | N/A            | N/A                             |
|   201 | F    |         0.05201 | False     |                          0.18727 |                 93.79 |        48.977 | N/A            | N/A                             |
|   202 | L    |         0.04842 | False     |                          0.21516 |                 94.77 |        48.895 | N/A            | N/A                             |
|   203 | A    |         0.05801 | False     |                          0.23086 |                 91.38 |        48.426 | N/A            | N/A                             |
|   204 | V    |         0.09089 | False     |                          0.22316 |                 90.61 |        48.032 | N/A            | N/A                             |
|   205 | V    |         0.07215 | False     |                          0.27582 |                 91.96 |        44.282 | N/A            | N/A                             |
|   206 | Y    |         0.1548  | False     |                          0.45459 |                 92    |         1.612 | N/A            | N/A                             |
|   207 | P    |         0.26719 | True      |                          0.44496 |                 88.72 |         0.657 | N/A            | N/A                             |
|   208 | M    |         0.43755 | True      |                          0.70721 |                 89.82 |         0     | N/A            | N/A                             |
|   209 | Q    |         0.37911 | True      |                          0.66083 |                 90.76 |         0     | N/A            | N/A                             |
|   210 | S    |         0.03925 | False     |                          0.03224 |                 90.82 |         0     | N/A            | N/A                             |
|   211 | L    |         0.36585 | True      |                          0.63486 |                 89.41 |         0     | N/A            | N/A                             |
|   212 | S    |         0.2815  | True      |                          0.60837 |                 90.62 |         0     | N/A            | N/A                             |
|   213 | W    |         0.13013 | False     |                          0.69055 |                 89.71 |         0     | N/A            | N/A                             |
|   214 | R    |         0.13073 | False     |                          0.22936 |                 93.52 |         0     | N/A            | N/A                             |
|   215 | T    |         0.18764 | True      |                          0.40796 |                 95.83 |         0     | N/A            | N/A                             |
|   216 | L    |         0.21121 | True      |                          0.47161 |                 96.18 |         0     | N/A            | N/A                             |
|   217 | G    |         0.16698 | False     |                          0.63085 |                 96.91 |         0     | N/A            | N/A                             |
|   218 | R    |         0.16625 | False     |                          0.4443  |                 97.21 |         0     | N/A            | N/A                             |
|   219 | A    |         0.006   | False     |                          0.00711 |                 97.52 |         2.529 | N/A            | N/A                             |
|   220 | S    |         0.0492  | False     |                          0.30916 |                 97.92 |         5.521 | N/A            | N/A                             |
|   221 | F    |         0.04099 | False     |                          0.7406  |                 98.29 |        71.497 | N/A            | N/A                             |
|   222 | T    |         0.01959 | False     |                          0.29159 |                 98.31 |        76.878 | N/A            | N/A                             |
|   223 | C    |         0.00156 | False     |                          0       |                 98.45 |        85.92  | N/A            | N/A                             |
|   224 | L    |         0.04254 | False     |                          0.69404 |                 98.28 |        95.322 | N/A            | N/A                             |
|   225 | A    |         0.01411 | False     |                          0.36154 |                 98.41 |        97.034 | N/A            | N/A                             |
|   226 | I    |         0.02694 | False     |                          0.0536  |                 98.19 |        99.136 | N/A            | N/A                             |
|   227 | W    |         0.02269 | False     |                          0.15643 |                 98.14 |        99.293 | N/A            | N/A                             |
|   228 | A    |         0.02233 | False     |                          0.56598 |                 98.01 |        98.69  | N/A            | N/A                             |
|   229 | L    |         0.02933 | False     |                          0.58895 |                 96.58 |        98.117 | N/A            | N/A                             |
|   230 | A    |         0.00306 | False     |                          0       |                 96.12 |        94.821 | N/A            | N/A                             |
|   231 | I    |         0.10059 | False     |                          0.52558 |                 96.28 |        91.968 | N/A            | N/A                             |
|   232 | A    |         0.04183 | False     |                          0.59629 |                 95.9  |        60.732 | N/A            | N/A                             |
|   233 | G    |         0.05136 | False     |                          0.15078 |                 93.02 |        34.308 | N/A            | N/A                             |
|   234 | V    |         0.02448 | False     |                          0.02856 |                 94.75 |        31.929 | N/A            | N/A                             |
|   235 | V    |         0.04351 | False     |                          0.41225 |                 95.41 |         3.924 | N/A            | N/A                             |
|   236 | P    |         0.1499  | False     |                          0.20776 |                 92.2  |         1.658 | N/A            | N/A                             |
|   237 | L    |         0.00844 | False     |                          0       |                 92.06 |         0     | N/A            | N/A                             |
|   238 | L    |         0.13349 | False     |                          0.37236 |                 94.39 |         0     | N/A            | N/A                             |
|   239 | L    |         0.27799 | True      |                          0.78092 |                 93.34 |         0     | N/A            | N/A                             |
|   240 | K    |         0.37043 | True      |                          0.44347 |                 89.74 |         0     | N/A            | N/A                             |
|   241 | E    |         0.22883 | True      |                          0.46775 |                 89.72 |         0     | N/A            | N/A                             |
|   242 | Q    |         0.02216 | False     |                          0.00859 |                 90.29 |         0     | N/A            | N/A                             |
|   243 | T    |         0.09949 | False     |                          0.16713 |                 91.41 |         0     | N/A            | N/A                             |
|   244 | I    |         0.16141 | False     |                          0.15199 |                 89.05 |         0     | N/A            | N/A                             |
|   245 | Q    |         0.32133 | True      |                          0.59463 |                 88.53 |         0     | N/A            | N/A                             |
|   246 | V    |         0.04503 | False     |                          0.01352 |                 84.41 |         0     | N/A            | N/A                             |
|   247 | P    |         0.2718  | True      |                          0.44841 |                 78.03 |         0     | N/A            | N/A                             |
|   248 | G    |         0.33458 | True      |                          0.68637 |                 79.94 |         0     | N/A            | N/A                             |
|   249 | L    |         0.31964 | True      |                          0.34188 |                 82.96 |         0     | N/A            | N/A                             |
|   250 | N    |         0.34753 | True      |                          0.88218 |                 88.26 |         0     | N/A            | N-linked (GlcNAc...) asparagine |
|   251 | I    |         0.15242 | False     |                          0.11919 |                 90.69 |         0     | N/A            | N/A                             |
|   252 | T    |         0.10006 | False     |                          0.16193 |                 92.45 |         0     | N/A            | N/A                             |
|   253 | T    |         0.0084  | False     |                          0       |                 91.01 |         0     | N/A            | N/A                             |
|   254 | C    |         0.007   | False     |                          0       |                 92.45 |         0     | N/A            | N/A                             |
|   255 | H    |         0.04994 | False     |                          0.12644 |                 88.93 |         0     | N/A            | N/A                             |
|   256 | D    |         0.08018 | False     |                          0.10019 |                 82.09 |         0     | N/A            | N/A                             |
|   257 | V    |         0.06552 | False     |                          0.01664 |                 73.27 |         0     | N/A            | N/A                             |
|   258 | L    |         0.1368  | False     |                          0.10095 |                 69.46 |         0     | N/A            | N/A                             |
|   259 | N    |         0.26    | True      |                          0.36289 |                 65.17 |         0     | N/A            | N-linked (GlcNAc...) asparagine |
|   260 | E    |         0.15844 | False     |                          0.20726 |                 58.25 |         0     | N/A            | N/A                             |
|   261 | T    |         0.41912 | True      |                          0.70928 |                 59.69 |         0     | N/A            | N/A                             |
|   262 | L    |         0.32114 | True      |                          0.39404 |                 65.03 |         0     | N/A            | N/A                             |
|   263 | L    |         0.14912 | False     |                          0.18878 |                 65.21 |         0     | N/A            | N/A                             |
|   264 | E    |         0.37907 | True      |                          0.43935 |                 66.36 |         0     | N/A            | N/A                             |
|   265 | G    |         0.41514 | True      |                          0.49354 |                 77.2  |         3.532 | N/A            | N/A                             |
|   266 | Y    |         0.29742 | True      |                          0.41673 |                 82.3  |        42.773 | N/A            | N/A                             |
|   267 | Y    |         0.02032 | False     |                          0.00509 |                 82.77 |        73.955 | N/A            | N/A                             |
|   268 | A    |         0.08088 | False     |                          0.14421 |                 81.44 |        82.995 | N/A            | N/A                             |
|   269 | Y    |         0.24255 | True      |                          0.77648 |                 86.06 |        93.794 | N/A            | N/A                             |
|   270 | Y    |         0.13474 | False     |                          0.11467 |                 89.32 |        96.957 | N/A            | N/A                             |
|   271 | F    |         0.00757 | False     |                          0       |                 87.61 |        97.873 | N/A            | N/A                             |
|   272 | S    |         0.05495 | False     |                          0.20674 |                 86.88 |        97.927 | N/A            | N/A                             |
|   273 | A    |         0.03865 | False     |                          0.37622 |                 87.58 |        98.539 | N/A            | N/A                             |
|   274 | F    |         0.03263 | False     |                          0.05779 |                 87.66 |        99.264 | N/A            | N/A                             |
|   275 | S    |         0.00697 | False     |                          0       |                 88.12 |        99.288 | N/A            | N/A                             |
|   276 | A    |         0.05204 | False     |                          0.43785 |                 86    |        99.728 | N/A            | N/A                             |
|   277 | V    |         0.041   | False     |                          0.61901 |                 88.61 |        99.789 | N/A            | N/A                             |
|   278 | F    |         0.01806 | False     |                          0.14337 |                 89.94 |        99.748 | N/A            | N/A                             |
|   279 | F    |         0.0314  | False     |                          0.01465 |                 92.09 |        99.211 | N/A            | N/A                             |
|   280 | F    |         0.02138 | False     |                          0.36527 |                 92.28 |        92.615 | N/A            | N/A                             |
|   281 | V    |         0.01572 | False     |                          0.53887 |                 93.62 |        11.361 | N/A            | N/A                             |
|   282 | P    |         0.00592 | False     |                          0.02684 |                 95.32 |         4.809 | N/A            | N/A                             |
|   283 | L    |         0.01236 | False     |                          0.25967 |                 94.73 |         6.19  | N/A            | N/A                             |
|   284 | I    |         0.02156 | False     |                          0.65736 |                 95.23 |         8.599 | N/A            | N/A                             |
|   285 | I    |         0.01427 | False     |                          0.36298 |                 96.08 |         9.863 | N/A            | N/A                             |
|   286 | S    |         0.00526 | False     |                          0.01295 |                 95.13 |         9.975 | N/A            | N/A                             |
|   287 | T    |         0.02174 | False     |                          0.3516  |                 95.84 |        10.898 | N/A            | N/A                             |
|   288 | V    |         0.01307 | False     |                          0.60552 |                 96.82 |        12.246 | N/A            | N/A                             |
|   289 | C    |         0.02001 | False     |                          0.0489  |                 95.65 |        12.235 | N/A            | N/A                             |
|   290 | Y    |         0.01887 | False     |                          0.22405 |                 94.71 |        12.831 | N/A            | N/A                             |
|   291 | V    |         0.00974 | False     |                          0.33799 |                 95.66 |        12.728 | N/A            | N/A                             |
|   292 | S    |         0.03348 | False     |                          0.20195 |                 94.77 |        11.381 | N/A            | N/A                             |
|   293 | I    |         0.00753 | False     |                          0.0056  |                 92.86 |        11.191 | N/A            | N/A                             |
|   294 | I    |         0.06638 | False     |                          0.35498 |                 91.91 |        10.418 | N/A            | N/A                             |
|   295 | R    |         0.10169 | False     |                          0.66653 |                 92.44 |         0.001 | N/A            | N/A                             |
|   296 | C    |         0.07882 | False     |                          0.28547 |                 90.1  |         0.001 | N/A            | N/A                             |
|   297 | L    |         0.08351 | False     |                          0.07831 |                 88.22 |         0.001 | N/A            | N/A                             |
|   298 | S    |         0.12811 | False     |                          0.63537 |                 86.67 |         0     | N/A            | N/A                             |
|   299 | S    |         0.22506 | True      |                          0.79386 |                 84.29 |         0     | N/A            | N/A                             |
|   300 | S    |         0.18294 | True      |                          0.33817 |                 77.71 |         0     | N/A            | N/A                             |
|   301 | A    |         0.17181 | True      |                          1.05099 |                 73.02 |         0     | N/A            | N/A                             |
|   302 | V    |         0.21315 | True      |                          0.33938 |                 65.32 |         0     | N/A            | N/A                             |
|   303 | A    |         0.21262 | True      |                          1.08746 |                 62.81 |         0     | N/A            | N/A                             |
|   304 | N    |         0.23513 | True      |                          0.38198 |                 79.48 |         0     | N/A            | N/A                             |
|   305 | R    |         0.27908 | True      |                          0.8435  |                 82.14 |         0     | N/A            | N/A                             |
|   306 | S    |         0.14567 | False     |                          0.60746 |                 81.43 |         0     | N/A            | N/A                             |
|   307 | K    |         0.15822 | False     |                          0.62433 |                 80.57 |         0     | N/A            | N/A                             |
|   308 | K    |         0.17023 | False     |                          0.30102 |                 83.18 |         0     | N/A            | N/A                             |
|   309 | S    |         0.08852 | False     |                          0.53385 |                 85.45 |         0     | N/A            | N/A                             |
|   310 | R    |         0.07333 | False     |                          0.38308 |                 84.7  |         0.001 | N/A            | N/A                             |
|   311 | A    |         0.03945 | False     |                          0.20702 |                 84.25 |        32.896 | N/A            | N/A                             |
|   312 | L    |         0.06211 | False     |                          0.38992 |                 88.35 |        71.801 | N/A            | N/A                             |
|   313 | F    |         0.04211 | False     |                          0.54469 |                 88.45 |        90.022 | N/A            | N/A                             |
|   314 | L    |         0.0263  | False     |                          0.04122 |                 87.14 |        91.508 | N/A            | N/A                             |
|   315 | S    |         0.0126  | False     |                          0.07189 |                 88.75 |        91.78  | N/A            | N/A                             |
|   316 | A    |         0.01897 | False     |                          0.21897 |                 90.91 |        93.974 | N/A            | N/A                             |
|   317 | A    |         0.00821 | False     |                          0.23778 |                 90.14 |        96.569 | N/A            | N/A                             |
|   318 | V    |         0.00652 | False     |                          0.01999 |                 89.04 |        99.637 | N/A            | N/A                             |
|   319 | F    |         0.02907 | False     |                          0.12436 |                 92.33 |        99.897 | N/A            | N/A                             |
|   320 | C    |         0.00891 | False     |                          0.43635 |                 92.38 |        99.909 | N/A            | N/A                             |
|   321 | I    |         0.0098  | False     |                          0.088   |                 90.94 |        99.98  | N/A            | N/A                             |
|   322 | F    |         0.00614 | False     |                          0.00921 |                 90.61 |        99.969 | N/A            | N/A                             |
|   323 | I    |         0.019   | False     |                          0.39177 |                 92.14 |        99.749 | N/A            | N/A                             |
|   324 | I    |         0.0183  | False     |                          0.62846 |                 91.99 |        97.122 | N/A            | N/A                             |
|   325 | C    |         0.00961 | False     |                          0.0355  |                 90.81 |        68.408 | N/A            | N/A                             |
|   326 | F    |         0.00796 | False     |                          0.02548 |                 91.73 |        63.254 | N/A            | N/A                             |
|   327 | G    |         0.01287 | False     |                          0.08996 |                 91.79 |         0.055 | N/A            | N/A                             |
|   328 | P    |         0.01519 | False     |                          0.41283 |                 91.92 |         0.015 | N/A            | N/A                             |
|   329 | T    |         0.00528 | False     |                          0.01596 |                 89.56 |         0.62  | N/A            | N/A                             |
|   330 | N    |         0.00428 | False     |                          0       |                 90.55 |         2.885 | N/A            | N/A                             |
|   331 | V    |         0.02081 | False     |                          0.55398 |                 89.86 |        72.723 | N/A            | N/A                             |
|   332 | L    |         0.03307 | False     |                          0.25014 |                 85.53 |        75.4   | N/A            | N/A                             |
|   333 | L    |         0.00676 | False     |                          0.00412 |                 83.76 |        75.885 | N/A            | N/A                             |
|   334 | I    |         0.04506 | False     |                          0.20159 |                 83.81 |        75.926 | N/A            | N/A                             |
|   335 | A    |         0.03527 | False     |                          0.22302 |                 82.22 |        74.791 | N/A            | N/A                             |
|   336 | H    |         0.06071 | False     |                          0.13116 |                 76.2  |        35.765 | N/A            | N/A                             |
|   337 | Y    |         0.07014 | False     |                          0.04375 |                 75.2  |        35.522 | N/A            | N/A                             |
|   338 | S    |         0.13546 | False     |                          0.30169 |                 74.49 |        32.564 | N/A            | N/A                             |
|   339 | F    |         0.14723 | False     |                          0.74525 |                 66.84 |        32.21  | N/A            | N/A                             |
|   340 | L    |         0.07427 | False     |                          0.14591 |                 63.07 |        27.711 | N/A            | N/A                             |
|   341 | S    |         0.19489 | True      |                          0.13522 |                 59.41 |         3.085 | N/A            | N/A                             |
|   342 | H    |         0.27519 | True      |                          0.73685 |                 57.94 |         0     | N/A            | N/A                             |
|   343 | T    |         0.25847 | True      |                          0.46197 |                 56.95 |         0     | N/A            | N/A                             |
|   344 | S    |         0.20132 | True      |                          0.64962 |                 53.1  |         0     | N/A            | N/A                             |
|   345 | T    |         0.09813 | False     |                          0.52388 |                 59.06 |         0     | N/A            | N/A                             |
|   346 | T    |         0.09213 | False     |                          0.04201 |                 64.64 |         0     | N/A            | N/A                             |
|   347 | E    |         0.09849 | False     |                          0.21795 |                 66.88 |         0     | N/A            | N/A                             |
|   348 | A    |         0.10372 | False     |                          0.67689 |                 77.12 |        13.398 | N/A            | N/A                             |
|   349 | A    |         0.0286  | False     |                          0.10743 |                 77.03 |        29.255 | N/A            | N/A                             |
|   350 | Y    |         0.05049 | False     |                          0.07713 |                 76.88 |        80.493 | N/A            | N/A                             |
|   351 | F    |         0.11849 | False     |                          0.41796 |                 84.6  |        95.118 | N/A            | N/A                             |
|   352 | A    |         0.01612 | False     |                          0.29207 |                 87.01 |        96.203 | N/A            | N/A                             |
|   353 | Y    |         0.04896 | False     |                          0.09307 |                 85.56 |        97.463 | N/A            | N/A                             |
|   354 | L    |         0.02746 | False     |                          0.04946 |                 87.69 |        97.66  | N/A            | N/A                             |
|   355 | L    |         0.0414  | False     |                          0.40146 |                 90.62 |        96.45  | N/A            | N/A                             |
|   356 | C    |         0.00949 | False     |                          0.14332 |                 91.81 |        88.314 | N/A            | N/A                             |
|   357 | V    |         0.01637 | False     |                          0.05617 |                 90.51 |        86.707 | N/A            | N/A                             |
|   358 | C    |         0.00839 | False     |                          0.01996 |                 93    |        67.448 | N/A            | N/A                             |
|   359 | V    |         0.01121 | False     |                          0.37416 |                 93.08 |        63.372 | N/A            | N/A                             |
|   360 | S    |         0.01447 | False     |                          0.0528  |                 92.84 |        15.366 | N/A            | N/A                             |
|   361 | S    |         0.00901 | False     |                          0.01427 |                 94.09 |         9.411 | N/A            | N/A                             |
|   362 | I    |         0.02153 | False     |                          0.40878 |                 93.63 |         8.673 | N/A            | N/A                             |
|   363 | S    |         0.00343 | False     |                          0.01581 |                 92.61 |         1.173 | N/A            | N/A                             |
|   364 | C    |         0.0071  | False     |                          0.06641 |                 93.7  |         0.31  | N/A            | N/A                             |
|   365 | C    |         0.02794 | False     |                          0.17747 |                 93.4  |         0.134 | N/A            | N/A                             |
|   366 | I    |         0.019   | False     |                          0.33279 |                 91.74 |         0.127 | N/A            | N/A                             |
|   367 | D    |         0.00131 | False     |                          0.00189 |                 91.3  |         0     | N/A            | N/A                             |
|   368 | P    |         0.01508 | False     |                          0.11977 |                 88.28 |         0.596 | N/A            | N/A                             |
|   369 | L    |         0.02169 | False     |                          0.62187 |                 84.31 |        44.636 | N/A            | N/A                             |
|   370 | I    |         0.00827 | False     |                          0.03955 |                 84.32 |        54.975 | N/A            | N/A                             |
|   371 | Y    |         0.00695 | False     |                          0.00609 |                 82.24 |        54.975 | N/A            | N/A                             |
|   372 | Y    |         0.09122 | False     |                          0.34218 |                 80.94 |        54.975 | N/A            | N/A                             |
|   373 | Y    |         0.04399 | False     |                          0.40842 |                 76.72 |        54.894 | N/A            | N/A                             |
|   374 | A    |         0.01955 | False     |                          0.20247 |                 76.03 |        31.273 | N/A            | N/A                             |
|   375 | S    |         0.08386 | False     |                          0.07555 |                 74.18 |         1.443 | N/A            | N/A                             |
|   376 | S    |         0.13022 | False     |                          0.47004 |                 74.52 |         0.103 | N/A            | N/A                             |
|   377 | E    |         0.08849 | False     |                          0.35033 |                 76.16 |         0     | N/A            | N/A                             |
|   378 | C    |         0.02112 | False     |                          0.03742 |                 75.56 |         0     | N/A            | N/A                             |
|   379 | Q    |         0.06143 | False     |                          0.25403 |                 77.79 |         0     | N/A            | N/A                             |
|   380 | R    |         0.20058 | True      |                          0.66722 |                 82.05 |         0     | N/A            | N/A                             |
|   381 | Y    |         0.19978 | True      |                          0.29927 |                 81.26 |        26.209 | N/A            | N/A                             |
|   382 | V    |         0.0299  | False     |                          0.26372 |                 78.46 |        33.088 | N/A            | N/A                             |
|   383 | Y    |         0.13836 | False     |                          0.66523 |                 80.01 |        33.194 | N/A            | N/A                             |
|   384 | S    |         0.08259 | False     |                          0.37115 |                 82.72 |        33.194 | N/A            | N/A                             |
|   385 | I    |         0.11073 | False     |                          0.48238 |                 78.97 |        33.194 | N/A            | N/A                             |
|   386 | L    |         0.06193 | False     |                          0.80931 |                 78.95 |        30     | N/A            | N/A                             |
|   387 | C    |         0.10669 | False     |                          0.45193 |                 77.15 |         3.759 | N/A            | N/A                             |
|   388 | C    |         0.18825 | True      |                          0.83108 |                 58.09 |         2.141 | N/A            | N/A                             |
|   389 | K    |         0.16214 | False     |                          0.90751 |                 45.16 |         0     | N/A            | N/A                             |
|   390 | E    |         0.22219 | True      |                          0.84472 |                 37.89 |         0     | N/A            | N/A                             |
|   391 | S    |         0.16821 | False     |                          0.86325 |                 40.18 |         0     | N/A            | N/A                             |
|   392 | S    |         0.14427 | False     |                          0.77454 |                 37.53 |         0     | N/A            | N/A                             |
|   393 | D    |         0.08981 | False     |                          0.83905 |                 36.06 |         0     | N/A            | N/A                             |
|   394 | P    |         0.16264 | False     |                          0.88774 |                 40.87 |         0     | N/A            | N/A                             |
|   395 | S    |         0.0886  | False     |                          0.68049 |                 38.61 |         0     | N/A            | N/A                             |
|   396 | S    |         0.12534 | False     |                          0.7778  |                 37.9  |         0     | N/A            | N/A                             |
|   397 | Y    |         0.10896 | False     |                          0.91444 |                 34.36 |         0     | N/A            | N/A                             |
|   398 | N    |         0.12978 | False     |                          0.6388  |                 38.05 |         0     | N/A            | N/A                             |
|   399 | S    |         0.25324 | True      |                          0.97293 |                 53.57 |         0     | N/A            | N/A                             |
|   400 | S    |         0.22536 | True      |                          0.69255 |                 56.97 |         0     | N/A            | N/A                             |
|   401 | G    |         0.20011 | True      |                          1.01845 |                 45.2  |         0     | N/A            | N/A                             |
|   402 | Q    |         0.20633 | True      |                          0.75557 |                 41.8  |         0     | N/A            | N/A                             |
|   403 | L    |         0.15476 | False     |                          1.07617 |                 36.1  |         0     | N/A            | N/A                             |
|   404 | M    |         0.18167 | True      |                          0.79206 |                 37.24 |         0     | N/A            | N/A                             |
|   405 | A    |         0.14931 | False     |                          0.92217 |                 37.51 |         0     | N/A            | N/A                             |
|   406 | S    |         0.11922 | False     |                          0.65132 |                 38.96 |         0     | N/A            | N/A                             |
|   407 | K    |         0.10401 | False     |                          0.98707 |                 34.84 |         0     | N/A            | N/A                             |
|   408 | M    |         0.12393 | False     |                          0.84649 |                 34.77 |         0     | N/A            | N/A                             |
|   409 | D    |         0.18076 | True      |                          0.80593 |                 34.44 |         0     | N/A            | N/A                             |
|   410 | T    |         0.15435 | False     |                          0.66587 |                 30.66 |         0     | N/A            | N/A                             |
|   411 | C    |         0.16656 | False     |                          0.94445 |                 30.96 |         0     | N/A            | N/A                             |
|   412 | S    |         0.20087 | True      |                          0.78837 |                 31.62 |         0     | N/A            | N/A                             |
|   413 | S    |         0.16669 | False     |                          0.64549 |                 30.73 |         0     | N/A            | N/A                             |
|   414 | N    |         0.24587 | True      |                          0.99001 |                 29.65 |         0     | N/A            | N/A                             |
|   415 | L    |         0.27043 | True      |                          0.91701 |                 34.8  |         0     | N/A            | N/A                             |
|   416 | N    |         0.25926 | True      |                          0.8528  |                 35.17 |         0     | N/A            | N/A                             |
|   417 | N    |         0.24498 | True      |                          0.96863 |                 38.44 |         0     | N/A            | N/A                             |
|   418 | S    |         0.19387 | True      |                          0.72365 |                 42.86 |         0     | Phosphoserine  | N/A                             |
|   419 | I    |         0.17371 | True      |                          0.80518 |                 42.36 |         0     | N/A            | N/A                             |
|   420 | Y    |         0.21483 | True      |                          0.79259 |                 41.46 |         0     | N/A            | N/A                             |
|   421 | K    |         0.23249 | True      |                          0.87627 |                 43.4  |         0     | N/A            | N/A                             |
|   422 | K    |         0.2037  | True      |                          0.87208 |                 44.85 |         0     | N/A            | N/A                             |
|   423 | L    |         0.21462 | True      |                          0.88027 |                 48.5  |         0     | N/A            | N/A                             |
|   424 | L    |         0.11315 | False     |                          1.00724 |                 46.63 |         0     | N/A            | N/A                             |
|   425 | T    |         0.10572 | False     |                          1.23034 |                 55.56 |         0     | N/A            | N/A                             |


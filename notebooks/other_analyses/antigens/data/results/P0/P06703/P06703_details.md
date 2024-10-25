# Detailed Data for P06703


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: P06703
- **Gene Name**: S100A6
- **Protein Name**: S100 calcium binding protein A6
- **Swiss Prot**: nan
- **Family**: transporter
- **Biomarker Application**: diagnosis,unspecified application
- **Number of Isoforms**: 0
- **Regulation**: 1
- **(transcriptomics) AUC**: nan
- **(transcriptomics) Fold Change**: nan
- **(transcriptomics) Regulation**: Downregulated
- **Discotope Epitope Count**: 19
- **Max n_uniprots (Homo)**: 2.0
- **Max n_uniprots (Hetero)**: 4.0


## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| S100A6            | CACYBP            |   0.998 |
| S100A6            | ANXA11            |   0.985 |
| S100A6            | AGER              |   0.983 |
| S100A6            | S100A10           |   0.972 |
| S100A6            | ANXA2             |   0.952 |
| S100A6            | RB1               |   0.921 |

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
| C9JRU3       | SNTN      |
| P31949       | S100A11   |
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
|            0 |          1 |            4 | Hetero        | 2m1k         |
|            0 |          1 |            2 | Homo          | 1k9k         |
|            1 |          2 |            2 | Homo          | 1k9k         |
|            0 |          1 |            1 | Homo          | 1k9p         |
|            0 |          1 |            1 | Homo          | 1k8u         |
|            0 |          1 |            1 | Homo          | 1k96         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification                 |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:-----------------------------|
|     1 | M    |         0.42895 | False     |                          1.32127 |                 57    |         0     | N/A                          |
|     2 | A    |         0.41841 | False     |                          0.53759 |                 76.97 |         0     | N/A                          |
|     3 | C    |         0.37612 | False     |                          0.56125 |                 91.15 |         0     | N/A                          |
|     4 | P    |         0.36811 | False     |                          0.83345 |                 92.41 |         0     | N/A                          |
|     5 | L    |         0.56494 | True      |                          0.76431 |                 92.01 |         0     | N/A                          |
|     6 | D    |         0.41749 | False     |                          0.48759 |                 92.97 |         0     | N/A                          |
|     7 | Q    |         0.26957 | False     |                          0.50757 |                 93.68 |         2.624 | N/A                          |
|     8 | A    |         0.23159 | False     |                          0.41246 |                 92.57 |        69.533 | N/A                          |
|     9 | I    |         0.52188 | True      |                          0.52478 |                 93.57 |        82.774 | N/A                          |
|    10 | G    |         0.21347 | False     |                          0.43868 |                 94.21 |        83.961 | N/A                          |
|    11 | L    |         0.43774 | False     |                          0.7     |                 93.91 |        96.912 | N/A                          |
|    12 | L    |         0.23556 | False     |                          0.42784 |                 93.49 |        98.847 | N/A                          |
|    13 | V    |         0.4601  | False     |                          0.36464 |                 94.36 |        98.843 | N/A                          |
|    14 | A    |         0.3021  | False     |                          0.54133 |                 93.52 |        98.511 | N/A                          |
|    15 | I    |         0.33003 | False     |                          0.24308 |                 94.29 |        98.209 | N/A                          |
|    16 | F    |         0.04172 | False     |                          0.00637 |                 94.07 |        92.543 | N/A                          |
|    17 | H    |         0.38793 | False     |                          0.52284 |                 92.78 |         0.681 | N/A                          |
|    18 | K    |         0.42144 | False     |                          0.56381 |                 93.18 |         0     | N/A                          |
|    19 | Y    |         0.07045 | False     |                          0.01142 |                 92.72 |         0     | N/A                          |
|    20 | S    |         0.1751  | False     |                          0.08932 |                 91.91 |         0     | N/A                          |
|    21 | G    |         0.36779 | False     |                          0.30239 |                 85.89 |         0     | N/A                          |
|    22 | R    |         0.5142  | True      |                          0.46606 |                 85.16 |         0     | N/A                          |
|    23 | E    |         0.67651 | True      |                          0.53558 |                 77.9  |         0     | N/A                          |
|    24 | G    |         0.59061 | True      |                          0.55138 |                 76.96 |         0     | N/A                          |
|    25 | D    |         0.46992 | False     |                          0.43682 |                 85.14 |         0     | N/A                          |
|    26 | K    |         0.51157 | True      |                          0.72344 |                 85.69 |         0     | N/A                          |
|    27 | H    |         0.57424 | True      |                          0.67079 |                 89.75 |         0     | N/A                          |
|    28 | T    |         0.26698 | False     |                          0.12049 |                 93.16 |         0     | N/A                          |
|    29 | L    |         0.00741 | False     |                          0       |                 93.27 |         0     | N/A                          |
|    30 | S    |         0.44325 | False     |                          0.17631 |                 91.7  |         0     | N/A                          |
|    31 | K    |         0.30896 | False     |                          0.49212 |                 89.18 |         0     | N/A                          |
|    32 | K    |         0.4205  | False     |                          0.57267 |                 90.13 |         0     | N/A                          |
|    33 | E    |         0.09527 | False     |                          0.01595 |                 92.5  |         0     | N/A                          |
|    34 | L    |         0.01479 | False     |                          0       |                 91.22 |         0     | N/A                          |
|    35 | K    |         0.3566  | False     |                          0.25214 |                 89.8  |         0     | N/A                          |
|    36 | E    |         0.49244 | True      |                          0.22723 |                 91.56 |         0     | N/A                          |
|    37 | L    |         0.09245 | False     |                          0.01649 |                 92.65 |         0     | N/A                          |
|    38 | I    |         0.0252  | False     |                          0       |                 89.84 |         0     | N/A                          |
|    39 | Q    |         0.50547 | True      |                          0.37884 |                 89.1  |         0     | N/A                          |
|    40 | K    |         0.66664 | True      |                          0.64615 |                 90.63 |         0     | N6-acetyllysine              |
|    41 | E    |         0.44113 | False     |                          0.31826 |                 90.72 |         0     | N/A                          |
|    42 | L    |         0.41111 | False     |                          0.17243 |                 86.28 |         0     | N/A                          |
|    43 | T    |         0.35009 | False     |                          0.83207 |                 82.01 |         0     | N/A                          |
|    44 | I    |         0.54259 | True      |                          0.37038 |                 79.49 |         0     | N/A                          |
|    45 | G    |         0.04074 | False     |                          0.00119 |                 76.72 |         0     | N/A                          |
|    46 | S    |         0.36351 | False     |                          0.73688 |                 76.89 |         0     | Phosphoserine                |
|    47 | K    |         0.59775 | True      |                          0.83907 |                 80.67 |         0     | N6-acetyllysine; alternate   |
|    47 | K    |         0.59775 | True      |                          0.83907 |                 80.67 |         0     | N6-succinyllysine; alternate |
|    48 | L    |         0.45965 | False     |                          0.29194 |                 81.01 |         0     | N/A                          |
|    49 | Q    |         0.50871 | True      |                          0.6677  |                 85.21 |         0     | N/A                          |
|    50 | D    |         0.40652 | False     |                          0.53849 |                 86.16 |         0     | N/A                          |
|    51 | A    |         0.31417 | False     |                          0.57225 |                 88.18 |         0     | N/A                          |
|    52 | E    |         0.3605  | False     |                          0.37471 |                 86.86 |         0     | N/A                          |
|    53 | I    |         0.05938 | False     |                          0.0096  |                 87.52 |         0     | N/A                          |
|    54 | A    |         0.26893 | False     |                          0.17495 |                 88.48 |         0     | N/A                          |
|    55 | R    |         0.54416 | True      |                          0.6099  |                 88.94 |         0     | N/A                          |
|    56 | L    |         0.31425 | False     |                          0.2472  |                 87.48 |         0     | N/A                          |
|    57 | M    |         0.18442 | False     |                          0.07539 |                 88.42 |         0     | N/A                          |
|    58 | E    |         0.34884 | False     |                          0.68228 |                 89.78 |         0     | N/A                          |
|    59 | D    |         0.48345 | True      |                          0.66166 |                 88.99 |         0     | N/A                          |
|    60 | L    |         0.17505 | False     |                          0.08839 |                 90.06 |         0     | N/A                          |
|    61 | D    |         0.42123 | False     |                          0.07776 |                 90.67 |         0     | N/A                          |
|    62 | R    |         0.49275 | True      |                          0.66439 |                 87.8  |         0     | N/A                          |
|    63 | N    |         0.38461 | False     |                          0.5674  |                 89.98 |         0     | N/A                          |
|    64 | K    |         0.65806 | True      |                          0.84775 |                 87.75 |         0     | N/A                          |
|    65 | D    |         0.47256 | False     |                          0.41748 |                 90.69 |         0     | N/A                          |
|    66 | Q    |         0.45716 | False     |                          0.70831 |                 87.97 |         0     | N/A                          |
|    67 | E    |         0.38982 | False     |                          0.24865 |                 91.71 |         0     | N/A                          |
|    68 | V    |         0.01104 | False     |                          0.00095 |                 93.26 |         0     | N/A                          |
|    69 | N    |         0.37509 | False     |                          0.26262 |                 93.86 |         0     | N/A                          |
|    70 | F    |         0.4846  | True      |                          0.39997 |                 92.06 |         0     | N/A                          |
|    71 | Q    |         0.36432 | False     |                          0.70746 |                 92.86 |         0     | N/A                          |
|    72 | E    |         0.09585 | False     |                          0.03786 |                 93.23 |         0     | N/A                          |
|    73 | Y    |         0.04381 | False     |                          0.01188 |                 93.25 |        64.506 | N/A                          |
|    74 | V    |         0.39257 | False     |                          0.50108 |                 93.16 |        82.818 | N/A                          |
|    75 | T    |         0.30257 | False     |                          0.37295 |                 91.73 |        87.053 | N/A                          |
|    76 | F    |         0.16371 | False     |                          0.03842 |                 90.78 |        94.225 | N/A                          |
|    77 | L    |         0.27703 | False     |                          0.16723 |                 91.63 |        94.8   | N/A                          |
|    78 | G    |         0.51877 | True      |                          0.41379 |                 91.71 |        93.658 | N/A                          |
|    79 | A    |         0.22213 | False     |                          0.4808  |                 88.94 |        94.636 | N/A                          |
|    80 | L    |         0.18164 | False     |                          0.07749 |                 87.17 |        95.27  | N/A                          |
|    81 | A    |         0.29074 | False     |                          0.53893 |                 89.31 |        94.519 | N/A                          |
|    82 | L    |         0.47496 | False     |                          0.72049 |                 89.04 |        93.879 | N/A                          |
|    83 | I    |         0.33785 | False     |                          0.62509 |                 86.3  |        90.39  | N/A                          |
|    84 | Y    |         0.3482  | False     |                          0.40835 |                 83.31 |        51.668 | N/A                          |
|    85 | N    |         0.27053 | False     |                          0.43611 |                 86.53 |         1.994 | N/A                          |
|    86 | E    |         0.35879 | False     |                          0.59961 |                 86.77 |         0.052 | N/A                          |
|    87 | A    |         0.38872 | False     |                          0.68334 |                 82    |         0.052 | N/A                          |
|    88 | L    |         0.34518 | False     |                          0.93968 |                 79.55 |         0.052 | N/A                          |
|    89 | K    |         0.27395 | False     |                          0.79038 |                 76.48 |         0.052 | N/A                          |
|    90 | G    |         0.21975 | False     |                          1.39266 |                 60.8  |         0     | N/A                          |


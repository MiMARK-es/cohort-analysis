# Detailed Data for P26447


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: P26447
- **Gene Name**: S100A4
- **Protein Name**: S100 calcium binding protein A4
- **Swiss Prot**: S10A4_HUMAN
- **Family**: other
- **Biomarker Application**: disease progression
- **Number of Isoforms**: 0
- **Regulation**: 1
- **(transcriptomics) AUC**: nan
- **(transcriptomics) Fold Change**: nan
- **(transcriptomics) Regulation**: Downregulated
- **Discotope Epitope Count**: 17
- **Max n_uniprots (Homo)**: 10
- **Max n_uniprots (Hetero)**: 4


## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| S100A4            | ANXA2             |   0.999 |
| S100A4            | MYH9              |   0.997 |
| S100A4            | TP53              |   0.996 |
| S100A4            | AGER              |   0.988 |

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
| P60903       | S100A10   |
| Q96FQ6       | S100A16   |
| P05109       | S100A8    |
| P06703       | S100A6    |
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
|            0 |          1 |            2 | Homo          | 1m31         |
|            0 |          1 |            4 | Hetero        | 5lpu         |
|            0 |          1 |            2 | Homo          | 7psq         |
|            1 |          2 |            2 | Homo          | 7psq         |
|            0 |          1 |            1 | Homo          | 6t58         |
|            1 |          2 |            1 | Homo          | 6t58         |
|            0 |          1 |            2 | Homo          | 2q91         |
|            0 |          1 |            2 | Homo          | 3ko0         |
|            1 |          2 |            2 | Homo          | 3ko0         |
|            2 |          3 |            2 | Homo          | 3ko0         |
|            3 |          4 |            2 | Homo          | 3ko0         |
|            4 |          5 |            2 | Homo          | 3ko0         |
|            5 |          6 |            2 | Homo          | 3ko0         |
|            6 |          7 |            2 | Homo          | 3ko0         |
|            7 |          8 |            2 | Homo          | 3ko0         |
|            8 |          9 |            2 | Homo          | 3ko0         |
|            9 |         10 |            2 | Homo          | 3ko0         |
|            0 |          1 |            3 | Hetero        | 4cfq         |
|            1 |          2 |            3 | Hetero        | 4cfq         |
|            0 |          1 |            2 | Homo          | 4hsz         |
|            1 |          2 |            2 | Homo          | 4hsz         |
|            0 |          1 |            3 | Hetero        | 2lnk         |
|            0 |          1 |            2 | Homo          | 2mrd         |
|            0 |          1 |            3 | Hetero        | 4eto         |
|            0 |          1 |            2 | Homo          | 3c1v         |
|            1 |          2 |            2 | Homo          | 3c1v         |
|            0 |          1 |            3 | Hetero        | 3zwh         |
|            0 |          1 |            3 | Hetero        | 4cfr         |
|            0 |          1 |            2 | Homo          | 7psp         |
|            0 |          1 |           10 | Homo          | 3m0w         |
|            1 |          2 |            2 | Homo          | 3m0w         |
|            2 |          3 |            2 | Homo          | 3m0w         |
|            3 |          4 |            2 | Homo          | 3m0w         |
|            4 |          5 |            2 | Homo          | 3m0w         |
|            5 |          6 |            2 | Homo          | 3m0w         |
|            0 |          1 |            2 | Homo          | 3cga         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification    |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:----------------|
|     1 | M    |         0.50067 | True      |                          1.27144 |                 63.7  |         0     | N/A             |
|     2 | A    |         0.33314 | False     |                          0.47507 |                 82.19 |         0     | N-acetylalanine |
|     3 | C    |         0.38081 | False     |                          0.56688 |                 94.79 |         0     | N/A             |
|     4 | P    |         0.43558 | False     |                          0.85212 |                 96.03 |         0     | N/A             |
|     5 | L    |         0.50284 | True      |                          0.79623 |                 95.69 |         0     | N/A             |
|     6 | E    |         0.33992 | False     |                          0.4781  |                 96.32 |         0     | N/A             |
|     7 | K    |         0.39329 | False     |                          0.55623 |                 96.41 |         0.152 | N6-acetyllysine |
|     8 | A    |         0.28556 | False     |                          0.52449 |                 95.23 |         0.152 | N/A             |
|     9 | L    |         0.43786 | False     |                          0.55054 |                 96.8  |         0.152 | N/A             |
|    10 | D    |         0.31911 | False     |                          0.58204 |                 97.08 |         0.152 | N/A             |
|    11 | V    |         0.35455 | False     |                          0.6655  |                 96.93 |        20.868 | N/A             |
|    12 | M    |         0.2854  | False     |                          0.22831 |                 96.56 |        22.594 | N/A             |
|    13 | V    |         0.45736 | False     |                          0.4151  |                 97.51 |        22.594 | N/A             |
|    14 | S    |         0.52601 | True      |                          0.45852 |                 96.81 |        22.594 | N/A             |
|    15 | T    |         0.23243 | False     |                          0.13625 |                 97.74 |        22.594 | N/A             |
|    16 | F    |         0.01493 | False     |                          0.00191 |                 97.85 |        22.37  | N/A             |
|    17 | H    |         0.31569 | False     |                          0.50588 |                 96.85 |         0.149 | N/A             |
|    18 | K    |         0.41981 | False     |                          0.60146 |                 96.91 |         0     | N/A             |
|    19 | Y    |         0.03553 | False     |                          0.00509 |                 97.42 |         0     | N/A             |
|    20 | S    |         0.16243 | False     |                          0.09626 |                 96.57 |         0     | N/A             |
|    21 | G    |         0.35921 | False     |                          0.38197 |                 91.01 |         0     | N/A             |
|    22 | K    |         0.43857 | False     |                          0.52312 |                 91.84 |         0     | N/A             |
|    23 | E    |         0.57163 | True      |                          0.60401 |                 86.94 |         0     | N/A             |
|    24 | G    |         0.56759 | True      |                          0.89524 |                 89.54 |         0     | N/A             |
|    25 | D    |         0.53862 | True      |                          0.33102 |                 91.9  |         0     | N/A             |
|    26 | K    |         0.5415  | True      |                          0.64722 |                 92.74 |         0     | N/A             |
|    27 | F    |         0.63749 | True      |                          0.61103 |                 94.92 |         0     | N/A             |
|    28 | K    |         0.35039 | False     |                          0.22232 |                 97.5  |         0     | N/A             |
|    29 | L    |         0.0058  | False     |                          0       |                 97.62 |         0     | N/A             |
|    30 | N    |         0.3362  | False     |                          0.17877 |                 95.61 |         0     | N/A             |
|    31 | K    |         0.35781 | False     |                          0.3821  |                 93.66 |         0     | N/A             |
|    32 | S    |         0.37034 | False     |                          0.54847 |                 93.63 |         0     | N/A             |
|    33 | E    |         0.09713 | False     |                          0.02913 |                 96.44 |         0     | N/A             |
|    34 | L    |         0.00826 | False     |                          0       |                 95.15 |         0     | N/A             |
|    35 | K    |         0.3357  | False     |                          0.36785 |                 92.97 |         0     | N6-acetyllysine |
|    36 | E    |         0.42087 | False     |                          0.26336 |                 94.19 |         0     | N/A             |
|    37 | L    |         0.02272 | False     |                          0.0033  |                 95.65 |         0     | N/A             |
|    38 | L    |         0.0159  | False     |                          0       |                 92.55 |         0     | N/A             |
|    39 | T    |         0.32722 | False     |                          0.51839 |                 91.03 |         0     | N/A             |
|    40 | R    |         0.70532 | True      |                          0.6442  |                 94.1  |         0     | N/A             |
|    41 | E    |         0.4057  | False     |                          0.34114 |                 94.3  |         0     | N/A             |
|    42 | L    |         0.35905 | False     |                          0.27286 |                 89.32 |         0     | N/A             |
|    43 | P    |         0.50061 | True      |                          0.60283 |                 86.88 |         0     | N/A             |
|    44 | S    |         0.48662 | True      |                          0.85142 |                 82.79 |         0     | N/A             |
|    45 | F    |         0.65493 | True      |                          0.40184 |                 77.69 |         0     | N/A             |
|    46 | L    |         0.24971 | False     |                          0.14289 |                 73.97 |         0     | N/A             |
|    47 | G    |         0.34843 | False     |                          0.53838 |                 68.69 |         0     | N/A             |
|    48 | K    |         0.42879 | False     |                          1.05602 |                 64.14 |         0     | N/A             |
|    49 | R    |         0.46446 | True      |                          0.90403 |                 58.55 |         0     | N/A             |
|    50 | T    |         0.27546 | False     |                          0.3018  |                 66.01 |         0     | N/A             |
|    51 | D    |         0.33793 | False     |                          0.53638 |                 81.2  |         0     | N/A             |
|    52 | E    |         0.27937 | False     |                          0.44986 |                 86.63 |         0     | N/A             |
|    53 | A    |         0.25689 | False     |                          0.64364 |                 88.17 |         0     | N/A             |
|    54 | A    |         0.26533 | False     |                          0.546   |                 86.15 |         0     | N/A             |
|    55 | F    |         0.03927 | False     |                          0.00686 |                 89.58 |         0     | N/A             |
|    56 | Q    |         0.38674 | False     |                          0.43697 |                 90.63 |         0     | N/A             |
|    57 | K    |         0.41126 | False     |                          0.70372 |                 90.57 |         0     | N/A             |
|    58 | L    |         0.18402 | False     |                          0.18501 |                 89.87 |         0     | N/A             |
|    59 | M    |         0.1194  | False     |                          0.04027 |                 92.2  |         0     | N/A             |
|    60 | S    |         0.33886 | False     |                          0.58405 |                 92.83 |         0     | N/A             |
|    61 | N    |         0.38728 | False     |                          0.64884 |                 91.57 |         0     | N/A             |
|    62 | L    |         0.11963 | False     |                          0.0877  |                 93.34 |         0     | N/A             |
|    63 | D    |         0.37501 | False     |                          0.07888 |                 95.02 |         0     | N/A             |
|    64 | S    |         0.37814 | False     |                          0.67509 |                 94.03 |         0     | N/A             |
|    65 | N    |         0.35511 | False     |                          0.54462 |                 95.04 |         0     | N/A             |
|    66 | R    |         0.57796 | True      |                          0.82909 |                 93.67 |         0     | N/A             |
|    67 | D    |         0.40972 | False     |                          0.3275  |                 95.38 |         0     | N/A             |
|    68 | N    |         0.37794 | False     |                          0.73017 |                 94.24 |         0     | N/A             |
|    69 | E    |         0.35154 | False     |                          0.19796 |                 96.33 |         0     | N/A             |
|    70 | V    |         0.00652 | False     |                          0.00095 |                 97.34 |         0     | N/A             |
|    71 | D    |         0.37542 | False     |                          0.23055 |                 97.62 |         0     | N/A             |
|    72 | F    |         0.43867 | False     |                          0.34732 |                 96.67 |         0     | N/A             |
|    73 | Q    |         0.41007 | False     |                          0.69893 |                 97.2  |         0     | N/A             |
|    74 | E    |         0.15361 | False     |                          0.06575 |                 97.44 |         0     | N/A             |
|    75 | Y    |         0.03702 | False     |                          0.02428 |                 96.54 |        14.536 | N/A             |
|    76 | C    |         0.28435 | False     |                          0.22138 |                 97.02 |        16.787 | N/A             |
|    77 | V    |         0.30312 | False     |                          0.62894 |                 95.09 |        44.124 | N/A             |
|    78 | F    |         0.15144 | False     |                          0.04699 |                 93.22 |        46.366 | N/A             |
|    79 | L    |         0.31128 | False     |                          0.21595 |                 93.4  |        46.366 | N/A             |
|    80 | S    |         0.31734 | False     |                          0.45801 |                 92.08 |        39.923 | N/A             |
|    81 | C    |         0.2806  | False     |                          0.39613 |                 88.29 |        38.969 | N/A             |
|    82 | I    |         0.28489 | False     |                          0.13279 |                 86.81 |        38.167 | N/A             |
|    83 | A    |         0.32767 | False     |                          0.57917 |                 89.61 |        28.253 | N/A             |
|    84 | M    |         0.38228 | False     |                          0.51564 |                 86.17 |        19.857 | N/A             |
|    85 | M    |         0.5191  | True      |                          0.72689 |                 80.88 |        10.948 | N/A             |
|    86 | C    |         0.47601 | True      |                          0.71641 |                 78.46 |         0.695 | N/A             |
|    87 | N    |         0.32915 | False     |                          0.43537 |                 79.15 |         0     | N/A             |
|    88 | E    |         0.32244 | False     |                          0.68968 |                 64.5  |         0     | N/A             |
|    89 | F    |         0.41058 | False     |                          0.69606 |                 58.61 |         0     | N/A             |
|    90 | F    |         0.38994 | False     |                          0.44375 |                 55.34 |         0     | N/A             |
|    91 | E    |         0.43698 | False     |                          0.65702 |                 54.84 |         0     | N/A             |
|    92 | G    |         0.43223 | False     |                          0.92462 |                 57.81 |         0     | N/A             |
|    93 | F    |         0.4215  | False     |                          0.61658 |                 53.11 |         0     | N/A             |
|    94 | P    |         0.37297 | False     |                          0.81734 |                 53.36 |         0     | N/A             |
|    95 | D    |         0.5934  | True      |                          0.88568 |                 58.82 |         0     | N/A             |
|    96 | K    |         0.37479 | False     |                          0.87157 |                 53.47 |         0     | N/A             |
|    97 | Q    |         0.32656 | False     |                          0.8324  |                 49.83 |         0     | N/A             |
|    98 | P    |         0.33024 | False     |                          0.89027 |                 45.9  |         0     | N/A             |
|    99 | R    |         0.44994 | False     |                          0.95046 |                 53.31 |         0     | N/A             |
|   100 | K    |         0.26479 | False     |                          0.99245 |                 44.48 |         0     | N/A             |
|   101 | K    |         0.25349 | False     |                          1.30144 |                 42.26 |         0     | N/A             |


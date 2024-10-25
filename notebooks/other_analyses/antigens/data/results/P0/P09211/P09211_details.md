# Detailed Data for P09211


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: P09211
- **Gene Name**: uniprot_accession
P09211    GSTP1
P09211    GSTP1
Name: gene_name, dtype: object
- **Protein Name**: uniprot_accession
P09211    Glutathione S-transferase P
P09211    Glutathione S-transferase P
Name: protein_name, dtype: object
- **Swiss Prot**: uniprot_accession
P09211    GSTP1_HUMAN
P09211    GSTP1_HUMAN
Name: swiss_prot, dtype: object
- **Family**: uniprot_accession
P09211    enzyme
P09211       NaN
Name: family, dtype: object
- **Biomarker Application**: uniprot_accession
P09211    diagnosis,efficacy,prognosis,response to thera...
P09211                                                  NaN
Name: biomarker_application, dtype: object
- **Number of Isoforms**: 0
- **Regulation**: uniprot_accession
P09211    1
P09211    1
Name: up_down_regulated, dtype: int64
- **(transcriptomics) AUC**: nan
- **(transcriptomics) Fold Change**: nan
- **(transcriptomics) Regulation**: Downregulated
- **Discotope Epitope Count**: 30
- **Max n_uniprots (Homo)**: 2
- **Max n_uniprots (Hetero)**: N/A


## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| GSTP1             | EPHX1             |   0.989 |
| GSTP1             | CYP2E1            |   0.979 |
| GSTP1             | CYP3A4            |   0.976 |
| GSTP1             | MAPK8             |   0.974 |
| GSTP1             | CYP1A1            |   0.974 |
| GSTP1             | PRDX6             |   0.973 |
| GSTP1             | CYP1B1            |   0.973 |
| GSTP1             | CYP1A2            |   0.96  |
| GSTP1             | GSR               |   0.952 |
| GSTP1             | CYP2C9            |   0.951 |
| GSTP1             | GSTT2B            |   0.947 |
| GSTP1             | GPX4              |   0.945 |
| GSTP1             | CYP2A6            |   0.945 |
| GSTP1             | GSTZ1             |   0.945 |
| GSTP1             | TRAF2             |   0.945 |
| GSTP1             | GSS               |   0.934 |
| GSTP1             | CYP2A13           |   0.932 |
| GSTP1             | GSTO2             |   0.927 |
| GSTP1             | JUN               |   0.927 |
| GSTP1             | GSTO1             |   0.915 |

## Homologs

| uniprot_id   | gene_id   |
|:-------------|:----------|
| O60760       | HPGDS     |
| Q5JW85       | GSTA3     |
| Q5JW88       | GSTA4     |
| Q7RTV2       | GSTA5     |
| A6NNT0       | GSTM4     |
| Q6FGJ9       | GSTM3     |
| B9ZVX7       | GSTM1     |
| P08263       | GSTA1     |
| A0A140VKE2   | GSTA2     |
| E9PGV1       | GSTM2     |
| Q5T8R1       | GSTM5     |

## Biological Assemblies

|   Unnamed: 0 |   assembly |   n_uniprots | composition   | crystal_id   |
|-------------:|-----------:|-------------:|:--------------|:-------------|
|            0 |          1 |            2 | Homo          | 11gs         |
|            0 |          1 |            2 | Homo          | 3kmn         |
|            0 |          1 |            2 | Homo          | 9gss         |
|            0 |          1 |            2 | Homo          | 1md3         |
|            0 |          1 |            2 | Homo          | 1px6         |
|            0 |          1 |            2 | Homo          | 17gs         |
|            0 |          1 |            2 | Homo          | 1kbn         |
|            0 |          1 |            2 | Homo          | 2pgt         |
|            0 |          1 |            2 | Homo          | 4pgt         |
|            0 |          1 |            2 | Homo          | 2a2r         |
|            0 |          1 |            2 | Homo          | 22gs         |
|            0 |          1 |            2 | Homo          | 3dgq         |
|            0 |          1 |            2 | Homo          | 10gs         |
|            0 |          1 |            2 | Homo          | 13gs         |
|            0 |          1 |            2 | Homo          | 5ddl         |
|            0 |          1 |            2 | Homo          | 6y1e         |
|            1 |          2 |            2 | Homo          | 6y1e         |
|            0 |          1 |            2 | Homo          | 3hkr         |
|            0 |          1 |            2 | Homo          | 3csi         |
|            1 |          2 |            2 | Homo          | 3csi         |
|            0 |          1 |            2 | Homo          | 5l6x         |
|            0 |          1 |            2 | Homo          | 5gss         |
|            0 |          1 |            2 | Homo          | 2gss         |
|            0 |          1 |            2 | Homo          | 1eog         |
|            0 |          1 |            2 | Homo          | 1md4         |
|            0 |          1 |            2 | Homo          | 19gs         |
|            0 |          1 |            2 | Homo          | 5djm         |
|            0 |          1 |            2 | Homo          | 5dcg         |
|            0 |          1 |            2 | Homo          | 16gs         |
|            0 |          1 |            2 | Homo          | 7gss         |
|            0 |          1 |            2 | Homo          | 5x79         |
|            0 |          1 |            2 | Homo          | 1pgt         |
|            0 |          1 |            2 | Homo          | 4gss         |
|            0 |          1 |            2 | Homo          | 5dak         |
|            0 |          1 |            2 | Homo          | 5djl         |
|            0 |          1 |            2 | Homo          | 5jcw         |
|            0 |          1 |            2 | Homo          | 6ap9         |
|            0 |          1 |            2 | Homo          | 7xba         |
|            0 |          1 |            2 | Homo          | 1lbk         |
|            0 |          1 |            2 | Homo          | 5j41         |
|            0 |          1 |            2 | Homo          | 1aqv         |
|            0 |          1 |            2 | Homo          | 3gss         |
|            0 |          1 |            2 | Homo          | 2a2s         |
|            0 |          1 |            2 | Homo          | 1aqw         |
|            1 |          2 |            2 | Homo          | 1aqw         |
|            0 |          1 |            2 | Homo          | 1zgn         |
|            0 |          1 |            1 | Homo          | 6llx         |
|            1 |          2 |            1 | Homo          | 6llx         |
|            0 |          1 |            2 | Homo          | 3csj         |
|            0 |          1 |            2 | Homo          | 5dal         |
|            0 |          1 |            2 | Homo          | 3ie3         |
|            0 |          1 |            2 | Homo          | 1aqx         |
|            1 |          2 |            2 | Homo          | 1aqx         |
|            0 |          1 |            2 | Homo          | 1gss         |
|            0 |          1 |            2 | Homo          | 12gs         |
|            0 |          1 |            2 | Homo          | 3km6         |
|            0 |          1 |            2 | Homo          | 8gss         |
|            1 |          2 |            1 | Homo          | 8gss         |
|            0 |          1 |            2 | Homo          | 3hjo         |
|            0 |          1 |            2 | Homo          | 3pgt         |
|            0 |          1 |            2 | Homo          | 6gss         |
|            0 |          1 |            2 | Homo          | 7bia         |
|            0 |          1 |            2 | Homo          | 3gus         |
|            0 |          1 |            2 | Homo          | 3n9j         |
|            0 |          1 |            2 | Homo          | 14gs         |
|            0 |          1 |            2 | Homo          | 2j9h         |
|            0 |          1 |            2 | Homo          | 20gs         |
|            0 |          1 |            2 | Homo          | 3dd3         |
|            0 |          1 |            2 | Homo          | 1px7         |
|            0 |          1 |            2 | Homo          | 3hjm         |
|            1 |          2 |            2 | Homo          | 3hjm         |
|            0 |          1 |            2 | Homo          | 18gs         |
|            0 |          1 |            2 | Homo          | 3kmo         |
|            0 |          1 |            2 | Homo          | 3csh         |
|            0 |          1 |            2 | Homo          | 1eoh         |
|            1 |          2 |            2 | Homo          | 1eoh         |
|            2 |          3 |            2 | Homo          | 1eoh         |
|            3 |          4 |            2 | Homo          | 1eoh         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification             |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:-------------------------|
|     1 | M    |         0.22468 | False     |                          0.85849 |                 62.62 |         0     | N/A                      |
|     2 | P    |         0.1807  | False     |                          0.50128 |                 65.38 |         0     | N/A                      |
|     3 | P    |         0.17955 | False     |                          0.77416 |                 91.43 |         0.212 | N/A                      |
|     4 | Y    |         0.04226 | False     |                          0.03619 |                 98.51 |        39.676 | Phosphotyrosine; by EGFR |
|     5 | T    |         0.21646 | False     |                          0.13809 |                 98.61 |        40.79  | N/A                      |
|     6 | V    |         0.01036 | False     |                          0.00476 |                 98.76 |        41.2   | N/A                      |
|     7 | V    |         0.11582 | False     |                          0.04189 |                 98.75 |        41.2   | N/A                      |
|     8 | Y    |         0.19166 | False     |                          0.07964 |                 98.75 |        41.2   | N/A                      |
|     9 | F    |         0.38665 | True      |                          0.25824 |                 98.53 |         5.344 | N/A                      |
|    10 | P    |         0.2888  | False     |                          0.39426 |                 98.2  |         1.471 | N/A                      |
|    11 | V    |         0.27509 | False     |                          0.09045 |                 98.47 |         0     | N/A                      |
|    12 | R    |         0.17753 | False     |                          0.15785 |                 98.68 |         0     | N/A                      |
|    13 | G    |         0.22272 | False     |                          0.24927 |                 98.37 |         0     | N/A                      |
|    14 | R    |         0.20502 | False     |                          0.25627 |                 98.73 |         0     | N/A                      |
|    15 | C    |         0.02297 | False     |                          0       |                 98.8  |         0     | N/A                      |
|    16 | A    |         0.02743 | False     |                          0.01658 |                 98.81 |         0     | N/A                      |
|    17 | A    |         0.03062 | False     |                          0.03372 |                 98.9  |         0     | N/A                      |
|    18 | L    |         0.01242 | False     |                          0.00401 |                 98.78 |         0     | N/A                      |
|    19 | R    |         0.14464 | False     |                          0.0544  |                 98.8  |         0     | N/A                      |
|    20 | M    |         0.00607 | False     |                          0       |                 98.89 |         0     | N/A                      |
|    21 | L    |         0.00293 | False     |                          0       |                 98.79 |         0     | N/A                      |
|    22 | L    |         0.00232 | False     |                          0       |                 98.65 |         0     | N/A                      |
|    23 | A    |         0.07798 | False     |                          0.13048 |                 98.63 |         0     | N/A                      |
|    24 | D    |         0.11213 | False     |                          0.05395 |                 98.73 |         0     | N/A                      |
|    25 | Q    |         0.13946 | False     |                          0.23079 |                 98.41 |         0     | N/A                      |
|    26 | G    |         0.17762 | False     |                          0.55764 |                 97.53 |         0     | N/A                      |
|    27 | Q    |         0.14348 | False     |                          0.1436  |                 98.11 |         0     | N/A                      |
|    28 | S    |         0.25942 | False     |                          0.74896 |                 97.35 |         0     | N/A                      |
|    29 | W    |         0.20366 | False     |                          0.22672 |                 98.14 |         0     | N/A                      |
|    30 | K    |         0.34204 | True      |                          0.57582 |                 98.08 |         0     | N/A                      |
|    31 | E    |         0.21584 | False     |                          0.29776 |                 98.34 |         0     | N/A                      |
|    32 | E    |         0.45051 | True      |                          0.37845 |                 98.04 |         0     | N/A                      |
|    33 | V    |         0.25795 | False     |                          0.62221 |                 97.84 |         0     | N/A                      |
|    34 | V    |         0.10468 | False     |                          0.03523 |                 98.25 |         0     | N/A                      |
|    35 | T    |         0.33794 | True      |                          0.39076 |                 97.46 |         0     | N/A                      |
|    36 | V    |         0.32791 | True      |                          0.61234 |                 96.18 |         0     | N/A                      |
|    37 | E    |         0.28526 | False     |                          0.59466 |                 97.17 |         0     | N/A                      |
|    38 | T    |         0.25846 | False     |                          0.40044 |                 97.49 |         0     | N/A                      |
|    39 | W    |         0.19697 | False     |                          0.16243 |                 98.08 |         0     | N/A                      |
|    40 | Q    |         0.29965 | False     |                          0.70009 |                 97.38 |         0     | N/A                      |
|    41 | E    |         0.23158 | False     |                          0.7019  |                 97.22 |         0     | N/A                      |
|    42 | G    |         0.30383 | False     |                          0.29708 |                 96.41 |         0     | N/A                      |
|    43 | S    |         0.36396 | True      |                          0.63208 |                 97.37 |         0     | N/A                      |
|    44 | L    |         0.22727 | False     |                          0.23954 |                 97.8  |         0     | N/A                      |
|    45 | K    |         0.25615 | False     |                          0.44824 |                 97.89 |         0     | N/A                      |
|    46 | A    |         0.27641 | False     |                          0.86069 |                 98.04 |         0     | N/A                      |
|    47 | S    |         0.28895 | False     |                          0.6273  |                 97.47 |         0     | N/A                      |
|    48 | C    |         0.08536 | False     |                          0.04974 |                 98.28 |         0     | N/A                      |
|    49 | L    |         0.30911 | False     |                          0.74457 |                 98.39 |         0     | N/A                      |
|    50 | Y    |         0.46743 | True      |                          0.58097 |                 98.43 |         0     | N/A                      |
|    51 | G    |         0.44701 | True      |                          0.19521 |                 98.35 |         0     | N/A                      |
|    52 | Q    |         0.45865 | True      |                          0.57303 |                 98.54 |         0     | N/A                      |
|    53 | L    |         0.32163 | True      |                          0.09891 |                 98.68 |         0     | N/A                      |
|    54 | P    |         0.1491  | False     |                          0.03324 |                 98.78 |         0     | N/A                      |
|    55 | K    |         0.31812 | True      |                          0.25047 |                 98.82 |         0     | N/A                      |
|    56 | F    |         0.01696 | False     |                          0.00466 |                 98.82 |         0     | N/A                      |
|    57 | Q    |         0.19832 | False     |                          0.21187 |                 98.55 |         0     | N/A                      |
|    58 | D    |         0.1361  | False     |                          0.1135  |                 98.11 |         0     | N/A                      |
|    59 | G    |         0.07807 | False     |                          0.25083 |                 96.69 |         0     | N/A                      |
|    60 | D    |         0.32405 | True      |                          0.94233 |                 96.76 |         0     | N/A                      |
|    61 | L    |         0.26852 | False     |                          0.49181 |                 98.2  |         0     | N/A                      |
|    62 | T    |         0.30828 | False     |                          0.40266 |                 98.46 |         0     | Phosphothreonine         |
|    63 | L    |         0.2276  | False     |                          0.16322 |                 98.76 |         0     | N/A                      |
|    64 | Y    |         0.30603 | False     |                          0.15062 |                 98.69 |         0     | N/A                      |
|    65 | Q    |         0.28349 | False     |                          0.45843 |                 98.74 |         0     | N/A                      |
|    66 | S    |         0.15304 | False     |                          0.05811 |                 98.84 |         0     | N/A                      |
|    67 | N    |         0.14891 | False     |                          0.16519 |                 98.85 |         0     | N/A                      |
|    68 | T    |         0.24247 | False     |                          0.40851 |                 98.91 |         0     | N/A                      |
|    69 | I    |         0.0074  | False     |                          0.0008  |                 98.88 |         0     | N/A                      |
|    70 | L    |         0.01704 | False     |                          0.01401 |                 98.89 |         0     | N/A                      |
|    71 | R    |         0.17665 | False     |                          0.19275 |                 98.91 |         0     | N/A                      |
|    72 | H    |         0.0866  | False     |                          0.1024  |                 98.73 |         0     | N/A                      |
|    73 | L    |         0.00307 | False     |                          0       |                 98.64 |         0     | N/A                      |
|    74 | G    |         0.00508 | False     |                          0.00119 |                 98.67 |         0     | N/A                      |
|    75 | R    |         0.3081  | False     |                          0.55558 |                 98.64 |         0     | N/A                      |
|    76 | T    |         0.22976 | False     |                          0.54282 |                 97.91 |         0     | N/A                      |
|    77 | L    |         0.16174 | False     |                          0.22785 |                 97.91 |         0     | N/A                      |
|    78 | G    |         0.21099 | False     |                          0.66174 |                 98.07 |         0     | N/A                      |
|    79 | L    |         0.09555 | False     |                          0.05441 |                 98.76 |         0     | N/A                      |
|    80 | Y    |         0.23738 | False     |                          0.16125 |                 98.77 |         0     | N/A                      |
|    81 | G    |         0.18838 | False     |                          0.4187  |                 98.43 |         0     | N/A                      |
|    82 | K    |         0.29886 | False     |                          0.7367  |                 98.14 |         0     | N/A                      |
|    83 | D    |         0.25393 | False     |                          0.41492 |                 98.5  |         0     | N/A                      |
|    84 | Q    |         0.32112 | True      |                          0.84028 |                 98.49 |         0     | N/A                      |
|    85 | Q    |         0.2157  | False     |                          0.68223 |                 98.5  |         0     | N/A                      |
|    86 | E    |         0.12531 | False     |                          0.0947  |                 98.65 |         0     | N/A                      |
|    87 | A    |         0.09621 | False     |                          0.2232  |                 98.83 |         0     | N/A                      |
|    88 | A    |         0.2335  | False     |                          0.5747  |                 98.8  |         0     | N/A                      |
|    89 | L    |         0.22443 | False     |                          0.41877 |                 98.77 |         0     | N/A                      |
|    90 | V    |         0.00342 | False     |                          0.00095 |                 98.9  |         0     | N/A                      |
|    91 | D    |         0.17587 | False     |                          0.24254 |                 98.89 |         0     | N/A                      |
|    92 | M    |         0.22671 | False     |                          0.55854 |                 98.87 |         0     | N/A                      |
|    93 | V    |         0.02613 | False     |                          0.01333 |                 98.89 |         0     | N/A                      |
|    94 | N    |         0.0055  | False     |                          0       |                 98.91 |         0     | N/A                      |
|    95 | D    |         0.21969 | False     |                          0.43958 |                 98.88 |         0     | N/A                      |
|    96 | G    |         0.18536 | False     |                          0.34706 |                 98.83 |         0     | N/A                      |
|    97 | V    |         0.00458 | False     |                          0       |                 98.92 |         0     | N/A                      |
|    98 | E    |         0.27472 | False     |                          0.15946 |                 98.86 |         0     | N/A                      |
|    99 | D    |         0.28226 | False     |                          0.55189 |                 98.83 |         0     | N/A                      |
|   100 | L    |         0.06759 | False     |                          0.02697 |                 98.81 |         0     | N/A                      |
|   101 | R    |         0.14841 | False     |                          0.052   |                 98.79 |         0     | N/A                      |
|   102 | C    |         0.27224 | False     |                          0.43848 |                 98.66 |         0     | N/A                      |
|   103 | K    |         0.2399  | False     |                          0.4584  |                 98.73 |         0     | N6-succinyllysine        |
|   104 | Y    |         0.06795 | False     |                          0.01865 |                 98.81 |        34.63  | N/A                      |
|   105 | I    |         0.3341  | True      |                          0.30239 |                 98.52 |        42.957 | N/A                      |
|   106 | S    |         0.31258 | False     |                          0.44039 |                 98.51 |        43.467 | N/A                      |
|   107 | L    |         0.19181 | False     |                          0.05984 |                 98.62 |        43.672 | N/A                      |
|   108 | I    |         0.01525 | False     |                          0.00177 |                 98.66 |        43.672 | N/A                      |
|   109 | Y    |         0.45039 | True      |                          0.50135 |                 98.11 |        39.556 | N/A                      |
|   110 | T    |         0.55504 | True      |                          0.75521 |                 98.08 |        22.239 | N/A                      |
|   111 | N    |         0.53916 | True      |                          0.48344 |                 97.61 |        11.222 | N/A                      |
|   112 | Y    |         0.24075 | False     |                          0.16225 |                 98.15 |         8.744 | N/A                      |
|   113 | E    |         0.53694 | True      |                          0.6915  |                 97.16 |         0     | N/A                      |
|   114 | A    |         0.42561 | True      |                          0.80748 |                 97.86 |         0     | N/A                      |
|   115 | G    |         0.27307 | False     |                          0.12358 |                 98.23 |         0     | N/A                      |
|   116 | K    |         0.3591  | True      |                          0.29665 |                 98.35 |         0     | N6-succinyllysine        |
|   117 | D    |         0.29135 | False     |                          0.52205 |                 98.31 |         0     | N/A                      |
|   118 | D    |         0.271   | False     |                          0.59987 |                 98.49 |         0     | N/A                      |
|   119 | Y    |         0.19473 | False     |                          0.13596 |                 98.69 |         0     | N/A                      |
|   120 | V    |         0.20832 | False     |                          0.3557  |                 98.61 |         0     | N/A                      |
|   121 | K    |         0.32973 | True      |                          0.70137 |                 98.45 |         0     | N/A                      |
|   122 | A    |         0.20734 | False     |                          0.528   |                 98.56 |         0     | N/A                      |
|   123 | L    |         0.0226  | False     |                          0.00989 |                 98.69 |         0     | N/A                      |
|   124 | P    |         0.16709 | False     |                          0.47948 |                 98.67 |         0     | N/A                      |
|   125 | G    |         0.22859 | False     |                          0.58727 |                 98.6  |         0     | N/A                      |
|   126 | Q    |         0.21142 | False     |                          0.33555 |                 98.73 |         0     | N/A                      |
|   127 | L    |         0.00473 | False     |                          0.00082 |                 98.81 |         0     | N/A                      |
|   128 | K    |         0.21183 | False     |                          0.63584 |                 98.8  |         0     | N6-acetyllysine          |
|   129 | P    |         0.30388 | False     |                          0.5058  |                 98.83 |         0     | N/A                      |
|   130 | F    |         0.05491 | False     |                          0.04522 |                 98.83 |         0     | N/A                      |
|   131 | E    |         0.18546 | False     |                          0.12183 |                 98.76 |         0     | N/A                      |
|   132 | T    |         0.25443 | False     |                          0.39012 |                 98.74 |         0     | N/A                      |
|   133 | L    |         0.15317 | False     |                          0.26344 |                 98.59 |         0     | N/A                      |
|   134 | L    |         0.00678 | False     |                          0       |                 98.66 |         0     | N/A                      |
|   135 | S    |         0.25198 | False     |                          0.45677 |                 98.39 |         0     | N/A                      |
|   136 | Q    |         0.26963 | False     |                          0.68586 |                 98.27 |         0     | N/A                      |
|   137 | N    |         0.22868 | False     |                          0.16403 |                 98.43 |         0     | N/A                      |
|   138 | Q    |         0.32247 | True      |                          0.60995 |                 96.9  |         0     | N/A                      |
|   139 | G    |         0.23718 | False     |                          0.45415 |                 96.89 |         0     | N/A                      |
|   140 | G    |         0.06882 | False     |                          0.0311  |                 97.22 |         0     | N/A                      |
|   141 | K    |         0.41217 | True      |                          0.78557 |                 96.8  |         0     | N/A                      |
|   142 | T    |         0.26178 | False     |                          0.24775 |                 97.24 |        12.361 | N/A                      |
|   143 | F    |         0.10631 | False     |                          0.15096 |                 98.62 |        12.361 | N/A                      |
|   144 | I    |         0.04303 | False     |                          0.01597 |                 98.7  |        12.361 | N/A                      |
|   145 | V    |         0.06408 | False     |                          0.06756 |                 98.7  |        12.361 | N/A                      |
|   146 | G    |         0.09861 | False     |                          0.14646 |                 98.04 |        12.361 | N/A                      |
|   147 | D    |         0.26674 | False     |                          0.55337 |                 98.04 |         0     | N/A                      |
|   148 | Q    |         0.1515  | False     |                          0.60108 |                 98.27 |         0     | N/A                      |
|   149 | I    |         0.0781  | False     |                          0.09664 |                 98.74 |         0     | N/A                      |
|   150 | S    |         0.02601 | False     |                          0.0104  |                 98.9  |         0     | N/A                      |
|   151 | F    |         0.00414 | False     |                          0       |                 98.88 |         0     | N/A                      |
|   152 | A    |         0.00112 | False     |                          0       |                 98.88 |         0     | N/A                      |
|   153 | D    |         0.00217 | False     |                          0       |                 98.93 |         0     | N/A                      |
|   154 | Y    |         0.00334 | False     |                          0       |                 98.94 |         0     | N/A                      |
|   155 | N    |         0.02666 | False     |                          0.0175  |                 98.89 |         0     | N/A                      |
|   156 | L    |         0.00161 | False     |                          0       |                 98.93 |         0     | N/A                      |
|   157 | L    |         0.0052  | False     |                          0       |                 98.92 |         0     | N/A                      |
|   158 | D    |         0.02926 | False     |                          0.01435 |                 98.9  |         0     | N/A                      |
|   159 | L    |         0.00286 | False     |                          0       |                 98.92 |         0     | N/A                      |
|   160 | L    |         0.00275 | False     |                          0       |                 98.9  |         0     | N/A                      |
|   161 | L    |         0.25183 | False     |                          0.25358 |                 98.79 |         0     | N/A                      |
|   162 | I    |         0.12488 | False     |                          0.0424  |                 98.77 |         0     | N/A                      |
|   163 | H    |         0.00393 | False     |                          0       |                 98.76 |         0     | N/A                      |
|   164 | E    |         0.19458 | False     |                          0.25541 |                 98.61 |         0     | N/A                      |
|   165 | V    |         0.23283 | False     |                          0.46677 |                 98.55 |         0     | N/A                      |
|   166 | L    |         0.06479 | False     |                          0.02255 |                 98.52 |         0     | N/A                      |
|   167 | A    |         0.12568 | False     |                          0.10935 |                 98.5  |         0     | N/A                      |
|   168 | P    |         0.29776 | False     |                          0.84863 |                 98.57 |         0     | N/A                      |
|   169 | G    |         0.21946 | False     |                          0.38804 |                 98.2  |         0     | N/A                      |
|   170 | C    |         0.22627 | False     |                          0.16214 |                 98.5  |         0     | N/A                      |
|   171 | L    |         0.0694  | False     |                          0.04616 |                 98.67 |         0     | N/A                      |
|   172 | D    |         0.29938 | False     |                          0.77342 |                 98.44 |         0     | N/A                      |
|   173 | A    |         0.21103 | False     |                          0.75259 |                 98.14 |         0     | N/A                      |
|   174 | F    |         0.16475 | False     |                          0.07261 |                 98.68 |         0     | N/A                      |
|   175 | P    |         0.26137 | False     |                          0.67325 |                 98.54 |         0     | N/A                      |
|   176 | L    |         0.15962 | False     |                          0.26874 |                 98.76 |         3.606 | N/A                      |
|   177 | L    |         0.0034  | False     |                          0       |                 98.83 |         4.108 | N/A                      |
|   178 | S    |         0.12479 | False     |                          0.35374 |                 98.66 |         4.108 | N/A                      |
|   179 | A    |         0.18462 | False     |                          0.5293  |                 98.66 |         4.108 | N/A                      |
|   180 | Y    |         0.01788 | False     |                          0       |                 98.79 |         4.108 | N/A                      |
|   181 | V    |         0.13578 | False     |                          0.15043 |                 98.79 |         3.472 | N/A                      |
|   182 | G    |         0.34633 | True      |                          0.50594 |                 98.4  |         0.245 | N/A                      |
|   183 | R    |         0.34892 | True      |                          0.31354 |                 98.53 |         0     | N/A                      |
|   184 | L    |         0.01465 | False     |                          0.00247 |                 98.71 |         0     | N/A                      |
|   185 | S    |         0.16599 | False     |                          0.19543 |                 98.57 |         0     | N/A                      |
|   186 | A    |         0.27697 | False     |                          0.59283 |                 98.66 |         0     | N/A                      |
|   187 | R    |         0.26867 | False     |                          0.28429 |                 98.66 |         0     | N/A                      |
|   188 | P    |         0.23873 | False     |                          0.85141 |                 98.75 |         0     | N/A                      |
|   189 | K    |         0.23813 | False     |                          0.54209 |                 98.73 |         0     | N/A                      |
|   190 | L    |         0.00615 | False     |                          0       |                 98.77 |         0     | N/A                      |
|   191 | K    |         0.22906 | False     |                          0.62967 |                 98.77 |         0     | N/A                      |
|   192 | A    |         0.19932 | False     |                          0.63459 |                 98.75 |         0     | N/A                      |
|   193 | F    |         0.17527 | False     |                          0.08573 |                 98.74 |         0     | N/A                      |
|   194 | L    |         0.20017 | False     |                          0.18162 |                 98.65 |         0     | N/A                      |
|   195 | A    |         0.2654  | False     |                          0.73507 |                 98.61 |         0     | N/A                      |
|   196 | S    |         0.21315 | False     |                          0.16119 |                 98.51 |         0     | N/A                      |
|   197 | P    |         0.28276 | False     |                          0.65906 |                 97.87 |         0     | N/A                      |
|   198 | E    |         0.2561  | False     |                          0.56481 |                 96.9  |         0     | N/A                      |
|   199 | Y    |         0.14013 | False     |                          0.08153 |                 98.39 |         0     | Phosphotyrosine; by EGFR |
|   200 | V    |         0.35551 | True      |                          0.59286 |                 97.74 |         0     | N/A                      |
|   201 | N    |         0.41038 | True      |                          0.72476 |                 97.88 |         0     | N/A                      |
|   202 | L    |         0.22129 | False     |                          0.26023 |                 97.95 |         0     | N/A                      |
|   203 | P    |         0.27477 | False     |                          0.47603 |                 98.37 |         0     | N/A                      |
|   204 | I    |         0.14379 | False     |                          0.06869 |                 98.62 |         0     | N/A                      |
|   205 | N    |         0.14578 | False     |                          0.04597 |                 98.57 |         0     | N/A                      |
|   206 | G    |         0.64152 | True      |                          0.65968 |                 97.54 |         0     | N/A                      |
|   207 | N    |         0.58079 | True      |                          0.37474 |                 96.98 |         0     | N/A                      |
|   208 | G    |         0.21337 | False     |                          0.80629 |                 95.88 |         0     | N/A                      |
|   209 | K    |         0.40256 | True      |                          0.31654 |                 97.76 |         0     | N/A                      |
|   210 | Q    |         0.13076 | False     |                          0.45234 |                 96.39 |         0     | N/A                      |


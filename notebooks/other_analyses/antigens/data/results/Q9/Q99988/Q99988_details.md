# Detailed Data for Q99988


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: Q99988
- **Gene Name**: GDF-15
- **Protein Name**: Growth/differentiation factor 15
- **Swiss Prot**: GDF15_HUMAN
- **Family**: growth factor
- **Biomarker Application**: diagnosis
- **Number of Isoforms**: 0
- **Regulation**: 1
- **(transcriptomics) AUC**: nan
- **(transcriptomics) Fold Change**: nan
- **(transcriptomics) Regulation**: Downregulated
- **Discotope Epitope Count**: 54
- **Max n_uniprots (Homo)**: 2
- **Max n_uniprots (Hetero)**: 6


## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| GDF15             | GFRAL             |   0.999 |
| GDF15             | TGFBR2            |   0.96  |
| GDF15             | RET               |   0.958 |

## Homologs

| uniprot_id   | gene_id   |
|:-------------|:----------|
| Q9UK05       | GDF2      |
| P22004       | BMP6      |
| Q96S42       | NODAL     |
| Q7Z4P5       | GDF7      |
| C8C060       | BMP2      |
| P55103       | INHBC     |
| B4DXG3       | GDF9      |
| P34820       | BMP8B     |
| Q7Z5Y6       | BMP8A     |
| Q53S46       | GDF8      |
| A4D1W7       | INHBA     |
| P55107       | GDF10     |
| A0A499FJK2   | TGFB1     |
| P05111       | INHA      |
| A0A0S2A5D6   | GDF6      |
| P12645       | BMP3      |
| P27539       | GDF1      |
| P61812       | TGFB2     |
| O95390       | GDF11     |
| P09529       | INHBB     |
| O95972       | BMP15     |
| V9GYF1       | BMP4      |
| F1T0J1       | GDF5      |
| Q9NR23       | GDF3      |
| P10600       | TGFB3     |
| O95393       | BMP10     |
| P18075       | BMP7      |
| M9VUD0       | BMP5      |
| O00292       | LEFTY2    |
| O75610       | LEFTY1    |
| P58166       | INHBE     |

## Biological Assemblies

|   Unnamed: 0 |   assembly |   n_uniprots | composition   | crystal_id   |
|-------------:|-----------:|-------------:|:--------------|:-------------|
|            0 |          1 |            6 | Hetero        | 6q2j         |
|            0 |          1 |            1 | Homo          | 5vz3         |
|            0 |          1 |            2 | Hetero        | 5vz4         |
|            0 |          1 |            2 | Homo          | 5vt2         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification   | glycosylation                   |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:---------------|:--------------------------------|
|     1 | M    |         0.10664 | False     |                          1.21541 |                 42.86 |         0     | N/A            | N/A                             |
|     2 | P    |         0.16434 | False     |                          0.98773 |                 45.61 |         0     | N/A            | N/A                             |
|     3 | G    |         0.19333 | False     |                          0.64202 |                 35.03 |         0     | N/A            | N/A                             |
|     4 | Q    |         0.15395 | False     |                          0.92104 |                 39.47 |         0     | N/A            | N/A                             |
|     5 | E    |         0.24047 | True      |                          0.8395  |                 35.08 |         0     | N/A            | N/A                             |
|     6 | L    |         0.14548 | False     |                          1.02967 |                 34.66 |         0     | N/A            | N/A                             |
|     7 | R    |         0.15598 | False     |                          0.91719 |                 35.07 |         0     | N/A            | N/A                             |
|     8 | T    |         0.14596 | False     |                          0.86739 |                 38.16 |         0.002 | N/A            | N/A                             |
|     9 | V    |         0.10428 | False     |                          0.72625 |                 43.88 |         0.005 | N/A            | N/A                             |
|    10 | N    |         0.18157 | False     |                          0.71128 |                 45.44 |         0.006 | N/A            | N/A                             |
|    11 | G    |         0.16334 | False     |                          0.66652 |                 50.73 |         0.027 | N/A            | N/A                             |
|    12 | S    |         0.0904  | False     |                          0.60486 |                 55.92 |         0.257 | N/A            | N/A                             |
|    13 | Q    |         0.10166 | False     |                          0.57856 |                 57.48 |         2.117 | N/A            | N/A                             |
|    14 | M    |         0.12544 | False     |                          0.56273 |                 59.77 |        49.575 | N/A            | N/A                             |
|    15 | L    |         0.10794 | False     |                          0.69729 |                 62.5  |        91.104 | N/A            | N/A                             |
|    16 | L    |         0.11774 | False     |                          0.68946 |                 64.89 |        98.645 | N/A            | N/A                             |
|    17 | V    |         0.07905 | False     |                          0.53767 |                 67.39 |        99.89  | N/A            | N/A                             |
|    18 | L    |         0.10702 | False     |                          0.65702 |                 64.92 |        99.932 | N/A            | N/A                             |
|    19 | L    |         0.11065 | False     |                          0.58289 |                 60.69 |        99.864 | N/A            | N/A                             |
|    20 | V    |         0.11019 | False     |                          0.69119 |                 65.95 |        99.108 | N/A            | N/A                             |
|    21 | L    |         0.13415 | False     |                          0.68456 |                 54.9  |        89.475 | N/A            | N/A                             |
|    22 | S    |         0.09457 | False     |                          0.5211  |                 48.44 |        36.125 | N/A            | N/A                             |
|    23 | W    |         0.17463 | False     |                          0.94874 |                 43.4  |        29.498 | N/A            | N/A                             |
|    24 | L    |         0.14602 | False     |                          0.71497 |                 40.63 |         2.101 | N/A            | N/A                             |
|    25 | P    |         0.15544 | False     |                          0.90574 |                 38.75 |         1.072 | N/A            | N/A                             |
|    26 | H    |         0.11683 | False     |                          0.99667 |                 34.25 |         0     | N/A            | N/A                             |
|    27 | G    |         0.22366 | True      |                          0.84808 |                 31.08 |         0     | N/A            | N/A                             |
|    28 | G    |         0.2123  | False     |                          0.99183 |                 30.47 |         0     | N/A            | N/A                             |
|    29 | A    |         0.12076 | False     |                          0.95282 |                 35.69 |         0     | N/A            | N/A                             |
|    30 | L    |         0.14194 | False     |                          1.02764 |                 35.32 |         0     | N/A            | N/A                             |
|    31 | S    |         0.12445 | False     |                          0.67352 |                 44.16 |         0     | N/A            | N/A                             |
|    32 | L    |         0.14558 | False     |                          0.96221 |                 34.73 |         0     | N/A            | N/A                             |
|    33 | A    |         0.11113 | False     |                          0.67262 |                 33.44 |         0     | N/A            | N/A                             |
|    34 | E    |         0.13618 | False     |                          0.54723 |                 34.21 |         0     | N/A            | N/A                             |
|    35 | A    |         0.13508 | False     |                          0.87995 |                 34.65 |         0     | N/A            | N/A                             |
|    36 | S    |         0.10768 | False     |                          0.72151 |                 32.59 |         0     | N/A            | N/A                             |
|    37 | R    |         0.20294 | False     |                          0.64249 |                 29.53 |         0     | N/A            | N/A                             |
|    38 | A    |         0.15803 | False     |                          0.80817 |                 35.5  |         0     | N/A            | N/A                             |
|    39 | S    |         0.19481 | False     |                          0.78356 |                 33.85 |         0     | N/A            | N/A                             |
|    40 | F    |         0.14578 | False     |                          0.80233 |                 34.72 |         0     | N/A            | N/A                             |
|    41 | P    |         0.18076 | False     |                          0.70701 |                 37.94 |         0     | N/A            | N/A                             |
|    42 | G    |         0.17627 | False     |                          0.41555 |                 32.54 |         0     | N/A            | N/A                             |
|    43 | P    |         0.15641 | False     |                          0.85999 |                 46.56 |         0     | N/A            | N/A                             |
|    44 | S    |         0.12    | False     |                          0.72968 |                 47.08 |         0     | N/A            | N/A                             |
|    45 | E    |         0.08513 | False     |                          0.53787 |                 42.74 |         0     | N/A            | N/A                             |
|    46 | L    |         0.11617 | False     |                          0.8217  |                 41.94 |         0     | N/A            | N/A                             |
|    47 | H    |         0.1139  | False     |                          0.72231 |                 44.66 |         0     | N/A            | N/A                             |
|    48 | S    |         0.07367 | False     |                          0.51587 |                 57.56 |         0     | N/A            | N/A                             |
|    49 | E    |         0.0768  | False     |                          0.52291 |                 69.45 |         0     | N/A            | N/A                             |
|    50 | D    |         0.06727 | False     |                          0.46344 |                 83.81 |         0     | N/A            | N/A                             |
|    51 | S    |         0.04018 | False     |                          0.42909 |                 87.48 |         0     | N/A            | N/A                             |
|    52 | R    |         0.07044 | False     |                          0.66503 |                 87.36 |         0     | N/A            | N/A                             |
|    53 | F    |         0.07099 | False     |                          0.70094 |                 88.33 |         0     | N/A            | N/A                             |
|    54 | R    |         0.05987 | False     |                          0.57033 |                 90.42 |         0     | N/A            | N/A                             |
|    55 | E    |         0.07336 | False     |                          0.40846 |                 90.49 |         0     | N/A            | N/A                             |
|    56 | L    |         0.07194 | False     |                          0.70683 |                 90.69 |         0     | N/A            | N/A                             |
|    57 | R    |         0.07558 | False     |                          0.57614 |                 90.87 |         0     | N/A            | N/A                             |
|    58 | K    |         0.05971 | False     |                          0.72801 |                 92.28 |         0     | N/A            | N/A                             |
|    59 | R    |         0.06452 | False     |                          0.64716 |                 90.8  |         0     | N/A            | N/A                             |
|    60 | Y    |         0.06219 | False     |                          0.55515 |                 90.41 |         0     | N/A            | N/A                             |
|    61 | E    |         0.0501  | False     |                          0.43851 |                 93.35 |         0     | N/A            | N/A                             |
|    62 | D    |         0.053   | False     |                          0.4868  |                 91.58 |         0     | N/A            | N/A                             |
|    63 | L    |         0.06872 | False     |                          0.55644 |                 89.13 |         0     | N/A            | N/A                             |
|    64 | L    |         0.05118 | False     |                          0.27265 |                 86.4  |         0     | N/A            | N/A                             |
|    65 | T    |         0.04781 | False     |                          0.57722 |                 86.42 |         0     | N/A            | N/A                             |
|    66 | R    |         0.07214 | False     |                          0.60878 |                 82.83 |         0     | N/A            | N/A                             |
|    67 | L    |         0.05512 | False     |                          0.53167 |                 78.38 |         0     | N/A            | N/A                             |
|    68 | R    |         0.0618  | False     |                          0.56238 |                 78.26 |         0     | N/A            | N/A                             |
|    69 | A    |         0.05505 | False     |                          0.54184 |                 76.64 |         0     | N/A            | N/A                             |
|    70 | N    |         0.09165 | False     |                          0.57663 |                 70.74 |         0     | N/A            | N-linked (GlcNAc...) asparagine |
|    71 | Q    |         0.09064 | False     |                          0.55838 |                 63.02 |         0     | N/A            | N/A                             |
|    72 | S    |         0.0923  | False     |                          0.52165 |                 59.88 |         0     | N/A            | N/A                             |
|    73 | W    |         0.08375 | False     |                          0.79043 |                 46.28 |         0     | N/A            | N/A                             |
|    74 | E    |         0.06195 | False     |                          0.44787 |                 48.29 |         0     | N/A            | N/A                             |
|    75 | D    |         0.16434 | False     |                          0.7098  |                 46.57 |         0     | N/A            | N/A                             |
|    76 | S    |         0.11113 | False     |                          0.71277 |                 50.12 |         0     | N/A            | N/A                             |
|    77 | N    |         0.10284 | False     |                          0.61765 |                 40.86 |         0     | N/A            | N/A                             |
|    78 | T    |         0.21998 | False     |                          0.84452 |                 36.81 |         0     | N/A            | N/A                             |
|    79 | D    |         0.21067 | False     |                          0.8334  |                 41.71 |         0     | N/A            | N/A                             |
|    80 | L    |         0.19746 | False     |                          1.11008 |                 37.98 |         0     | N/A            | N/A                             |
|    81 | V    |         0.12092 | False     |                          0.73806 |                 41.74 |         0     | N/A            | N/A                             |
|    82 | P    |         0.15858 | False     |                          0.70663 |                 48.42 |         0     | N/A            | N/A                             |
|    83 | A    |         0.11347 | False     |                          0.62127 |                 48.78 |         0     | N/A            | N/A                             |
|    84 | P    |         0.10898 | False     |                          0.41185 |                 52.85 |         0     | N/A            | N/A                             |
|    85 | A    |         0.12329 | False     |                          0.55299 |                 69.28 |         0     | N/A            | N/A                             |
|    86 | V    |         0.12415 | False     |                          0.52939 |                 77.08 |         0     | N/A            | N/A                             |
|    87 | R    |         0.19564 | False     |                          0.43582 |                 78.44 |         0     | N/A            | N/A                             |
|    88 | I    |         0.1406  | False     |                          0.57783 |                 83.95 |         0     | N/A            | N/A                             |
|    89 | L    |         0.08298 | False     |                          0.09563 |                 84.68 |         0     | N/A            | N/A                             |
|    90 | T    |         0.18197 | False     |                          0.73831 |                 85.91 |         0     | N/A            | N/A                             |
|    91 | P    |         0.0272  | False     |                          0.03944 |                 87.48 |         0     | N/A            | N/A                             |
|    92 | E    |         0.08582 | False     |                          0.48554 |                 87.16 |         0     | N/A            | N/A                             |
|    93 | V    |         0.08188 | False     |                          0.32515 |                 86.09 |         0     | N/A            | N/A                             |
|    94 | R    |         0.28753 | True      |                          0.72454 |                 83.78 |         0     | N/A            | N/A                             |
|    95 | L    |         0.18236 | False     |                          0.46042 |                 81.24 |         0     | N/A            | N/A                             |
|    96 | G    |         0.16765 | False     |                          0.27555 |                 76.3  |         0     | N/A            | N/A                             |
|    97 | S    |         0.20257 | False     |                          1.05167 |                 75.37 |         0     | N/A            | N/A                             |
|    98 | G    |         0.20077 | False     |                          0.67164 |                 71.66 |         0     | N/A            | N/A                             |
|    99 | G    |         0.13015 | False     |                          0.42457 |                 74.21 |         0     | N/A            | N/A                             |
|   100 | H    |         0.11234 | False     |                          0.26662 |                 81.71 |         0     | N/A            | N/A                             |
|   101 | L    |         0.01152 | False     |                          0.00412 |                 84.45 |         0     | N/A            | N/A                             |
|   102 | H    |         0.09922 | False     |                          0.44241 |                 86.85 |         0     | N/A            | N/A                             |
|   103 | L    |         0.00934 | False     |                          0.00574 |                 89.27 |         0     | N/A            | N/A                             |
|   104 | R    |         0.12856 | False     |                          0.41165 |                 87.91 |         0     | N/A            | N/A                             |
|   105 | I    |         0.01888 | False     |                          0.012   |                 86.87 |         0     | N/A            | N/A                             |
|   106 | S    |         0.0651  | False     |                          0.38516 |                 83    |         0     | N/A            | N/A                             |
|   107 | R    |         0.17987 | False     |                          0.38084 |                 74.6  |         0     | N/A            | N/A                             |
|   108 | A    |         0.16412 | False     |                          1.01459 |                 70.82 |         0     | N/A            | N/A                             |
|   109 | A    |         0.08089 | False     |                          0.4285  |                 70.6  |         0     | N/A            | N/A                             |
|   110 | L    |         0.04684 | False     |                          0.14315 |                 64.85 |         0     | N/A            | N/A                             |
|   111 | P    |         0.08513 | False     |                          0.23128 |                 53.05 |         0     | N/A            | N/A                             |
|   112 | E    |         0.14785 | False     |                          0.96163 |                 44.3  |         0     | N/A            | N/A                             |
|   113 | G    |         0.22269 | False     |                          0.80085 |                 40.04 |         0     | N/A            | N/A                             |
|   114 | L    |         0.07392 | False     |                          0.38207 |                 47.54 |         0     | N/A            | N/A                             |
|   115 | P    |         0.15958 | False     |                          0.62968 |                 46.36 |         0     | N/A            | N/A                             |
|   116 | E    |         0.17017 | False     |                          0.81808 |                 50.13 |         0     | N/A            | N/A                             |
|   117 | A    |         0.07707 | False     |                          0.38464 |                 52.33 |         0     | N/A            | N/A                             |
|   118 | S    |         0.09384 | False     |                          0.19002 |                 65.23 |         0     | N/A            | N/A                             |
|   119 | R    |         0.10103 | False     |                          0.45915 |                 71.81 |         0     | N/A            | N/A                             |
|   120 | L    |         0.06511 | False     |                          0.12645 |                 79.5  |         0     | N/A            | N/A                             |
|   121 | H    |         0.16468 | False     |                          0.28695 |                 80.71 |         0     | N/A            | N/A                             |
|   122 | R    |         0.18227 | False     |                          0.44122 |                 87.14 |         0     | N/A            | N/A                             |
|   123 | A    |         0.00381 | False     |                          0       |                 89.08 |         0     | N/A            | N/A                             |
|   124 | L    |         0.08858 | False     |                          0.21577 |                 89.92 |         0     | N/A            | N/A                             |
|   125 | F    |         0.00964 | False     |                          0.00165 |                 88.71 |         0     | N/A            | N/A                             |
|   126 | R    |         0.23001 | True      |                          0.2389  |                 84.96 |         0     | N/A            | N/A                             |
|   127 | L    |         0.08239 | False     |                          0.10931 |                 80.82 |         0     | N/A            | N/A                             |
|   128 | S    |         0.18811 | False     |                          0.11844 |                 74.97 |         0     | N/A            | N/A                             |
|   129 | P    |         0.15602 | False     |                          0.45918 |                 69.39 |         0     | N/A            | N/A                             |
|   130 | T    |         0.29059 | True      |                          0.91461 |                 68.66 |         0     | N/A            | N/A                             |
|   131 | A    |         0.25601 | True      |                          0.22148 |                 67.14 |         0     | N/A            | N/A                             |
|   132 | S    |         0.25308 | True      |                          0.89954 |                 61.31 |         0     | N/A            | N/A                             |
|   133 | R    |         0.34764 | True      |                          0.69875 |                 70.66 |         0     | N/A            | N/A                             |
|   134 | S    |         0.26479 | True      |                          0.42408 |                 80.5  |         0     | N/A            | N/A                             |
|   135 | W    |         0.16964 | False     |                          0.11547 |                 84.09 |         0     | N/A            | N/A                             |
|   136 | D    |         0.10027 | False     |                          0.58781 |                 86.13 |         0     | N/A            | N/A                             |
|   137 | V    |         0.01171 | False     |                          0.02571 |                 87.66 |         0     | N/A            | N/A                             |
|   138 | T    |         0.11163 | False     |                          0.08835 |                 85.03 |         0     | N/A            | N/A                             |
|   139 | R    |         0.2048  | False     |                          0.83378 |                 84.87 |         0     | N/A            | N/A                             |
|   140 | P    |         0.19964 | False     |                          0.3379  |                 86.13 |         0     | N/A            | N/A                             |
|   141 | L    |         0.00614 | False     |                          0.00412 |                 87.45 |         0     | N/A            | N/A                             |
|   142 | R    |         0.16536 | False     |                          0.43777 |                 84.03 |         0     | N/A            | N/A                             |
|   143 | R    |         0.25728 | True      |                          0.69334 |                 82.34 |         0     | N/A            | N/A                             |
|   144 | Q    |         0.13625 | False     |                          0.31508 |                 82.9  |         0     | N/A            | N/A                             |
|   145 | L    |         0.12174 | False     |                          0.47084 |                 80.32 |         0     | N/A            | N/A                             |
|   146 | S    |         0.18425 | False     |                          0.71699 |                 74.02 |         0     | N/A            | N/A                             |
|   147 | L    |         0.18158 | False     |                          0.75338 |                 78.47 |         0     | N/A            | N/A                             |
|   148 | A    |         0.10561 | False     |                          0.31173 |                 73.24 |         0     | N/A            | N/A                             |
|   149 | R    |         0.23636 | True      |                          0.77231 |                 69.86 |         0     | N/A            | N/A                             |
|   150 | P    |         0.24564 | True      |                          0.79704 |                 65.51 |         0     | N/A            | N/A                             |
|   151 | Q    |         0.33356 | True      |                          0.87552 |                 71.49 |         0     | N/A            | N/A                             |
|   152 | A    |         0.15506 | False     |                          0.29606 |                 77.3  |         0     | N/A            | N/A                             |
|   153 | P    |         0.19111 | False     |                          0.80832 |                 82.12 |         0     | N/A            | N/A                             |
|   154 | A    |         0.08011 | False     |                          0.09339 |                 83.96 |         0     | N/A            | N/A                             |
|   155 | L    |         0.04642 | False     |                          0.05264 |                 85.62 |         0     | N/A            | N/A                             |
|   156 | H    |         0.15609 | False     |                          0.58284 |                 88.17 |         0     | N/A            | N/A                             |
|   157 | L    |         0.03588 | False     |                          0.0173  |                 87.96 |         0     | N/A            | N/A                             |
|   158 | R    |         0.12208 | False     |                          0.59148 |                 85.72 |         0     | N/A            | N/A                             |
|   159 | L    |         0.05891 | False     |                          0.06183 |                 83.26 |         0     | N/A            | N/A                             |
|   160 | S    |         0.12964 | False     |                          0.64711 |                 78.68 |         0     | N/A            | N/A                             |
|   161 | P    |         0.18722 | False     |                          0.18248 |                 67.6  |         0     | N/A            | N/A                             |
|   162 | P    |         0.30809 | True      |                          0.38743 |                 62.19 |         0     | N/A            | N/A                             |
|   163 | P    |         0.39186 | True      |                          0.97915 |                 57.19 |         0     | N/A            | N/A                             |
|   164 | S    |         0.29634 | True      |                          0.7932  |                 54.05 |         0     | N/A            | N/A                             |
|   165 | Q    |         0.18437 | False     |                          0.17702 |                 55.47 |         0     | N/A            | N/A                             |
|   166 | S    |         0.1484  | False     |                          0.493   |                 56.74 |         0     | N/A            | N/A                             |
|   167 | D    |         0.25575 | True      |                          0.78191 |                 57.69 |         0     | N/A            | N/A                             |
|   168 | Q    |         0.18901 | False     |                          0.53299 |                 56.59 |         0     | N/A            | N/A                             |
|   169 | L    |         0.04291 | False     |                          0.0315  |                 55.49 |         0     | N/A            | N/A                             |
|   170 | L    |         0.18922 | False     |                          0.80984 |                 55.8  |         0     | N/A            | N/A                             |
|   171 | A    |         0.15073 | False     |                          0.7895  |                 54.88 |         0     | N/A            | N/A                             |
|   172 | E    |         0.10121 | False     |                          0.22698 |                 55.78 |         0     | N/A            | N/A                             |
|   173 | S    |         0.18832 | False     |                          0.49909 |                 55.15 |         0     | N/A            | N/A                             |
|   174 | S    |         0.2443  | True      |                          0.86823 |                 56.21 |         0     | N/A            | N/A                             |
|   175 | S    |         0.18416 | False     |                          0.83931 |                 55.4  |         0     | N/A            | N/A                             |
|   176 | A    |         0.13516 | False     |                          0.28002 |                 66.23 |         0     | N/A            | N/A                             |
|   177 | R    |         0.21602 | False     |                          0.74016 |                 77.54 |         0     | N/A            | N/A                             |
|   178 | P    |         0.03491 | False     |                          0.12426 |                 85.87 |         0     | N/A            | N/A                             |
|   179 | Q    |         0.0852  | False     |                          0.16481 |                 87.61 |         0     | N/A            | N/A                             |
|   180 | L    |         0.00481 | False     |                          0.00082 |                 88.58 |         0     | N/A            | N/A                             |
|   181 | E    |         0.0638  | False     |                          0.13272 |                 88.67 |         0     | N/A            | N/A                             |
|   182 | L    |         0.02569 | False     |                          0.0676  |                 86.76 |         0     | N/A            | N/A                             |
|   183 | H    |         0.07934 | False     |                          0.17389 |                 84.15 |         0     | N/A            | N/A                             |
|   184 | L    |         0.04892 | False     |                          0.05788 |                 79.52 |         0     | N/A            | N/A                             |
|   185 | R    |         0.20209 | False     |                          0.36315 |                 70.76 |         0     | N/A            | N/A                             |
|   186 | P    |         0.07334 | False     |                          0.4735  |                 62.28 |         0     | N/A            | N/A                             |
|   187 | Q    |         0.11591 | False     |                          0.3934  |                 58.57 |         0     | N/A            | N/A                             |
|   188 | A    |         0.13511 | False     |                          0.80464 |                 51.85 |         0     | N/A            | N/A                             |
|   189 | A    |         0.15194 | False     |                          0.75163 |                 47.26 |         0     | N/A            | N/A                             |
|   190 | R    |         0.18046 | False     |                          0.87852 |                 45.44 |         0     | N/A            | N/A                             |
|   191 | G    |         0.13285 | False     |                          0.53314 |                 45.46 |         0     | N/A            | N/A                             |
|   192 | R    |         0.16867 | False     |                          0.82114 |                 45.53 |         0     | N/A            | N/A                             |
|   193 | R    |         0.17707 | False     |                          0.55548 |                 46.71 |         0     | N/A            | N/A                             |
|   194 | R    |         0.22552 | True      |                          0.83377 |                 45.69 |         0     | N/A            | N/A                             |
|   195 | A    |         0.15223 | False     |                          0.88706 |                 45.57 |         0     | N/A            | N/A                             |
|   196 | R    |         0.21951 | False     |                          0.90148 |                 45.27 |         0     | N/A            | N/A                             |
|   197 | A    |         0.07425 | False     |                          0.70439 |                 46.55 |         0     | N/A            | N/A                             |
|   198 | R    |         0.15417 | False     |                          0.94165 |                 49.4  |         0     | N/A            | N/A                             |
|   199 | N    |         0.18923 | False     |                          0.87569 |                 47.61 |         0     | N/A            | N/A                             |
|   200 | G    |         0.16584 | False     |                          0.80879 |                 54.71 |         0     | N/A            | N/A                             |
|   201 | D    |         0.12098 | False     |                          0.46656 |                 61.92 |         0     | N/A            | N/A                             |
|   202 | H    |         0.16044 | False     |                          0.87035 |                 78.22 |         0     | N/A            | N/A                             |
|   203 | C    |         0.07868 | False     |                          0.07091 |                 86.33 |         0     | N/A            | N/A                             |
|   204 | P    |         0.28749 | True      |                          0.55942 |                 86.49 |         0     | N/A            | N/A                             |
|   205 | L    |         0.27807 | True      |                          0.35401 |                 87.86 |         0     | N/A            | N/A                             |
|   206 | G    |         0.18268 | False     |                          0.28675 |                 85.64 |         0     | N/A            | N/A                             |
|   207 | P    |         0.24127 | True      |                          0.95742 |                 84.04 |         0     | N/A            | N/A                             |
|   208 | G    |         0.13259 | False     |                          0.53673 |                 84.78 |         0     | N/A            | N/A                             |
|   209 | R    |         0.19512 | False     |                          0.60938 |                 90.74 |         0     | N/A            | N/A                             |
|   210 | C    |         0.0205  | False     |                          0.00448 |                 94.61 |         0     | N/A            | N/A                             |
|   211 | C    |         0.00533 | False     |                          0.00592 |                 95.28 |         0     | N/A            | N/A                             |
|   212 | R    |         0.10371 | False     |                          0.29086 |                 93.85 |         0     | N/A            | N/A                             |
|   213 | L    |         0.06921 | False     |                          0.42926 |                 95.49 |         0     | N/A            | N/A                             |
|   214 | H    |         0.13435 | False     |                          0.31817 |                 96.08 |         0     | N/A            | N/A                             |
|   215 | T    |         0.09442 | False     |                          0.57696 |                 97.1  |         0     | N/A            | N/A                             |
|   216 | V    |         0.13154 | False     |                          0.4151  |                 96.68 |         0     | N/A            | N/A                             |
|   217 | R    |         0.19126 | False     |                          0.70004 |                 97.59 |         0     | N/A            | N/A                             |
|   218 | A    |         0.15262 | False     |                          0.10313 |                 97.22 |         0     | N/A            | N/A                             |
|   219 | S    |         0.39176 | True      |                          0.24905 |                 97.46 |         0     | N/A            | N/A                             |
|   220 | L    |         0.02293 | False     |                          0.00742 |                 95.44 |         0     | N/A            | N/A                             |
|   221 | E    |         0.30952 | True      |                          0.6313  |                 96.88 |         0     | N/A            | N/A                             |
|   222 | D    |         0.38428 | True      |                          0.67688 |                 96.57 |         0     | N/A            | N/A                             |
|   223 | L    |         0.28191 | True      |                          0.33585 |                 96.15 |         0     | N/A            | N/A                             |
|   224 | G    |         0.45104 | True      |                          0.67649 |                 96.17 |         0     | N/A            | N/A                             |
|   225 | W    |         0.21084 | False     |                          0.19909 |                 96.65 |         0     | N/A            | N/A                             |
|   226 | A    |         0.26418 | True      |                          0.43065 |                 94.79 |         0     | N/A            | N/A                             |
|   227 | D    |         0.41394 | True      |                          0.81155 |                 94.71 |         0     | N/A            | N/A                             |
|   228 | W    |         0.33149 | True      |                          0.388   |                 95.26 |         0     | N/A            | N/A                             |
|   229 | V    |         0.00922 | False     |                          0.0007  |                 96.89 |         0     | N/A            | N/A                             |
|   230 | L    |         0.31516 | True      |                          0.3506  |                 96.68 |         0     | N/A            | N/A                             |
|   231 | S    |         0.30446 | True      |                          0.31675 |                 97.11 |         0     | N/A            | N/A                             |
|   232 | P    |         0.26871 | True      |                          0.35389 |                 96.09 |         0     | N/A            | N/A                             |
|   233 | R    |         0.31219 | True      |                          0.59822 |                 95.66 |         0     | N/A            | N/A                             |
|   234 | E    |         0.19081 | False     |                          0.49486 |                 96.68 |         0     | N/A            | N/A                             |
|   235 | V    |         0.03506 | False     |                          0.03793 |                 95.77 |         1.85  | N/A            | N/A                             |
|   236 | Q    |         0.13003 | False     |                          0.60841 |                 96.09 |         1.85  | N/A            | N/A                             |
|   237 | V    |         0.10803 | False     |                          0.12567 |                 96.85 |         2.879 | N/A            | N/A                             |
|   238 | T    |         0.08072 | False     |                          0.16268 |                 97.68 |         2.879 | N/A            | N/A                             |
|   239 | M    |         0.18636 | False     |                          0.37053 |                 96.79 |         2.879 | N/A            | N/A                             |
|   240 | C    |         0.05103 | False     |                          0.14695 |                 96.81 |         2.319 | N/A            | N/A                             |
|   241 | I    |         0.23873 | True      |                          0.46318 |                 95.55 |         2.319 | N/A            | N/A                             |
|   242 | G    |         0.05254 | False     |                          0.36534 |                 95.31 |         0     | N/A            | N/A                             |
|   243 | A    |         0.11021 | False     |                          0.45209 |                 94.77 |         0     | N/A            | N/A                             |
|   244 | C    |         0.06589 | False     |                          0.06224 |                 95.03 |         0     | N/A            | N/A                             |
|   245 | P    |         0.17475 | False     |                          0.17879 |                 89.9  |         0     | N/A            | N/A                             |
|   246 | S    |         0.19426 | False     |                          0.55164 |                 85.57 |         0     | N/A            | N/A                             |
|   247 | Q    |         0.16426 | False     |                          0.63625 |                 85.07 |         0     | N/A            | N/A                             |
|   248 | F    |         0.10548 | False     |                          0.11309 |                 88.06 |         0     | N/A            | N/A                             |
|   249 | R    |         0.11466 | False     |                          0.37536 |                 89.25 |         0     | N/A            | N/A                             |
|   250 | A    |         0.09561 | False     |                          0.23497 |                 90.67 |         0     | N/A            | N/A                             |
|   251 | A    |         0.07495 | False     |                          0.11851 |                 88.74 |         0     | N/A            | N/A                             |
|   252 | N    |         0.10002 | False     |                          0.43219 |                 86.27 |         0     | N/A            | N/A                             |
|   253 | M    |         0.12022 | False     |                          0.67932 |                 91.05 |         0     | N/A            | N/A                             |
|   254 | H    |         0.11117 | False     |                          0.64515 |                 92.51 |         0     | N/A            | N/A                             |
|   255 | A    |         0.00551 | False     |                          0.00477 |                 93.05 |         0     | N/A            | N/A                             |
|   256 | Q    |         0.2755  | True      |                          0.32207 |                 91.51 |         0     | N/A            | N/A                             |
|   257 | I    |         0.0741  | False     |                          0.52055 |                 94.15 |         0     | N/A            | N/A                             |
|   258 | K    |         0.06018 | False     |                          0.17014 |                 95.17 |         0     | N/A            | N/A                             |
|   259 | T    |         0.07372 | False     |                          0.09036 |                 93.62 |         0     | N/A            | N/A                             |
|   260 | S    |         0.17183 | False     |                          0.388   |                 94.33 |         0     | N/A            | N/A                             |
|   261 | L    |         0.15555 | False     |                          0.45092 |                 95.44 |         0     | N/A            | N/A                             |
|   262 | H    |         0.15488 | False     |                          0.29415 |                 95.42 |         0     | N/A            | N/A                             |
|   263 | R    |         0.29724 | True      |                          0.71042 |                 93.53 |         0     | N/A            | N/A                             |
|   264 | L    |         0.21231 | False     |                          0.66544 |                 95.27 |         0     | N/A            | N/A                             |
|   265 | K    |         0.2399  | True      |                          0.60554 |                 95.82 |         0     | N/A            | N/A                             |
|   266 | P    |         0.29417 | True      |                          0.56968 |                 94.83 |         0     | N/A            | N/A                             |
|   267 | D    |         0.30805 | True      |                          0.91511 |                 96.21 |         0     | N/A            | N/A                             |
|   268 | T    |         0.29373 | True      |                          0.75471 |                 96.51 |         0     | N/A            | N/A                             |
|   269 | V    |         0.16689 | False     |                          0.20089 |                 95.94 |         0     | N/A            | N/A                             |
|   270 | P    |         0.2368  | True      |                          0.66064 |                 95.37 |         0     | N/A            | N/A                             |
|   271 | A    |         0.10127 | False     |                          0.41666 |                 94.49 |         0     | N/A            | N/A                             |
|   272 | P    |         0.03928 | False     |                          0.06012 |                 95.77 |         0     | N/A            | N/A                             |
|   273 | C    |         0.08478 | False     |                          0.51121 |                 96.39 |         0     | N/A            | N/A                             |
|   274 | C    |         0.0384  | False     |                          0.17385 |                 96.95 |         0     | N/A            | N/A                             |
|   275 | V    |         0.08569 | False     |                          0.31133 |                 97.19 |         0     | N/A            | N/A                             |
|   276 | P    |         0.04776 | False     |                          0.32736 |                 96.77 |         0     | N/A            | N/A                             |
|   277 | A    |         0.05762 | False     |                          0.45436 |                 93.35 |         0     | N/A            | N/A                             |
|   278 | S    |         0.08791 | False     |                          0.33359 |                 92.92 |         0     | N/A            | N/A                             |
|   279 | Y    |         0.13475 | False     |                          0.4331  |                 95.19 |         0     | N/A            | N/A                             |
|   280 | N    |         0.14215 | False     |                          0.31758 |                 94.46 |         0     | N/A            | N/A                             |
|   281 | P    |         0.17152 | False     |                          0.6573  |                 95.48 |         0.227 | N/A            | N/A                             |
|   282 | M    |         0.09791 | False     |                          0.10624 |                 96.01 |         0.936 | N/A            | N/A                             |
|   283 | V    |         0.17992 | False     |                          0.49977 |                 96.32 |         0.936 | N/A            | N/A                             |
|   284 | L    |         0.00663 | False     |                          0.00247 |                 97.12 |         0.936 | N/A            | N/A                             |
|   285 | I    |         0.19052 | False     |                          0.38307 |                 97.5  |         0.936 | N/A            | N/A                             |
|   286 | Q    |         0.2384  | True      |                          0.14601 |                 95.72 |         0.71  | N/A            | N/A                             |
|   287 | K    |         0.24655 | True      |                          0.6579  |                 94.89 |         0     | N/A            | N/A                             |
|   288 | T    |         0.25928 | True      |                          0.29773 |                 92.92 |         0     | N/A            | N/A                             |
|   289 | D    |         0.39231 | True      |                          0.99563 |                 92.62 |         0     | N/A            | N/A                             |
|   290 | T    |         0.34327 | True      |                          0.98102 |                 91.76 |         0     | N/A            | N/A                             |
|   291 | G    |         0.21203 | False     |                          0.41003 |                 93.35 |         0     | N/A            | N/A                             |
|   292 | V    |         0.2443  | True      |                          0.71268 |                 96.36 |         0     | N/A            | N/A                             |
|   293 | S    |         0.25104 | True      |                          0.28362 |                 95.15 |         0     | N/A            | N/A                             |
|   294 | L    |         0.17909 | False     |                          0.78991 |                 96.44 |         0     | N/A            | N/A                             |
|   295 | Q    |         0.39211 | True      |                          0.38052 |                 95.09 |         0     | N/A            | N/A                             |
|   296 | T    |         0.21476 | False     |                          0.4857  |                 94.67 |         0     | N/A            | N/A                             |
|   297 | Y    |         0.3228  | True      |                          0.26869 |                 95.64 |         0     | N/A            | N/A                             |
|   298 | D    |         0.24565 | True      |                          0.62392 |                 94.09 |         0     | N/A            | N/A                             |
|   299 | D    |         0.3077  | True      |                          0.57931 |                 93.13 |         0     | N/A            | N/A                             |
|   300 | L    |         0.23289 | True      |                          0.32011 |                 94.78 |         0     | N/A            | N/A                             |
|   301 | L    |         0.09884 | False     |                          0.15086 |                 97.11 |         0     | N/A            | N/A                             |
|   302 | A    |         0.01791 | False     |                          0.02279 |                 97.2  |         0     | N/A            | N/A                             |
|   303 | K    |         0.04853 | False     |                          0.43129 |                 95.01 |         0     | N/A            | N/A                             |
|   304 | D    |         0.08385 | False     |                          0.43742 |                 93.85 |         0     | N/A            | N/A                             |
|   305 | C    |         0.03514 | False     |                          0.04119 |                 95.13 |         0     | N/A            | N/A                             |
|   306 | H    |         0.06472 | False     |                          0.15123 |                 95.03 |         0     | N/A            | N/A                             |
|   307 | C    |         0.01472 | False     |                          0.01302 |                 95.05 |         0     | N/A            | N/A                             |
|   308 | I    |         0.06281 | False     |                          0.39218 |                 93.88 |         0     | N/A            | N/A                             |


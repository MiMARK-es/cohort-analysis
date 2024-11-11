# Detailed Data for P07108


## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
## Summary & Metrics

- **UniProt Accession**: P07108
- **Gene Name**: DBI
- **Protein Name**: diazepam binding inhibitor (GABA receptor modulator, acyl-CoA binding protein)
- **Swiss Prot**: ACBP_HUMAN
- **Family**: other
- **Biomarker Application**:  
- **Number of Isoforms**: 0
- **Regulation**: 2
- **(transcriptomics) AUC**: 0.98
- **(transcriptomics) Fold Change**: 1.20
- **(transcriptomics) Regulation**: Upregulated
- **Discotope Epitope Count**: 27
- **Max n_uniprots (Homo)**: 1.0
- **Max n_uniprots (Hetero)**: N/A


## Expression Comparison

![Expression Comparison](./P07108_expression_comparison.png)

## Interactors

| preferredName_A   | preferredName_B   |   score |
|:------------------|:------------------|--------:|
| DBI               | TSPO              |   0.941 |
| DBI               | PEX3              |   0.926 |
| DBI               | APOA5             |   0.918 |
| DBI               | APOE              |   0.913 |

## Homologs

| uniprot_id   | gene_id   |
|:-------------|:----------|
| Q5TGU0       | TSPO2     |
| A0A7I2V560   | ACBD5     |
| K7EMH4       | ACBD4     |
| Q8N6N7       | ACBD7     |
| A0A0C4DGA2   | ECI2      |

## Biological Assemblies

|   Unnamed: 0 |   assembly |   n_uniprots | composition   | crystal_id   |
|-------------:|-----------:|-------------:|:--------------|:-------------|
|            0 |          1 |            1 | Homo          | 2fj9         |
|            1 |          2 |            1 | Homo          | 2fj9         |

## Combined Per-Residue Information

|   res | aa   |   epitope_score | epitope   |   relative_surface_accessibility |   modeling_confidence |   Aggregation | modification                              |
|------:|:-----|----------------:|:----------|---------------------------------:|----------------------:|--------------:|:------------------------------------------|
|     1 | M    |         0.22811 | False     |                          0.54917 |                 75.71 |         0     | N/A                                       |
|     2 | S    |         0.24414 | False     |                          0.41399 |                 88.76 |         0     | N-acetylserine                            |
|     3 | Q    |         0.39546 | False     |                          0.49255 |                 92.6  |         0     | N/A                                       |
|     4 | A    |         0.29516 | False     |                          0.64976 |                 96.74 |         0     | N/A                                       |
|     5 | E    |         0.32243 | False     |                          0.43436 |                 96.94 |         0     | N/A                                       |
|     6 | F    |         0.0733  | False     |                          0.02229 |                 98.05 |         0     | N/A                                       |
|     7 | E    |         0.50983 | True      |                          0.50358 |                 98.07 |         0     | N/A                                       |
|     8 | K    |         0.38838 | False     |                          0.63278 |                 97.95 |         0     | N6-acetyllysine; alternate                |
|     8 | K    |         0.38838 | False     |                          0.63278 |                 97.95 |         0     | N6-succinyllysine; alternate              |
|     9 | A    |         0.06217 | False     |                          0.03499 |                 98.08 |         0     | N/A                                       |
|    10 | A    |         0.21312 | False     |                          0.13888 |                 98.03 |         0     | N/A                                       |
|    11 | E    |         0.52234 | True      |                          0.41161 |                 97.81 |         0     | N/A                                       |
|    12 | E    |         0.25026 | False     |                          0.14527 |                 97.83 |         0     | N/A                                       |
|    13 | V    |         0.33926 | False     |                          0.15329 |                 97.53 |         0     | N/A                                       |
|    14 | R    |         0.57605 | True      |                          0.72092 |                 96.17 |         0     | N/A                                       |
|    15 | H    |         0.41488 | False     |                          0.54227 |                 97.21 |         0     | N/A                                       |
|    16 | L    |         0.26203 | False     |                          0.1302  |                 97.84 |         0     | N/A                                       |
|    17 | K    |         0.48575 | False     |                          0.74334 |                 97.35 |         0     | N6-succinyllysine                         |
|    18 | T    |         0.44282 | False     |                          0.49307 |                 97.13 |         0     | N/A                                       |
|    19 | K    |         0.63135 | True      |                          0.7345  |                 95.12 |         0     | N6-acetyllysine                           |
|    20 | P    |         0.16288 | False     |                          0.07881 |                 97.38 |         0     | N/A                                       |
|    21 | S    |         0.41705 | False     |                          0.41083 |                 97.81 |         0     | N/A                                       |
|    22 | D    |         0.68964 | True      |                          0.60707 |                 97.26 |         0     | N/A                                       |
|    23 | E    |         0.56622 | True      |                          0.73785 |                 98    |         0     | N/A                                       |
|    24 | E    |         0.24011 | False     |                          0.05439 |                 98.43 |         0     | N/A                                       |
|    25 | M    |         0.58274 | True      |                          0.42739 |                 98.04 |        21.657 | N/A                                       |
|    26 | L    |         0.42459 | False     |                          0.30089 |                 98.59 |        31.31  | N/A                                       |
|    27 | F    |         0.27995 | False     |                          0.35723 |                 98.69 |        31.439 | N/A                                       |
|    28 | I    |         0.17777 | False     |                          0.0832  |                 98.52 |        31.439 | N/A                                       |
|    29 | Y    |         0.57015 | True      |                          0.30206 |                 98.49 |        31.439 | Phosphotyrosine                           |
|    30 | G    |         0.02232 | False     |                          0.00644 |                 98.67 |        13.794 | N/A                                       |
|    31 | H    |         0.18507 | False     |                          0.10002 |                 98.71 |         8.404 | N/A                                       |
|    32 | Y    |         0.51617 | True      |                          0.37896 |                 98.7  |         7.605 | N/A                                       |
|    33 | K    |         0.4835  | False     |                          0.24167 |                 98.67 |         0     | N/A                                       |
|    34 | Q    |         0.03064 | False     |                          0.00821 |                 98.76 |         0     | N/A                                       |
|    35 | A    |         0.15587 | False     |                          0.06034 |                 98.4  |         0     | N/A                                       |
|    36 | T    |         0.4787  | False     |                          0.40224 |                 97.96 |         0     | N/A                                       |
|    37 | V    |         0.58825 | True      |                          0.42919 |                 98.32 |         0     | N/A                                       |
|    38 | G    |         0.25093 | False     |                          0.11588 |                 98.18 |         0     | N/A                                       |
|    39 | D    |         0.39284 | False     |                          0.37072 |                 98.66 |         0     | N/A                                       |
|    40 | I    |         0.3795  | False     |                          0.13722 |                 98.04 |         0     | N/A                                       |
|    41 | N    |         0.69288 | True      |                          0.70735 |                 97.61 |         0     | N/A                                       |
|    42 | T    |         0.75712 | True      |                          0.54102 |                 97.3  |         0     | N/A                                       |
|    43 | E    |         0.60883 | True      |                          0.84626 |                 97    |         0     | N/A                                       |
|    44 | R    |         0.57839 | True      |                          0.47783 |                 97.01 |         0     | N/A                                       |
|    45 | P    |         0.45574 | False     |                          0.31737 |                 96.65 |         0     | N/A                                       |
|    46 | G    |         0.68114 | True      |                          0.59396 |                 94.43 |         0     | N/A                                       |
|    47 | M    |         0.64048 | True      |                          0.85122 |                 89.26 |         0     | N/A                                       |
|    48 | L    |         0.67463 | True      |                          0.99473 |                 95.38 |         0     | N/A                                       |
|    49 | D    |         0.56064 | True      |                          0.42166 |                 96.71 |         0     | N/A                                       |
|    50 | F    |         0.73216 | True      |                          0.74615 |                 95.06 |         0     | N/A                                       |
|    51 | T    |         0.62409 | True      |                          0.63529 |                 95.05 |         0     | N/A                                       |
|    52 | G    |         0.53881 | True      |                          0.19655 |                 97.33 |         0     | N/A                                       |
|    53 | K    |         0.43709 | False     |                          0.28281 |                 97.61 |         0     | N/A                                       |
|    54 | A    |         0.51525 | True      |                          0.32376 |                 97.91 |         0     | N/A                                       |
|    55 | K    |         0.44515 | False     |                          0.38575 |                 98.38 |         0     | N6-succinyllysine; alternate              |
|    55 | K    |         0.44515 | False     |                          0.38575 |                 98.38 |         0     | N6-malonyllysine; alternate               |
|    55 | K    |         0.44515 | False     |                          0.38575 |                 98.38 |         0     | N6-acetyllysine; alternate                |
|    55 | K    |         0.44515 | False     |                          0.38575 |                 98.38 |         0     | N6-(2-hydroxyisobutyryl)lysine; alternate |
|    56 | W    |         0.32412 | False     |                          0.18758 |                 98.52 |         0     | N/A                                       |
|    57 | D    |         0.53201 | True      |                          0.23703 |                 98.21 |         0     | N/A                                       |
|    58 | A    |         0.27745 | False     |                          0.15979 |                 98.55 |         0     | N/A                                       |
|    59 | W    |         0.21263 | False     |                          0.03206 |                 98.75 |         0     | N/A                                       |
|    60 | N    |         0.44201 | False     |                          0.33039 |                 98.58 |         0     | N/A                                       |
|    61 | E    |         0.58868 | True      |                          0.73127 |                 98.45 |         0     | N/A                                       |
|    62 | L    |         0.27104 | False     |                          0.17064 |                 98.63 |         0     | N/A                                       |
|    63 | K    |         0.49783 | True      |                          0.64962 |                 98.47 |         0     | N/A                                       |
|    64 | G    |         0.49002 | True      |                          0.79954 |                 98.41 |         0     | N/A                                       |
|    65 | T    |         0.40923 | False     |                          0.33222 |                 98.36 |         0     | N/A                                       |
|    66 | S    |         0.30349 | False     |                          0.41252 |                 98.05 |         0     | N/A                                       |
|    67 | K    |         0.28404 | False     |                          0.4539  |                 97.94 |         0     | N/A                                       |
|    68 | E    |         0.36734 | False     |                          0.56172 |                 97.41 |         0     | N/A                                       |
|    69 | D    |         0.46064 | False     |                          0.47986 |                 98.14 |         0     | N/A                                       |
|    70 | A    |         0.00688 | False     |                          0.00128 |                 98.38 |         0     | N/A                                       |
|    71 | M    |         0.366   | False     |                          0.16473 |                 98.48 |         0     | N/A                                       |
|    72 | K    |         0.23717 | False     |                          0.52593 |                 98.19 |         0     | N/A                                       |
|    73 | A    |         0.3487  | False     |                          0.28848 |                 98.55 |         0     | N/A                                       |
|    74 | Y    |         0.18729 | False     |                          0.01713 |                 98.62 |         0     | N/A                                       |
|    75 | I    |         0.12167 | False     |                          0.1064  |                 98.49 |         0     | N/A                                       |
|    76 | N    |         0.48385 | False     |                          0.53149 |                 98.35 |         0     | N/A                                       |
|    77 | K    |         0.40099 | False     |                          0.16286 |                 98.54 |         0     | N6-succinyllysine; alternate              |
|    77 | K    |         0.40099 | False     |                          0.16286 |                 98.54 |         0     | N6-acetyllysine; alternate                |
|    78 | V    |         0.01627 | False     |                          0       |                 98.29 |         0     | N/A                                       |
|    79 | E    |         0.36499 | False     |                          0.34737 |                 98.2  |         0     | N/A                                       |
|    80 | E    |         0.52743 | True      |                          0.42925 |                 98.56 |         0     | N/A                                       |
|    81 | L    |         0.02325 | False     |                          0       |                 98.58 |         0     | N/A                                       |
|    82 | K    |         0.23403 | False     |                          0.2008  |                 97.88 |         0     | N/A                                       |
|    83 | K    |         0.41505 | False     |                          0.8662  |                 97.96 |         0     | N/A                                       |
|    84 | K    |         0.45068 | False     |                          0.59576 |                 98.25 |         0     | N/A                                       |
|    85 | Y    |         0.36356 | False     |                          0.19654 |                 97.61 |         0     | N/A                                       |
|    86 | G    |         0.2443  | False     |                          0.28263 |                 94.46 |         0     | N/A                                       |
|    87 | I    |         0.13861 | False     |                          0.58057 |                 88.02 |         0     | N/A                                       |


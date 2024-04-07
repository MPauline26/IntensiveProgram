# Intensive Program Repository

This repository documents the code used during the Intensive Program, which focused on credit risk modeling under the supervision of business professionals from UBS.

## Overview

The Intensive Program provided participants with the opportunity to deepen their knowledge of credit risk modeling in international teams. The program included lectures and tutorials covering topics such as default probability modeling, derivatives pricing, and statistical tools used for modeling. Teams were presented with a business case and given two weeks to work on the problem, culminating in a presentation of results.

## Contents
- `CaseStudy.ipynb`: Contains the code used to create the Probit model for estimating the Probability of Default.
- `DataPD_Analysis.xlsx`: Contains the summary of all results
- `CaseStudy/Export/`: Contains Exce-files with detailed results
- `CaseStudy/Export/`: Contains all figures created during the model development process

## Code Contents

The Python notebook in this repository contains code for the following tasks:

- Data preparation, including data cleaning, handling missing values using kNN-Imputer, and outlier treatment using winsorization.
- Univariate analysis, including the creation of plots, determination of discriminatory power and correlation matrices of variables.
- Development of a probit model.
- Evaluation of model performance using GINI and confusion matrix.

## Figures

Figures created during the analysis:

- Distribution plots before and after outlier and missing treatment.
- Box plots for outlier detection.
- ROC curve for discriminatory power evaluation.

## Dependencies

To run the Python notebook, you will need the following libraries:

- pandas
- numpy
- seaborn
- matplotlib
- statsmodels
- scipy
- scikit-learn

## Feedback and Contributions

If you have any feedback, encounter issues, or would like to contribute to this project, feel free to reach out.

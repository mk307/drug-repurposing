# drug-repurposing
Predicting Drug-Disease Association for Drug Repurposing using Machine Learning Models

1. Problem statement

With an increasing need and trend towards drug repurposing, it is imperative to utilize the relevant data available for repurposed drugs. However, this integrated domain has not received the due attention, which multiplies the significance of feature extraction and engineering to be further utilized by Machine Learning models to predict drug-disease association scores considering the disease for which a drug already known for a certain disease needs to be repurposed. Advances in Computational Biology has made it possible to apply a combination of Machine Learning models such as Linear Regression and Random Forest to conclude the accuracy of prediction by reporting errors such as mean squared errors in case of regression problems.

2. Introduction
   
a. Purpose Statement

The project comes with a purpose to extract features from “A Benchmark Dataset for Computational Drug Repositioning” (Tsatsaronis, 2015). This will eventually aid in making predictions regarding the drug-disease associations by analyzing if drug that already treats the old indication can treat the new indication mentioned in the dataset. In this way, it can be proved that the drug repurposed for new indication is actually based on the certain similarity measures.

b. Dataset Description

The dataset consists of a total of 41 drugs and against each Drug Bank ID and Drug Name, the corresponding Old Indication and New Indication is mentioned along with the Year of Repositioning, Status and Source.

3. Methodology

A. Feature Extraction

The proposed solution takes in to account the process of feature extraction from the dataset. Since the focus was on genetic measures, the first step was to identify the target genes of drug, old indication and new indication, following by the retrieval of sequences of each target gene and the calculation of sequence alignment scores.

i. Target Genes Identification

Against each DrugbankId and Drug Name both protein and gene targets were retrieved from (https://www.drugbank.ca/). Each drug had a number of protein targets, which further had more than one gene targets. All this information was taken in to account for further feature extraction since a total of 41 drugs resulted in 224 rows based on their corresponding targets.

Target genes were also identified for both old and new indication from (https://www.disgenet.org/) by applying a filter on N. PMIDs (Total Number of PMIDs Supporting the Association). The selected target gene was the one having the greatest value of N. PMIDs.

ii. Target Genes Sequence Retrieval

For each identified target gene, the RefSeq was obtained from (https://www.ncbi.nlm.nih.gov/gene) in FASTA format.

Note: In case a RefSeq was not available for a certain disease target gene, the gene having next greatest value of N. PMIDs was selected in case of both old and new indication.

iii. Calculation of Sequence Alignment Score

The obtained RefSeq of each target gene was aligned based on Smith–Waterman sequence alignment score (Gottlieb et al., 2011a). The following combinations for gene pairs were taken in to account:

a. Drug Target Gene – Old Indication Target Gene

b. Drug Target Gene – New Indication Target Gene

c. Old Indication Target Gene – New Indication Target Gene

To achieve the sequence alignment score, the following code in Python Language was applied with a match score = 1.0, mismatch score = -2.0, and gap score = -2.5 (Chang et al., 2010).

iv. Calculation of Drug-Disease Association Score

Once 224 rows against each drug target was filled using the obtained Sequence Alignment score, the scores corresponding to same drug were averaged to maintain the number of rows back to the total number of 41, which represents the total number of drugs considered. The calculation of combined Drug-Disease Association Score using Sequence Alignment Scores obtained for each combination was based on an approach of computing their weighted geometric mean (Perlman et al., 2011). However, in this project, to combine the similarities measures to a single Drug-Disease Association score for New Indication, Score(dr,di), a simple (unweighted) geometric mean was calculated using the following formula, an approach followed by (Gottlieb et al., 2011b):

Score(dr,di) = √𝑺(𝒅𝒓,𝒅𝒐)∗𝑺(𝒅𝒓,𝒅𝒏)∗𝑺(𝒅𝒐,𝒅𝒏)𝟑

Where:

Score(dr,di) = Drug-Disease Association Score for New Indication

S(dr,do) = Sequence Alignment Score between target gene sequences of Drug and Old Indication

S(dr,dn) = Sequence Alignment Score between target gene sequences of Drug and New Indication

S(do,dn) = Sequence Alignment Score between target gene sequences of Old and New Indication

v. Feature Scaling

For the purpose of Feature Scaling, Normalization was performed to convert all the similarity measures or the features in the range (0, 1). The Python code applied is mentioned as part of code applied for Model Building.

4. Feature Selection
   
The main strategy behind the selection of features was based on target genes sequence similarity measures. These measures, Score(dr,di), S(dr,do), S(dr,dn) and S(d0,dn) were taken as features to be fed in to the ML models to predict the Drug-Disease Association score, Score(dr,di), for the new indication.

5. Model Building
   
i. Selected Models

Since the target to be predicated was a numerical value, the Score(dr,di), the problem was therefore concluded to be a regression problem. The models were also selected based on the nature of the problem, and included:

a. Linear Regression

b. Decision Tree

c. Random Forest

6. Validation Method
   
For the purpose of validation, Train/Test splits were applied on the data which resulted in three parts:

a. Training Set

b. Testing Set

c. Validating Set

The model was trained with Training Data, evaluated on Validation Data and lastly tested on Testing Data, which made up a total of 20% of the total data. A seed was also provided be able to reproduce this split.

7. Evaluation Metric
   
Since the project caters to a regression problem, the evaluation metric should be able to report the error in prediction. Hence, Mean Squared Error (MSE), Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) were chosen as the evaluation metrics. The score of each evaluation metric was generated separately for Training and Testing data set in order to generalize each model.

8. Conclusion

Based on the results of indicated in both Table 2 and Table 3, it can be seen that each model performs better on Training Data as evident by lower error reported in the form of MSE, MAE and RMSE. Going further in to the detail, the Decision Tree gives perfect score in case of Training Data with all errors being 0, but it performs worse than both Linear Regression and Random Forest in Testing Data. This appears to be a case of Overfitting, which is more likely associated with nonparametric and nonlinear models that have more flexibility when learning a target function. These criteria are fulfilled by Decision Tree, which is very flexible and is subject to overfitting Training Data. This problem can be addressed by pruning a tree after it has learned in order to remove some of the detail it has picked up.

To further validate the results, the percentage difference between each Evaluation Metric score can be analyzed to check which model has least difference between results obtained for Training Data and Testing Data. Overall, it can be concluded that Random Forest is associated with lowest difference in score of each Evaluation Metric in the Training Data and Testing Data, hence indicating lowest error in making predictions of Score(dr,di) for New Indication. The lower the error, the higher the accuracy of the model to predict the correct drug-disease association score between each drug and the indication for which it needs to repurposed.

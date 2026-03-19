# Human vs Machine Learning Project

This project challenges you to explore the differences between human-designed algorithms and machine learning models. You will first create a human algorithm (pseudo-code) to classify data based on features, then translate that algorithm into Python. Next, you will train a K-Nearest Neighbors (KNN) classifier on the same dataset and compare your results. Finally, you will record a short screen-share with narration explaining your methods and observations.

You may work alone or with a partner. You may choose to work with the provided Penguins dataset, or select your own pre-cleaned dataset from the links below (I have suggested a few datasets as a guide, but you are welcome to select something different with approval).  The most important detail regarding your data-set is that your data needs to lend itself to classification.  For example, an iris with a sepal length of x and a petal width of y can be classified as ‘Setosa’. I also recommend that you use github codespaces, as you will need access to command-line tools that are unavailable in VS Code for EDU.

[UCI Machine Learning Repository](https://archive.ics.uci.edu/datasets)
 - Iris (classic 3-class classification)
 - Mushroom (binary classification: edible/poisonous)
 - Student Performance (predict grades, numeric features)

[Kaggle Datasets](https://www.kaggle.com/datasets)   *Note: For Kaggle, I will have to download the data for you and post on a shared drive.
 - Titanic survival dataset (binary classification)
 - Heart disease dataset (binary classification)
 - Breast cancer diagnosis (binary)
 - Penguins dataset (same as Kira, already cleaned)

---

**Team Members:**  
- Name 1  Jesse Rhodes
- Name 2 Landon Chittum 

**Dataset Used:**  
Penguins

**Source:**  
Provided Dataset

**Target Variable (What we are predicting):**  
Species

**Features Used:**  
- Feature 1  
- Feature 2  
- Feature 3

**[Video Review] https://www.youtube.com/watch?v=4dT1MyDw_RA (Our video)

GRAPHS

https://docs.google.com/document/d/1jL0wlDWOKum5R6o97Jhx4hXnQ7HrSbDRVuCG8MVIFpM/edit?usp=sharing **

## Human Algorithm

### Pseudo-Code
```text
Write your human decision rules here.
```

When examining the data and visualizations, we focused on the features Culmen Length and Culmen Depth because thats how we define the penguins.

The plots/tables suggested a possible threshold for their culmen length , and we considered values above or below this point to see how they might relate to the types of penguins there are.

From the summary tables and visualizations, it appeared that culmen length could influence classification, which led us to which species our penguins are in our decision rules.

### Confusion Matrix

Accuracy: 56.31%

| Actual \ Predicted | Class 1 | Class 2 | Class 3 |
|-------------------|---------|---------|---------|
| **Class 1**       |   12    |    30   |     3   |
| **Class 2**       |    4    |   13    |     4   |
| **Class 3**       |    0    |    4    |    33   |

One example where our algorithm worked well is when the inputs were what type of penguins we , leading to a correct prediction of Gentoo in class 3 because we had 33 right.

An example where the algorithm did not perform as expected is when the inputs were correct, resulting in a prediction of none wrong with gentoos instead of Chinstrap, which may have happened because of a harder way to classify them.

These examples of success and failure highlight patterns in the data or limitations in our rules, such as Gentoo in class 3.

<img width="315" height="334" alt="image" src="https://github.com/user-attachments/assets/23ee1e49-da76-47c2-97b8-c8fbcbef179c" />

## Machine Learning Model

We chose a value of k = 1 after comparing model performance across different values of k and observing that it gets very hard to identify penguins after that because they need specific classifications.

When analyzing the outputs and metrics, we noticed that changing k affected how many penguins are in certain groups, which influenced our final choice.

Based on the results shown in the tables or visualizations, k = 1 best matched our goals for model performance because it was the most accurate way.

### Confusion Matrix

Accuracy: 71%

| Actual \ Predicted | Adelie | Chinstrap | Gentoo |
|-------------------|---------|---------|---------|
| **Adelie**       |    33     |    12     |   0      |
| **Chinstrap**       |  17       |   4     |   0     |
| **Gentoo**       |     0    |     0    |    37     |

The table/visualization shows a clear pattern where the model predicts penguins when they have certain beak sizes, indicating a strong relationship between these features.

The confusion matrix reveals that the model most often confuses Chinstrap penguins with Adelie, suggesting these classes have similar feature values.

Compared to the human algorithm, the KNN model shows different behavior when we give it the data, as seen in the all visualization.

<img width="315" height="334" alt="image" src="https://github.com/user-attachments/assets/199ae59d-3470-40c6-9669-60e62b211619" />



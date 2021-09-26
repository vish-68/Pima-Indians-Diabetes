
# Pima Indians Diabeties

This dataset is originally from the National Institute of
 Diabetes and Digestive and Kidney Diseases. The 
 objective of the dataset is to diagnostically predict 
 whether or not a patient has diabetes, based on certain 
 diagnostic measurements included in the dataset. Several 
 constraints were placed on the selection of these 
 instances from a larger database. In particular, all 
 patients here are females at least 21 years old of Pima 
 Indian heritage.
## Data Analysis

In Pima Indians Diabeties dataset we have 9 features(including target 
variable) and 768 records.

* Pregnancies : Number of times pregnant.
* Glucose : Plasma glucose concentration a 2 hours in an
  oral glucose tolerance test.
* BloodPressure : Diastolic blood pressure (mm Hg).
* SkinThickness : Triceps skin fold thickness (mm).
* Insulin : 2-Hour serum insulin (mu U/ml).
* BMI : Body mass index (weight in kg/(height in m)^2).
* DiabetesPedigreeFunction : Diabetes pedigree function.
* Age : Age(in Years)
* Outcome : Class variable (0 or 1) 268 of 768 are 1, the 
  others are 0
## Approach

Our Main goal is to know that whether which check whether the patientis Diabetic
or Non-Diabetic

* Data Exploration : Exploring dataset using pandas, numpy, matplotlib and seaborn.
* Data visualization :Ploted graphs to get insights about dependend and independed variables.
* Model Selection I : Tested all base models to check the base accuracy. Also ploted and calculate Performance Metrics to check whether a model is a good fit or not.
* Model Selection II : After testing all base if some of them are not working properly then we have to do model tunning. 
* Pickle File : Selected model as per best accuracy and created pickle file using pickle library.
* Webpage & deployment : Created a webform that takes all the necessary inputs from user and shows output. After that I have deployed project on Herokuapp. 

## Technologies Used

* Jupyter notebook, Spyder, VScode Is Used For IDE.
* For Visualization Of The Plots Matplotlib , Seaborn Are Used.
* Herokuapp is Used For Model Deployment.
* Front End Deployment Is Done Using HTML, CSS, Bootstrap.
* Flask is for creating the application server and pages.
* Git Hub Is Used As A Version Control System.
* os is used for creating and deleting folders.
* csv is used for creating .csv format file.
* numpy is for arrays computations and mathematical operations
* pandas is for Manipulation and wrangling structured data
* scikit-learn is used for machine learning tool kit
* pickle is used for saving model
* Logistic regression is used for LogisticRegression Implementation.
* SGD is used for SGDClassifier Implementation.
* K-Nearest Neighbors is used for KNeighborsClassifier Implementation.
* SVM is used for SVC Implementation.
* Decision Tree is used for DecisionTreeClassifier Implementation.
* Extra Trees is used for ExtraTreesClassifier Implementation.
* Random forest is used for RandomForestClassifier Implementation.
* Ada boost is used for AdaBoostClassifier Implementation.
* Gradient is used for GradientBoostingClassifier Implementation.
* XGboost is used for XGBClassifier Implementation
* Ensemble is used for VotingClassifier Implementation.
## Deployment

**Herokuapp Link:** https://pima-indians-diabeties.herokuapp.com/
  
## Deployment

To Clone this project run

```bash
git clone https://github.com/vish-68/Pima-Indians-Diabetes
```
Go to Project directory
```bash
cd Pima-Indians-Diabetes
```
Install dependencies
``` bash
pip install -r requirements.txt
```  
Run the app.py
```bash
python app.py
```
## Conclusion

We developed Pima Indians Diabeties model which is capable to predict
whether the patient is diabetic or non-diabetic. In this dataset 9 features
(including target variable) and 768 records.
* Our 1st step is to import dataset and check all
  the details like shape, info(), describe() for getting better knowledge
  about data or each variable.
* 2nd step is to checking missing value and datatype of missing variable
  by looking at info(). after that we have to delete those 
  variable whose missing value is more than 50% of data. Other 
  variable should be treat as repect to their datatype.
* 3rd step After handling all this we have to do data 
  visualization for getting some insight for eg. we have to check 
  for ouliers, imbalanced variable or imbalanced data so we have to 
  remove ouliers or do upsampling for those.
* 4th step Splitting data into training and validation data and building 
  different ML model like LogisticrRegression, SGDClassifier, 
  KNeighborsClassifier, SVR, DecisionTreeRClassifier, ExtraTreesClassifier, 
  RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, 
  VotingClassifier, XGBClassifier. Out of all ExtraTreesClassifier is working 
  properly.
* Last step is model Deployment using Flask Framework.
  For model deployment we have to dump our model using pickle library
  and can save our model in .pkl or .sav extension.

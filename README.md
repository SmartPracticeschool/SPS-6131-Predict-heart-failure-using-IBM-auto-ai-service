# Predict-Heart-Failure-Using-IBM-Auto-Ai-Service

## Category: 

IBM Cloud Application

## Skills Required: 

* IBM Nodered
* IBM Watson Studio
* IBM Machine Learning

## Project Description:

* Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide.
* Heart failure is a common event caused by CVDs and this dataset contains 9 features that can be used to predict mortality by heart failure.
* In this project, you need to build a model using Auto AI and build a web application where we can get the prediction of heart failure.

## Services Used:

* IBM Watson Studio
* IBM Watson Machine Learning
* Node-RED
* IBM Cloud Object Storage

This code pattern can be thought of as two distinct parts:
* A predictive model will be built using AUTO AI service within a Machine learning instance on IBM Watson Studio. The model is then deployed to the Watson Machine Learning service, where it can be accessed via a REST API.
* A NodeRED web app that allows a user to input some data to be scored against the previous model.

## Prerequisites

* An [IBM Cloud Account](https://cloud.ibm.com)
* An account on [IBM Watson Studio](https://dataplatform.cloud.ibm.com/).

## Sample output:

Sample output and Architecture diagrams are added in this repositary 


### 1. Setup project and data in Watson Studio

To complete this code pattern we'll need to do a few setup steps before creating our model. In Watson Studio we need to: create a project, add our patient data (which our model will be based on), upload our notebook, and provision a Watson Machine Learning service.

## 1.1. Create a project in Watson Studio

* Log into IBM's [Watson Studio](https://dataplatform.cloud.ibm.com). Once in, you'll land on the dashboard.
* Create a new project by clicking `+ New project` and choosing `AUTO AI`:
* Enter a name for the project name and click `Create`.

## 1.2 Add patient data as an asset

The data used in this example was generated using a normal distribution. Attributes such as age, gender, heartrate, minutes of exercise per week, and cholesterol are used to create the model we will eventually deploy.

* A panel on the right of the screen will appear to assit you in uploading data.

  * Ensure you're on the `Load` tab.
  * Click on the `browse` option. From your machine, browse to the location of the [`patientdata1.csv`] file in this repository, and upload it. 
  * Once uploaded, go to the `Files` 
  * Ensure the `patientdata1.csv` 

* **TIP:** Once successfully uploaded, the file should appear in the `Data assets` section of the `Assets` tab.

## 1.3 Provision a Watson Machine Learning service

* Click on the navigation menu on the left (`☰`) to show additional options. Click on the `Watson Services` option.
* From the overview page, click `+ Add service` on the top right and choose the `Machine Learning` service. Select the `Lite` plan to avoid fees.
* Once provisioned, you should see the service listed in the `Watson Services` overview page. **Select the service by opening the link in a new tab.**  We're now in the IBM Cloud tool, where we will create service credentials for our now Watson Machine Learning service. Follow the numbered steps in the image below. **We'll be using these credentials in Step 2, so keep them handy!**.

* **TIP:** You can now go back the project via the navigation menu on the left (`☰`).

### 2. Create Node-Red app in cloud foundary services and Develop a web page.

* refer this page to install Node red [https://developer.ibm.com/components/node-red/tutorials/how-to-create-a-node-red-starter-application/]

## 2.1 Open Node Red flow editor

* Go do Dashboard and select Cloudfoundary apps and click on NODE RED. You will be Redirected to NODE RED page.
* Below the title you may find Visit App URL [https://node-red-lgrjw-2020-09-30.eu-gb.mybluemix.net/] click Visit App URL.
* You may find the button called " Go to your Node RED flow editor " click it. You will be redirected to Node RED workspace.
* Create a New flow And import "Flows.json" file found in NODE RED web app folder in this repositary.

## 2.2 Edit Your Flow

* Double click on Pre-tocken tab and enter Model API In 'var apikey'

# Generate API key

* Go to dashboard and you may find 'Manage' on top bars. click it and select Access(IAM) 
* Find API keys on left side of the page
* Click on ' Create An IBM cloud key  '. Give a name and generate your own APIkey.

## 2.3 HTTP request

* Double click on your second ''http request' tab and find the URL  
* Add your "Models URL" in that URL text box with an extension [?version=2020-09-01] 

## 2.4 Deploy

* Click on Deploy button on top right corner to Deploy your flow. 
* Once deployed successfully You may find The Dashboard icon down to the deploy button. click on it
* Near 'Theme' you wil find a small pop screen button. Click it.
* Your Web page will be displayed. Enter New patient detais and check the model.




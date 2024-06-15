**Zillow Data Analytics Project | End-To-End Python ETL Pipeline **

**Overview**

In this project, I focused on building and automating a Python ETL process. 
The process involves extracting real estate properties data from the Zillow Rapid API and loading it into an Amazon S3 bucket. 
This action triggers a series of AWS Lambda functions, which transform the data, convert it into CSV format, and load the resulting file into another S3 bucket using Apache Airflow. 
Apache Airflow employs an S3KeySensor operator to monitor the S3 bucket for the presence of the transformed data before loading it into Amazon Redshift.

Once the data is loaded into AWS Redshift, I connected Amazon QuickSight to the Redshift cluster to visualize the Zillow data obtained from the Rapid API.

**Key Technologies**

Apache Airflow: An open-source platform used for orchestrating and scheduling workflows and data pipelines.

Amazon S3: For storage of raw and processed data.

AWS Lambda: To process and transform the data.

Amazon Redshift: For data warehousing.

Amazon QuickSight: For data visualization.


**Project Steps:**

Install Apache Airflow: Learn to set up Apache Airflow from scratch.

Schedule the ETL Pipeline: Automate the extraction, transformation, and loading process.

Utilize S3KeySensor: Monitor S3 buckets for the presence of transformed data.

Set Up AWS Lambda Functions: From scratch, to handle data transformation.

Configure Amazon Redshift: Set up the Redshift cluster for data storage.
Visualize Data with QuickSight: Connect QuickSight to Redshift for data visualization.

Here is the dashboard I generated using Quicksight -
![image](https://github.com/nanditaNG/Zillow/assets/75269866/95b9614a-bbe0-46f1-adc4-e73b261f3c4b)


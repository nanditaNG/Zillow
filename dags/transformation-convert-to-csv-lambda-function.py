import boto3
import json
import pandas as pd

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']
        
        target_bucket = 'cleaned-data-zone-csv-bucket-ng'
        # target_file_name = object_key[:-5]
        if object_key.endswith('.json'):
            target_file_name = object_key[:-5]
        else:
            target_file_name = object_key 
        
        
        # Wait until the object exists
        waiter = s3_client.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket, Key=object_key)
        
        # Retrieve the object
        response = s3_client.get_object(Bucket=source_bucket, Key=object_key)
        data = response['Body']
        data = response['Body'].read().decode('utf-8')
        data = json.loads(data)
        # print(data)
        
        # Convert JSON to DataFrame
        f= []
        for i in data["results"]:
            f.append(i)
        df = pd.DataFrame(f)
        
        # Print DataFrame columns for debugging
        # print(f"DataFrame columns: {df.columns.tolist()}")
        
        # Selecting specific columns
        selected_columns = ['bathrooms', 'bedrooms', 'city', 'homeStatus', 'homeType',
                            'livingArea', 'price', 'rentZestimate', 'zipcode', 'year']
        
        if not all(col in df.columns for col in selected_columns):
            raise ValueError("One or more selected columns are not in the DataFrame")
        
        df = df[selected_columns]
        # print(df)
        
        # Convert DataFrame to CSV
        csv_data = df.to_csv(index=False)
        bucket_name = target_bucket
        object_key=f"{target_file_name}.csv"
        
        # Upload CSV to S3
        s3_client.put_object(Bucket=target_bucket, Key=object_key, Body=csv_data)
        
        print(f"CSV file uploaded to: s3://{target_bucket}/{target_file_name}.csv")
        
        return {
            'statusCode': 200,
            'body': json.dumps('CSV conversion and S3 upload completed successfully')
        }
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }

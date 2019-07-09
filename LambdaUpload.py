import json
import io
import zipfile
import mimetypes
import boto3

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    
    topic = sns.Topic('arn:aws:sns:us-east-1:722277795083:deployportfoliotopic')
    
    try:
        s3 = boto3.resource('s3')
        
        portfolio_bucket = s3.Bucket('portfolio.richardsirokman.info')
        build_bucket = s3.Bucket('portfoliobuild.richardsirokman')
        
        portfolio_zip = io.BytesIO()
        build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)
        
        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm,
                    ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
        print('job done!')
        topic.publish(Subject="Portfolio Deployed", Message="Portfolio Deployed Successfully")
           
    except:
        topic.publish(Subject="Portfolio Failed", Message="Portfolio Deployment FAILED")
        raise
            
    return 'Hello from Lambda'


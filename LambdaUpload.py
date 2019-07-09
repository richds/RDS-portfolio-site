import json
import io
import zipfile
import mimetypes
import boto3

def lambda_handler(event, context):
    
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
            
    return 'Hello from Lambda'
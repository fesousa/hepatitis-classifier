
.\setupenv.ps1
rm -r -fo .aws-sam
sam build
sam package --region us-east-1 --resolve-s3
sam deploy --stack-name api-hepatite --region us-east-1 --capabilities CAPABILITY_IAM --resolve-s3
aws s3 cp html/index.html s3://hepatite-classifier-fernando-sousa/index.html

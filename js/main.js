import React from 'react';
import ReactDOM from "react-dom";
import ExampleWork from './example-work';

const myWork = [
    {
        'title': "Services Provided",
        'href': "content/RichardSirokmanDevOpsResume2019.pdf",
        'desc': "Link to Resume",
        'body': "I provide help to growing companies who need to improve their \
        software engineering practices. If your company has created an application that runs\
        on AWS, or you are thinking of transitioning to the cloud, I can help.\
        Please click the link above for a link to my PDF resume.",
        'image': {
            'desc': "Thermopolis hot spring",
            'src': "images/example3.png",
        }
    },
    {
        'title': "AWS CI/CD in 5 Minutes",
        'href': "https://s3.amazonaws.com/portfolio.richardsirokman.info/content/CI_CD+on+AWS+in+5+minutes.pdf",
        'desc': "PDF slideshow for CI/CD",
        'body': "",
        'image': {
            'desc': "Southern Utah Canyons",
            'src': "images/whitecanyon.png",
            'comment': ""
        }
    },
    {
        'title': "How this site is built",
        'href': "https://github.com/richds/RDS-portfolio-site",
        'desc': "Link to Git repo",
        'body': "This site is built using React and is hosted on AWS. \
        Changes are managed through an automated pipeline with Git, CodeBuild & CodePipeline.\
        The pipeline is tested with Chai and Mocha.\
        Automated deployments use AWS Lambda function in Python and Boto3.\
        This page is served by Cloudfront from an S3 bucket.\
        Click the link to see the Git Repo",
        'image': {
            'desc': "balls art project",
            'src': "images/balls.png",
        }
    }
]

ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'))
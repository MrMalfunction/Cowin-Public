# Cowin Vaccine Tracker Discord Bot

## Serverless Vaccine Tracker using AWS Lambda and Discord Webhook

### Directory

* ```cowin_bot``` &nbsp;&nbsp;&nbsp;&nbsp;----> &nbsp;&nbsp;Main Lambda Function Folder
    * ```app.py``` &nbsp;&nbsp; ---> Main python file
    * ```reuirements.txt```&nbsp;&nbsp; ---> requirements file required to run function
* ```packaged.yaml``` ---> Packed Application for deployment on Servreless Application Repository
* README.md ---> Instructions for deployment
* ```template.yaml``` ---> Cloudformation template required for deployment from SAM CLI

---

## Requirements

### * Discord Webhook URL (to learn more about webhook [click here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks))

### * District Code for official Cowin API (to get your district code [click here](https://github.com/MrMalfunction/Cowin-Discord-Bot/blob/master/district_code.md))

### * Role id of your district(on how to copy id [click here](https://support.discord.com/hc/en-us/community/posts/360048094171-Get-Role-ID))

---

## How to Setup

1. Create an AWS Account
2. [Go Here](https://console.aws.amazon.com/lambda/home#/create/app?applicationId=arn:aws:serverlessrepo:ap-south-1:404907247506:applications/Cowin-Discord-Bot)
3. Paste all the required inputs (don't leave blank)
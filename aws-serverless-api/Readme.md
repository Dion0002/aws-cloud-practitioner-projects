## **1️⃣ Project Overview**

This project is a **serverless CRUD API** built with **AWS Lambda, API Gateway, and DynamoDB**.  
It allows you to create, list, update (PATCH), and delete tasks.

---

## 🚀 Architecture

- **API Gateway** → exposes REST API endpoints
- **AWS Lambda** → executes CRUD operations
- **IAM Premissions** → allow lambda function full access for dynamodb and cloudwatch 
- **DynamoDB** → stores tasks (`task_id` is the primary key)
- **CloudWatch Logs** → monitors Lambda executions

---


## **1️⃣ Deployment Steps**

### **Step 1: DynamoDB Setup**
1. Create a DynamoDB table named **`Tasks`**.  
2. Set **Primary Key** = `task_id` (String).  
3. Table will store items like:  task .
4. ![DynamoDb ](screenshots/dynamodb_table.png). 


### **Step 2: Lambda Function**
1. Create a Lambda function (Python 3.x). 
2. Add the CRUD code (lambda_function.py).  
3. Attach an IAM role with DynamoDB + CloudWatch permissions.  
![Lambda premission](screenshots/lambda_premission.png)


### **Step 3: API Gateway Setup**
1. Create a REST API in API Gateway. 
2. Add endpoints:
  - POST /create → Create task
  - GET /list → List tasks
  - PATCH /update → Update task
  - DELETE /delete → Delete task  
3. Integrate each endpoint with the Lambda function.  
4. Deploy API → Get public Invoke URL.
5. ![API](screenshots/api.png)

---


## **2️⃣ Lambda function with api**
![Lambda function overview](screenshots/lambda_function_overview.png)

---

## **3️⃣ Testing with Postman**
1. ![Post ](screenshots/post_task.png). 
2. ![Get ](screenshots/get_task.png).  
3. ![Put ](screenshots/put_task.png).
4. ![Delete ](screenshots/delete_task.png).  

--- 

## **4️⃣ DynamoDB Validation**
1. ![Added Item  ](screenshots/task_add.png). 
2. ![Updated Item  ](screenshots/updated_task.png).  

---

## **5️⃣  Monitoring**
1. CloudWatch Logs → See Lambda execution logs.

---
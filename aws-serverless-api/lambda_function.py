import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')  

def lambda_handler(event, context):
    http_method = event.get('httpMethod')
    body = json.loads(event['body']) if event.get('body') else {}
    query_params = event.get('queryStringParameters') or {}

    try:
        # CREATE
        if http_method == 'POST':
            if 'task_id' not in body:
                body['task_id'] = str(uuid.uuid4())  # auto-generate UUID if not provided

            table.put_item(Item=body)
            return {
                'statusCode': 201,
                'body': json.dumps({'message': 'Item created successfully', 'item': body})
            }

        # READ
        elif http_method == 'GET':
            if 'task_id' in query_params:
                response = table.get_item(Key={'task_id': query_params['task_id']})
                return {
                    'statusCode': 200,
                    'body': json.dumps(response.get('Item', {}))
                }
            else:
                response = table.scan()
                return {
                    'statusCode': 200,
                    'body': json.dumps(response.get('Items', []))
                }

        # UPDATE 
        elif http_method == 'PUT':
            task_id = query_params.get('task_id') or body.get('task_id')
            if not task_id:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'message': 'task_id is required'})
                }

            
            body['task_id'] = task_id

            table.put_item(Item=body)  
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Item updated successfully', 'item': body})
            }

        # DELETE
        elif http_method == 'DELETE':
            task_id = query_params.get('task_id') or body.get('task_id')
            if not task_id:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'message': 'task_id is required'})
                }

            table.delete_item(Key={'task_id': task_id})
            return {
                'statusCode': 200,
                'body': json.dumps({'message': f"Item {task_id} deleted successfully"})
            }

        # Invalid method
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

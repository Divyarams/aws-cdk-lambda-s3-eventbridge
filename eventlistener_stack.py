from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_events as events,
    aws_events_targets as event_target
)
from constructs import Construct

class EventlistenerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        #Create S3 bucket:
        bucket=s3.Bucket.from_bucket_arn(self,"catswebsite",bucket_arn="arn:aws:s3:::catswebsite") 
        
        #Create a Lambda fucntion
        lambda_function= _lambda.Function(self,"cdks3event",
                            runtime=_lambda.Runtime.PYTHON_3_9,
                            handler="lambdalistener.handler",
                            code=_lambda.Code.from_asset("F:\AWS\CDK\Eventlistener\lambda"),
                            environment={'BUCKET_NAME':"catswebsite"}
                            )  
        #Event Rule
        rule =events.Rule(self,"MyS3Rule",
                        event_pattern=events.EventPattern(
                            detail= {"eventSource": ["s3.amazonaws.com"],
                                     "eventName": ["PutObject"],
                                    "requestParameters": {
                                    "bucketName": ["catswebsite"]
                                    }
                                    },
                            resources=[bucket.bucket_arn],
                            source=["aws.s3"]
                            )
                         
                            )
        #s3.BucketProps(bucket_name=bucket.bucket_name,
        #event_bridge_enabled=True)  
        rule.add_target(event_target.LambdaFunction(lambda_function))



        #Create event notifications for Object creation
        #notifications=s3_notify.LambdaDestination(lambda_function)
        #notifications.bind(self,bucket)
        #bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3_notify.LambdaDestination(lambda_function))
        #Create Event for .jpg only
        #bucket.add_object_created_notification(notifications,s3.NotificationKeyFilter(suffix='.jpg'))
               

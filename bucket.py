import boto3
from django.conf import settings


class bucket:
    '''CDN Bucket manager

    	init method creates connection.

    	NOTE:
    		none of these methods are async. use public interface in tasks.py modules instead.
    	'''
    def __init__(self):
        session = boto3.session.Session()
        self.conn = session.client(
            service_name='s3',
            aws_access_key_id=settings.STORAGES['default']['OPTIONS']['access_key'],
            aws_secret_access_key=settings.STORAGES['default']['OPTIONS']['secret_key'],
            endpoint_url=settings.STORAGES['default']['OPTIONS']['endpoint_url'],
        )

    def get_objects(self):
        result = self.conn.list_objects_v2(Bucket=settings.STORAGES['default']['OPTIONS']['bucket_name'])
        if result['KeyCount']:
            return result['Contents']
        else:
            return None

    def delete_object(self, key):
        self.conn.delete_object(Bucket=settings.STORAGES['default']['OPTIONS']['bucket_name'], Key=key)
        return True

bucket = bucket()
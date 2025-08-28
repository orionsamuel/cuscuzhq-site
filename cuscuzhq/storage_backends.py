from storages.backends.s3boto3 import S3Boto3Storage
import os

class PublicMediaStorage(S3Boto3Storage):
    default_acl = "public-read"
    file_overwrite = False
    querystring_auth = False

    def url(self, name):
        from django.conf import settings
        return f"https://{os.environ.get('SUPABASE_PROJECT_ID')}.supabase.co/storage/v1/object/public/{os.environ.get('SUPABASE_BUCKET_NAME')}/{name}"
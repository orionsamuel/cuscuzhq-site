import os
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from supabase import create_client


class SupabaseStorage(Storage):
    def __init__(self):
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        self.bucket = os.getenv("SUPABASE_BUCKET")
        self.client = create_client(url, key)

    def _save(self, name, content):
        # Faz upload para Supabase
        res = self.client.storage.from_(self.bucket).upload(name, content.read())
        if res.get("error"):
            raise Exception(res["error"]["message"])
        return name

    def _open(self, name, mode="rb"):
        # Faz download do arquivo
        res = self.client.storage.from_(self.bucket).download(name)
        return ContentFile(res)

    def url(self, name):
        # Gera URL pública
        return self.client.storage.from_(self.bucket).get_public_url(name)
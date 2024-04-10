from typing import List
from ninja import NinjaAPI, Schema
from datetime import datetime
from .models import Document

api = NinjaAPI(title="DADA-Forest API")


class DocumentOut(Schema):
    id: int
    identifier: str
    url: str
    description: str


@api.get("/health")
def health(request):
    now = datetime.now()
    return {
        "msg": "ok",
        "data": now,
    }


@api.get("/documents", response=List[DocumentOut])
def documents(request):
    documents = Document.objects.all()
    return documents

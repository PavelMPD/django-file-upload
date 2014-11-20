# -*- coding: utf-8 -*-
import uuid
import os
from django.db import models


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('documents', filename)


class Document(models.Model):
    docfile = models.FileField(upload_to=get_file_path)

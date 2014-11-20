# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from upload_file.models import Document
from upload_file.forms import DocumentForm

from base64 import b64decode
from django.core.files.base import ContentFile
from django.http import JsonResponse


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('upload_file.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    documents = [d for d in documents]

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def file_list(request):
    # Handle file upload
    form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    documents = [d for d in documents]

    # Render list page with the documents and the form
    return render_to_response(
        'ajax_upload.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


def json_upload(request):
    data = request.POST['data']
    filename = request.POST['filename']
    data = b64decode(data)
    docfile = ContentFile(data, filename)
    newdoc = Document(docfile=docfile)
    newdoc.save()
    return  JsonResponse({"result": True})
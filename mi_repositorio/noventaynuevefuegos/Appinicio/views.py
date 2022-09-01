from mailbox import NoSuchMailboxError
from pipes import Template
from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render



def inicio (request):

    return render(request, "Appinicio/inicio.html")
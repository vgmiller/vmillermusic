from django.shortcuts import render
from music.models import Piece, Program, Concert
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from music.forms import ContactForm
from django.contrib import messages
from django.conf import settings
from datetime import datetime

def music_index(request):
	context = {
		"breakpoints": settings.IMAGE_BREAKPOINTS,
	}
	return render(request, "music_index.html", context)

def music_about(request):
    context = { 
		"breakpoints": settings.IMAGE_BREAKPOINTS,
    }
    return render(request, "music_about.html", context)

def music_recordings(request):
    context = {
		"breakpoints": settings.IMAGE_BREAKPOINTS,
    }
    return render(request, "music_recordings.html", context)

def music_repertoire(request):
    repertoire = {}
    repertoire["Concertos"] = Piece.objects.filter(category=1).order_by('composer__lastName')
    repertoire["Solos with Orchestra"] = Piece.objects.filter(category=2).order_by('composer__lastName')
    repertoire["Unaccompanied"] = Piece.objects.filter(category=4).order_by('composer__lastName')
    repertoire["Solos with Piano"] = Piece.objects.filter(category=3).order_by('composer__lastName')
    context = {
        "repertoire": repertoire
    }
    return render(request, "music_repertoire.html", context)

def music_samplePrograms(request):
    context = {
		"breakpoints": settings.IMAGE_BREAKPOINTS,
		"programs": Program.objects.order_by("pageOrder"),
    }
    return render(request, "music_samplePrograms.html", context)

def music_news(request):
    context = {
		"breakpoints": settings.IMAGE_BREAKPOINTS,
		"concerts": Concert.objects.filter(date__gte=datetime.today()).order_by("date"),
    }
    return render(request, "music_news.html", context)

def music_contact(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			tagline = " - Sent from %s" % from_email
			message+=tagline
			try:
				myEmail = 'vanessa.g.miller@gmail.com'
				send_mail(subject, message, myEmail, [myEmail])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			messages.success(request, 'Your message was sent!')
	context = { 
		"breakpoints": settings.IMAGE_BREAKPOINTS,
		"form": form,
    }
	return render(request, "music_contact.html", context)

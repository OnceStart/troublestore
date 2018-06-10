# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from models import troubles

# Create your views here.

def home(request):
	return render_to_response('home.html')

def troublesubmit(request):
	if request.method == 'POST':
		trouble = troubles()
		trouble.nickname = request.POST.get('nickname', 'no nickname')
		trouble.title = request.POST.get('title', 'no title')
		trouble.content = request.POST.get('content', 'no content')
		trouble.save()
	return render(request, 'trouble_submit.html')

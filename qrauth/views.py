from django.shortcuts import render


def qrcod(request):
	return render(request, 'qrauth/page.html')


def qrcod_activate(request):
	return render(request, 'qrauth/invalid_code.html')

'''from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import Feedback_form

def contact_view(request):
    if request.method == 'POST':
        form = Feedback_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            
            email_message = f"Message from {name} ({email}):\n\n{message}"

            send_mail(
                subject=subject,
                message=email_message,
                from_email=email,
                recipient_list=[settings.CONTACT_EMAIL],  
                fail_silently=False,
            )
            return HttpResponse("<h1>Feedback form submitted successfully</h1>")
    else:
        form = Feedback_form()

    return render(request, 'feed.html', {'form': form})'''

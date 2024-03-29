from datetime import date
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact
from post_office import mail
from django.core.files.base import ContentFile
# from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # Send email
        # mail.send(
        #     'lalinhabom@gmail.com', 'lalinhabom@gmail.com'
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        #     'traversy.brad@gmail.com',
        # [realtor_email, 'lalinhabom@gmail.com'],
        # fail_silently=False
        # )


        # mail.send(
        #     ['lalinhabom@gmail.com'],
        #     'lalinhabom@gmail.com',
        #     template='welcome_email',
        #     context={'foo': 'bar'},
        #     priority='now',
        #     attachments={
        #         'attachment1.doc': '/path/to/file/file1.doc',
        #         'attachment2.txt': ContentFile('file content'),
        #         'attachment3.txt': { 'file': ContentFile('file content'), 'mimetype': 'text/plain'},
        #     }
        # )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')


        return redirect('/listings/'+listing_id)
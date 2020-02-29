from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from datetime import datetime
from contacts.models import Contact


def contact(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # Check user already contacted
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )
        contact.save()

        # Email Send
        m_subject = 'Property Listing Inquiry'
        m_body = f'There has been an inquiry for {listing}. Sign into the admin panel for more ifno'
        f_mail = 'raselrostock@gmail.com'
        t_mail = [realtor_email, 'raselrostock@yahoo.com']
        send_mail(
            m_subject,
            m_body,
            f_mail,
            t_mail,
            fail_silently=False
        )
        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)

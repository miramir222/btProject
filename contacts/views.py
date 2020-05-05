from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .models import Contact
from listings.models import Listing
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing_id = request.POST['listing_id']    
        if request.user.is_authenticated:
            inquiry = Contact.objects.filter(listing_id=listing_id,user_id=request.user.id)
            if inquiry:
                messages.error(request,'You Query For This Proprty Is Already Submitted!!!')
                return redirect('/listings/'+listing_id)      
        contact = Contact(listing=listing,name=name,listing_id=listing_id,email=email,
        phone=phone,message=message,user_id=user_id)
        contact.save()
        send_mail(
            'Property Listing Inquiry',
            'Their Has Been Inquiry For '+listing+'. Sign into the admin panel for more info',
            'amir@anviam.com',
            [realtor_email,'tamannaaamir@gmail.com'],
            fail_silently=False
        )
        messages.success(request,'Your Request Has Been Submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)
        
    

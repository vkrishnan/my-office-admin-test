from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth import logout
from order.forms import RegistrationForm, OrderForm
from django.utils import timezone
from django.contrib.auth.models import User
from models import Order

# Create your views here.

def main_page(request):
    if request.user.is_authenticated():
        if request.user.is_superuser:
            orders = Order.objects.all()
            return HttpResponseRedirect('/admin')
        else:
            user = User.objects.get(username=request.user.username)
            orders = user.order_set.all()
    else:
        orders = None
    return render_to_response(
        'main_page.html',
        { 'user': request.user,
          'orders': orders})

def user_page(request, username):
    user = get_object_or_404(User, pk=username)
    
    orders = user.order_set.all()
    context = { 'username': username,
                'bookmarks': orders }

    return render(request, 'user_page.html', variables)

@staff_member_required      
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email'])
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    variables = RequestContext(request, {
                            'form': form})
                         
    return render_to_response(
                'registration/register.html', variables)
            

def order_page(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                                         user = request.user,
                                         name = form.cleaned_data['name'],
                                         category = form.cleaned_data['category'],
                                         order_date = timezone.now(),
                                         status = 'Pending'
                                         )
            return HttpResponseRedirect('/order/success/')
    else:
        form = OrderForm()
        
    variables = RequestContext(request, {
                            'form': form})
                         
    return render_to_response(
                'registration/order.html', variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
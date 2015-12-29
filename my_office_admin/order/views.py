from django.shortcuts import render
from django.template import RequestContext
from .forms import UserForm, CustomerForm
from django.shortcuts import render_to_response

# Create your views here.
def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and OrderForm.
        user_form = UserForm(data=request.POST)
        customer_form = CustomerForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and customer_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            customer = customer_form.save(commit=False)
            customer.user = user

            # Now we save the order model instance.
            customer.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, customer_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        customer_form = CustomerForm()

    # Render the template depending on the context.
    return render_to_response(
            'order/register.html',
            {'user_form': user_form, 'customer_form': customer_form, 'registered': registered},
            context)
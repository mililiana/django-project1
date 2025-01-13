from account.form import UserRegistrationForm

def register_form(request):
    return {'register_form':UserRegistrationForm}
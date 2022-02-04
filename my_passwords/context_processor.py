# from django.contrib.auth.models import User

# I am going to have to find a better use for working with a context processor.
# Turns out the user object was already available.
def add_user(request):  
    user = request.user
    if user.is_authenticated:
        name = user.first_name
    else:
        name = 'Anonymous'
    # return {
    #     'user': user,
    #     'name': name,
    # }
    return {}
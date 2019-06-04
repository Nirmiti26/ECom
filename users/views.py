from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.template.context_processors import csrf


def login(request):
    return render(request, 'users/login.html')


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('loggedin'))
    else:
        return HttpResponseRedirect(reverse('invalid_login'))


def loggedin(request):
    return render_to_response('users/loggedin.html',
                              {'full_name': request.user.username},
                              context_instance=RequestContext(request))


def invalid_login(request):
    return render_to_response('users/invalid_login.html',
                              context_instance=RequestContext(request)
                              )


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))


def register_user(request):
    form = UserCreationForm(request.POST or request.GET)
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # print form
            return HttpResponseRedirect(reverse('register_success'))
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    print args
    return render_to_response('users/register.html', args)


def register_success(request):
    return render_to_response('users/register_success.html')

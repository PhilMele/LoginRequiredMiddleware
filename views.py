def login_user(request):
    if request.user.is_authenticated:
        return redirect('list-venues')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #next_param = request.POST.get('next') <-- old redirection when users when clicking on login from nav bar

            url= request.session.get('next_param', reverse('list-venues'))

            return redirect(url)
        else:
            messages.success(request,("There was an error, try again!"))
            return redirect('login_user')
    else:
        return render(request,'main/registration/login_user.html',{})
      
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            user = authenticate(username = form.cleaned_data['username'],
                                password = form.cleaned_data['password1'],)
            login(request,user)
            activateEmail(request, user, form.cleaned_data.get('email'))
            
            url= request.session.get('next_param', reverse('list-venues'))
            
            return redirect(url)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = RegisterForm()
    return render(request,'main/registration/register_user.html',{'form':form})

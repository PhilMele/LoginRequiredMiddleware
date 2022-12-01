MIDDLEWARE = [
  
    'mysite.middleware.LoginRequiredMiddleware', 
]





LOGIN_EXEMPT_URLS =(
    r'logout',
    r'register_user',
    r'accounts/google/login/',
    r'accounts/social/signup/',
    r'accounts/facebook/login/',
    r'password_reset/',
    
)

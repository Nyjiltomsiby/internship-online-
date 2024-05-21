from django.urls import path
from .views import views
from django.conf.urls.static import static
from django.conf import settings
from NEeduapp.views import HomePageView, coursePage, SignupView , LoginView ,signout
from NEeduapp.views.views import aboutPageView,coursesPageView, contactPageView,testimonialPageView
from NEeduapp.views.courses import MyCoursesList
from NEeduapp.views.checkout import verifyPayment,checkout
# from NEeduapp.views.mentor import  mentor_login, mentor_dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',HomePageView.as_view() , name = 'home'),
    path('my-courses', MyCoursesList.as_view() , name = 'my-courses'),
    path('course/<str:slug>', coursePage , name = 'coursepage'),
    path('about/',aboutPageView.as_view(), name='about'),
    path('courses/',coursesPageView.as_view(), name='courses'),
    path('contact/',contactPageView.as_view(), name='contact'),
    path('testimonial/',testimonialPageView.as_view(), name='testimonial'),
    path('signup', SignupView.as_view() , name = 'signup'),
    path('login', LoginView.as_view() , name = 'login'),
    path('logout/', signout , name = 'logout'),
    path('check-out/<str:slug>', checkout , name = 'check-out'),
    path('verify_payment', verifyPayment , name = 'verify_payment'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
   
    

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
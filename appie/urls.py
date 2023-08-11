from django.urls import path
from appie import views

urlpatterns = [
    path('studentdetail/<int:pk>',views.student_detail,name = 'studentdetail/pk'),
    path('studentlist/',views.student_list,name = 'studentlist'),
    path('studentcreate/',views.student_create,name = 'studentcreate '),
    path('studentapi/',views.student_api,name = 'studentapi'),
]
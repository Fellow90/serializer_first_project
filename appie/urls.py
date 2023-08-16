from django.urls import path
from appie import views

urlpatterns = [
    # path('studentdetail/<int:pk>',views.student_detail,name = 'studentdetail/pk'),
    # path('studentlist/',views.student_list,name = 'studentlist'),
    # path('studentcreate/',views.student_create,name = 'studentcreate '),
    #for function based view
    # path('studentapi/',views.student_api,name = 'studentapi'),
    #for class based view
    # path('studentapi/',views.StudentAPI.as_view(),name = 'studentapi'),
    path('student_api/',views.student_api, name = 'student_api'),
    path('student_api/<int:pk>/',views.student_api,name='student_api/pk'),

]

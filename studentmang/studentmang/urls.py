from django.contrib import admin
from django.urls import path
from app.views import home,add_student,get_all_std,get_single_std,update_student,delete_student
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("add_student/",add_student,name="add_student"),
    path("get_all_std/",get_all_std,name="get_all_std"),
    path("get_single_std/<int:id>/",get_single_std,name="get_single_std"),
    path("update_student/<int:id>/",update_student,name="update_student"),
    path("delete_student/<int:id>/",delete_student,name="delete_student"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

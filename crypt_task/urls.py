from django.urls import path

from crypt_task.views import CryptTaskAPIPost
from . import views

urlpatterns = [
    path('crypt_tasks/', CryptTaskAPIPost.as_view()),  # http://127.0.0.1:8000/crypt_tasks/
    path('crypt_tasks/<int:task_id>/', views.get_cryptographic),  # http://127.0.0.1:8000/crypt_tasks/<int:task_id>
]

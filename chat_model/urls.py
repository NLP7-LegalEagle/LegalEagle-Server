from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    # path("", views.ChatView.as_view(), name='chat_model'),
    # path("basic/", views.index_basic, name='index_basic'),
    path("rest/", views.index_rest, name='index_rest'),
    # path("basic/index-basic/", views.submit_text, name='submit_text1'),
    path("rest/index-rest/", views.PredictSentence.as_view(), name='submit_text2')
]

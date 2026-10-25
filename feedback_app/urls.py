from django.urls import path
from feedback_app.views import SignUpView,FeedbackListCreateView,FeedbackRetrieveUpdateDeleteView,FeedbackSummaryView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[
    path("signup/",SignUpView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path("feedbacks/",FeedbackListCreateView.as_view()),
    path("<int:pk>/",FeedbackRetrieveUpdateDeleteView.as_view()),
    path("summary/",FeedbackSummaryView.as_view())

]
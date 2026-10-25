from rest_framework import serializers

from django.contrib.auth.models import User

from feedback_app.models import Feedback

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password"]

        read_only_fields = ["id"]

class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:

        model=Feedback

        fields = "__all__"

        read_only_fields = ["id","student","created_at"]
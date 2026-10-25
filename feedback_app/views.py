from django.shortcuts import render,get_object_or_404

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from feedback_app.models import  Feedback
from feedback_app.serializers import UserSerializer,FeedbackSerializer
from feedback_app.permissions import IsOwner


# Create your views here.
class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class FeedbackListCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        qs = Feedback.objects.filter(student=request.user)

        serializer_instance = FeedbackSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = FeedbackSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(student=request.user)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class FeedbackRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    
    permission_classes = [IsOwner]


    def get(self,request,pk=None):

        instance = get_object_or_404(Feedback,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance = FeedbackSerializer(instance)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        instance = get_object_or_404(Feedback,id=pk)

        self.check_object_permissions(request,instance)

        form_data =  request.data

        serializer_instance = FeedbackSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Feedback,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response({"message":"deleted..."})


from django.db.models import Count

class FeedbackSummaryView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        response_data = {
            "total_feedback": 0,
            
        }

        feedback_transaction = Feedback.objects.filter(student=request.user)

        if feedback_transaction:

            total_feedback = feedback_transaction.count()

            response_data["total_feedback"] = total_feedback

            # sentiment summary

            sentiment_summary = feedback_transaction.values("sentiment").annotate(total=Count("id"))

            response_data["sentiment_summary"] = sentiment_summary

            # category summary

            category_summary = feedback_transaction.values("category").annotate(total=Count("id"))

            response_data["category_summary"] = category_summary

        return Response(data=response_data)
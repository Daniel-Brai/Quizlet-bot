from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer


class RandomQuestionView(APIView):

    """
    A simple view for getting a random question
    """
    
    def get(self, request, formate=None, **kwargs):
        question = Question.objects.filter().order_by('?')[:1]
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)


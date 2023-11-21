from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .Llama2 import Llama
from .models import InputSentence
from .serializers import InputSentenceSerializer

import torch, gc


def index_rest(request):
    return render(request, 'index_rest.html')

class PredictSentence(APIView):
    @csrf_exempt
    def get(self, request):
        query = InputSentence.ojects.all()
        print(query)
        serializer = InputSentenceSerializer(query, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            input_text = request.data.get('text', '')
            print(input_text)

            # Save input text to the database
            input_sentence = InputSentence(sentence=input_text)
            input_sentence.save()
            # Load the model
            
            gc.collect()
            torch.cuda.empty_cache()
            llm = Llama()
            gc.collect()
            torch.cuda.empty_cache()
            
            prediction = llm.text_generation(input_sentence)

            # Format the response (adjust as needed)
            response_data = {
                'input_text': input_text,
                'prediction': prediction,  # Convert to list for JSON serialization
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            # Log the exception for debugging
            print(f"Exception: {e}")

            # Return a generic error response
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
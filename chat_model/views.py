from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# from llama_cpp import Llama
from .models import InputSentence
from .serializers import InputSentenceSerializer
# from langchain.callbacks.manager import CallbackManager
# from langchain.llms import llamacpp
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

import replicate

# llm = Llama(model_path="/home/panwoo/3_2_classes/server-test/llama-2-7b-chat.Q3_K_L.gguf")
# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]) 


def index_rest(request):
    return render(request, 'index_rest.html')

class PredictSentence(APIView):
    @csrf_exempt
    def get(self, request):
        query = InputSentence.objects.all()
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
        
            # prompt = "Q: " + input_text + "? A:"
            # prediction = llm(prompt)
            output =replicate.run(
                "meta/llama-2-7b-chat:f1d50bb24186c52daae319ca8366e53debdaa9e0ae7ff976e918df752732ccc4",
                input={"prompt": input_text}
            )
            output = ' '.join(output)

            # Format the response (adjust as needed)
            response_data = {
                'input_text': input_text,
                # 'prediction': prediction.text,
                'prediction' : output
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            # Log the exception for debugging
            print(f"Exception: {e}")

            # Return a generic error response
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
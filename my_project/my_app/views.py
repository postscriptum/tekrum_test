from django.shortcuts import render, redirect, get_object_or_404
from .models import Purchase
from .serializers import PurchaseSerializer

from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


def home(request):
    return render(request, 'my_app/home.html')


class PurchaseList(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'my_app/update.html'

    def get(self, request, pk):
        purchase = get_object_or_404(Purchase, pk=pk)
        serializer = PurchaseSerializer(purchase, context={'request': request})
        return Response({'serializer': serializer, 'purchase': purchase})

    def post(self, request, pk):
        purchase = get_object_or_404(Purchase, pk=pk)
        serializer = PurchaseSerializer(purchase, data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'purchase': purchase})
        serializer.save()
        return redirect('home')


class PurchaseCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'my_app/create.html'

    def get(self, request):
        serializer = PurchaseSerializer(context={'request': request})
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = PurchaseSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('home')

from .models import Product
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse


class PageHome(View):
    def get(self, request):
        return render(request, 'home.html')



class SearchProduct(View):
    def get(self, request):
        query = request.GET.get('q', '')

        search_products = Product.objects.filter(
            title__iregex=query
        ).values('title', 'price', 'photo')

        return JsonResponse({
            'success': True,
            'query': query,
            'result': list(search_products),
            'count': len(search_products)
        }, status=200)

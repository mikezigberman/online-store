from django.shortcuts import render

def index(request):
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Catalog',
        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Adidas Originals Black Monogram Hoodie',
                'price': 100,
                'description': 'Soft fabric for sweatshirts. Style and comfort is a way of life.',
            },
            {
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'name': 'The North Face blue jacket',
                'price': 100,
                'description': 'Smooth fabric. Waterproof coating. Lightweight and warm down fill.',
            },
            {
                'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'name': 'ASOS DESIGN oversized sports top in brown',
                'price': 100,
                'description': 'Plush material. Comfortable and soft.',
            }
        ]
    }
    return render(request, 'products/products.html', context)
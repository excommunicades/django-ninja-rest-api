from ninja import NinjaAPI

from django.shortcuts import get_object_or_404

from api.schemas import (
    ProductIn,
    ProductOut,
)

from api.models import Product

api = NinjaAPI()

@api.get("/products", response=list[ProductOut])
def get_product_list(request):

    products = Product.objects.all()

    return products

@api.get("/product/{product_id}", response=ProductOut)
def get_product(request, product_id: int):

    product = get_object_or_404(Product, id=product_id)

    return product

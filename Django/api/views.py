from ninja import NinjaAPI

from django.shortcuts import get_object_or_404
from django.http import JsonResponse

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

    product_out = ProductOut.from_orm(product)

    return product_out

@api.post("/products", response=ProductOut)
def create_product(request, product_in: ProductIn):

    try:

        product = Product.objects.create(
            title=product_in.title,
            description=product_in.description,
        )

        product_out = ProductOut.from_orm(product)

        return product_out

    except Exception as e:

        return JsonResponse(status=400, data={"errors": f"Product did not create! {str(e)}"})

@api.put("/product/update/{product_id}", response=ProductOut)
def update_product(request, product_id: int, product_in: ProductIn):

    try:

        product = get_object_or_404(Product, id=product_id)

        if product_in.title:

            product.title = product_in.title

        if product_in.description:

            product.description = product_in.description

        product.save()

        product_out = ProductOut.from_orm(product)

        return product_out

    except Exception as e:

        return JsonResponse(status=400, data={"errors": f"Product did not update! {str(e)}"})
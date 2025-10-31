import graphene
from graphene_django import DjangoObjectType
from .models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "stock")

class UpdateLowStockProducts(graphene.Mutation):
    class Arguments:
        pass  # No arguments needed

    updated_products = graphene.List(ProductType)
    message = graphene.String()

    def mutate(self, info):
        low_stock_products = Product.objects.filter(stock__lt=10)
        for product in low_stock_products:
            product.stock += 10  # Restock by 10 units
            product.save()

        return UpdateLowStockProducts(
            updated_products=low_stock_products,
            message=f"{low_stock_products.count()} products updated successfully."
        )

class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()


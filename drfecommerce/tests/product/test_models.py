import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self, category_factory):
        #Arrange
        #Act
        obj = category_factory(name="test_cat")
        #Assert
        assert obj.__str__() == "test_cat"
        #Test ortaminda gercek database'e dokunmuyoruz. Test olusturuldugunda, test ortaminda bir database olusturuyoruz ve kullaniyoruz
        #Test ortamindaki database gercek database'in bir kopyasi oluyor ve bos olucak.
        

class TestBrandModel:
    def test_str_method(self, brand_factory):
        #Arrange
        #Act
        obj = brand_factory(name="test_brand")
        #Assert
        assert obj.__str__() == "test_brand"

class TestProductModel:
    def test_str_method(self, product_factory):
        #Arrange
        #Act
        obj = product_factory(name="test_product")
        #Assert
        assert obj.__str__() == "test_product"


class TestProductLineModel:
    def test_str_method(self, product_line_factory):
        obj = product_line_factory(sku="12345")
        assert obj.__str__() == "12345"

    def test_duplicate_order_values(self, product_line_factory, product_factory):
        obj = product_factory()
        product_line_factory(order=1, product=obj)
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=obj).clean()

class TestProductImageModel:
    def test_str_method(self, product_image_factory):
        obj = product_image_factory(url="test.jpg")
        assert obj.__str__() == "test.jpg"
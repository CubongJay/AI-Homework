import requests

BASE_URL = "http://localhost:8000"  # Update to match your API host
PRODUCTS_ENDPOINT = "https://fakestoreapi.com/products"

def test_get_products_success():
    response = requests.get(PRODUCTS_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_product_schema_integrity():
    response = requests.get(PRODUCTS_ENDPOINT)
    products = response.json()

    for product in products:
        assert "id" in product
        assert "title" in product
        assert "image" in product
        assert "price" in product
        assert "rating" in product
        assert isinstance(product["rating"], dict)
        assert "rate" in product["rating"]


def test_product_field_validations():
    response = requests.get(PRODUCTS_ENDPOINT)
    products = response.json()

    for product in products:
        # Title should not be empty
        assert product["title"].strip() != "", "Product title should not be empty"

        # Price should not be negative
        assert product["price"] >= 0, f"Negative price found: {product['price']}"

        # Rating rate should not exceed 5
        rate = product["rating"].get("rate")
        assert rate <= 5, f"Rating exceeds 5: {rate}"
        
        
        
        
def test_invalid_endpoint_returns_404():
    response = requests.get(INVALID_ENDPOINT)
    assert response.status_code == 404, "Invalid endpoint should return 404"


def test_product_ids_are_unique():
    response = requests.get(PRODUCTS_ENDPOINT)
    products = response.json()

    product_ids = [product["id"] for product in products]
    assert len(product_ids) == len(set(product_ids)), "Duplicate product IDs found"


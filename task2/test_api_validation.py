import requests
import pytest

API_URL = "https://fakestoreapi.com/products"

def test_api_response():
    """Test if the API returns a successful response code."""
    response = requests.get(API_URL)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_product_data_validation():
    """Test product data validation for required fields and constraints."""
    response = requests.get(API_URL)
    products = response.json()
    
    # List to store products with defects
    products_with_defects = []
    
    for product in products:
        defects = []
        
        # Check if title exists and is not empty
        if not product.get('title'):
            defects.append("Missing or empty title")
        
        # Check if price exists and is not negative
        price = product.get('price')
        if price is None:
            defects.append("Missing price")
        elif price < 0:
            defects.append(f"Negative price: {price}")
        
        # Check if rating exists and rate is not exceeding 5
        rating = product.get('rating', {})
        rate = rating.get('rate')
        if rate is None:
            defects.append("Missing rating rate")
        elif rate > 5:
            defects.append(f"Rating rate exceeds 5: {rate}")
        
        # If any defects found, add product to the list
        if defects:
            products_with_defects.append({
                'id': product.get('id'),
                'title': product.get('title'),
                'defects': defects
            })
    
    # Print products with defects
    if products_with_defects:
        print("\nProducts with defects:")
        for product in products_with_defects:
            print(f"\nProduct ID: {product['id']}")
            print(f"Title: {product['title']}")
            print("Defects:")
            for defect in product['defects']:
                print(f"- {defect}")
    
    # Assert that we found some products with defects
    assert len(products_with_defects) > 0, "No products with defects found" 
# API Data Validation Tests

This project contains automated tests to validate data from the Fake Store API (https://fakestoreapi.com/products). The tests check for various data quality issues and anomalies in the API response.

## Test Objectives

The tests verify the following criteria:
- Server response code (expected 200)
- Product data validation:
  - `title` (name) - must not be empty
  - `price` - must not be negative
  - `rating.rate` - must not exceed 5

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Setup

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Tests

To run the tests, execute the following command in the terminal:
```bash
python -m pytest test_api_validation.py -v
```

## Test Output

The test results will show:
- Overall test status (pass/fail)
- A detailed list of products with defects, including:
  - Product ID
  - Product title
  - Specific defects found for each product

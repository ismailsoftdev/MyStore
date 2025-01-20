# My Store

## Description

This is a simple Django application for managing products and orders. It includes a basic setup for listing products, viewing product details, and processing payments with a "Buy Now" flow. It also includes success and cancel pages after a transaction.

## Features

1. Product List: View a list of available products.
2. Product Details: View detailed information about a specific product.
3. Buy Now: Initiate a payment for a product and redirect to a Stripe checkout page.
4. Payment Success: Display a success message after a successful payment.
5. Payment Cancel: Display a message if the payment is canceled.

## Requirements

- Python 3.8 or higher
- Django 4.2
- Stripe Python library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/my-store.git
    ```

2. Navigate to the project directory:

    ```bash
    cd my-store
    ```

3. Create a virtual environment:
    - Windows: `python -m venv venv`
    - Linux/Mac: `python3 -m venv venv`

4. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Start the development server.
2. Access the application at http://localhost:8000.


# Vendor Sweets API

This Flask application provides an API for managing vendors, sweets, orders, and order items.

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```
   
2. **Navigate to the project directory:**
    ```bash
    cd <project_directory>
    ```

3. **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment:**

    On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

    On Windows:
    ```bash
    venv\Scripts\activate
    ```

5. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application:**
    ```bash
    python app.py
    ```

2. **Access the API endpoints using a tool like Postman or cURL:**

    - GET /vendors: Retrieve all vendors
    - POST /vendors: Create a new vendor
    - GET /vendors/<id>: Retrieve a specific vendor by ID
    - PUT /vendors/<id>: Update a specific vendor by ID
    - DELETE /vendors/<id>: Delete a specific vendor by ID

    - GET /sweets: Retrieve all sweets
    - POST /sweets: Create a new sweet
    - GET /sweets/<id>: Retrieve a specific sweet by ID
    - PUT /sweets/<id>: Update a specific sweet by ID
    - DELETE /sweets/<id>: Delete a specific sweet by ID

    - GET /orders: Retrieve all orders
    - POST /orders: Create a new order
    - GET /orders/<id>: Retrieve a specific order by ID
    - PUT /orders/<id>: Update a specific order by ID
    - DELETE /orders/<id>: Delete a specific order by ID

    - GET /order_items: Retrieve all order items
    - POST /order_items: Create a new order item
    - GET /order_items/<id>: Retrieve a specific order item by ID
    - PUT /order_items/<id>: Update a specific order item by ID
    - DELETE /order_items/<id>: Delete a specific order item by ID

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

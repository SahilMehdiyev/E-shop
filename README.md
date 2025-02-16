# E-Shop

## Overview
E-Shop is a fully functional e-commerce API built with Django Rest Framework (DRF). It provides essential features for managing products, orders, users, and payments. The project follows best practices in API development, including authentication, filtering, pagination, and background task processing with Celery.

## Features
- **User Authentication**: Token-based authentication using Django Rest Framework.
- **Product Management**: CRUD operations for products.
- **Order Management**: Create and track orders.
- **Filtering & Pagination**: Advanced filtering and pagination for product listings.
- **Middleware & Signals**: Implements custom middleware for logging and signals for event handling.
- **Celery & Redis**: Background task execution for email notifications and order processing.
- **Advanced Serializers**: Custom serializers with nested relationships and dynamic fields.
- **Django Admin**: Manage products, orders, and users from the Django admin panel.
- **Stripe Payment Integration**: Secure online payment processing.

## Installation

### Prerequisites
- Python 3.11+
- Django 5.1+
- PostgreSQL (or SQLite for development)
- Redis & Celery (for background tasks)

### Steps to Install

1. **Clone the Repository**
```bash
git clone https://github.com/SahilMehdiyev/E-shop.git
cd E-shop
```

2. **Create and Activate a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variables**
Create a `.env` file in the project root and add the following:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/eshop
CELERY_BROKER_URL=redis://localhost:6379/0
```

5. **Apply Migrations**
```bash
python manage.py migrate
```

6. **Create Superuser**
```bash
python manage.py createsuperuser
```

7. **Run the Development Server**
```bash
python manage.py runserver
```

8. **Run Celery Worker**
```bash
celery -A shop worker --loglevel=info
```

## API Endpoints

### Authentication
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| POST   | `/api/auth/login/`     | User login |
| POST   | `/api/auth/register/`  | User registration |
| POST   | `/api/auth/logout/`    | User logout |

### Product Management
| Method | Endpoint             | Description |
|--------|----------------------|-------------|
| GET    | `/api/products/`     | List all products |
| GET    | `/api/products/{id}/` | Retrieve a product |
| POST   | `/api/products/`     | Create a new product (Admin only) |
| PUT    | `/api/products/{id}/` | Update a product (Admin only) |
| DELETE | `/api/products/{id}/` | Delete a product (Admin only) |

### Order Management
| Method | Endpoint         | Description |
|--------|----------------|-------------|
| GET    | `/api/orders/`  | List user orders |
| POST   | `/api/orders/`  | Create a new order |
| GET    | `/api/orders/{id}/` | Retrieve order details |

### Payment
| Method | Endpoint           | Description |
|--------|-------------------|-------------|
| POST   | `/api/payment/checkout/` | Process payment |
| GET    | `/api/payment/status/`   | Check payment status |

## Technologies Used
- **Django Rest Framework (DRF)** - API development
- **PostgreSQL** - Database management
- **Celery & Redis** - Background task processing
- **Stripe API** - Payment integration
- **Django Signals & Middleware** - Event handling & request logging
- **Docker (optional)** - Containerized deployment

## Contribution
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature-branch`
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, feel free to reach out to [Sahil Mehdiyev](https://github.com/SahilMehdiyev).


# FastAPI Purchase Tracking System

A scalable web application built with FastAPI, PostgreSQL, and Nginx load balancing. This system allows tracking users and their purchases with a distributed architecture.

## Features

- User management (create and retrieve users)
- Purchase tracking (create and list purchases)
- Load balanced with Nginx (multiple FastAPI instances)
- PostgreSQL database for persistent storage
- Comprehensive error handling
- Docker containerization

## Tech Stack

- FastAPI (Python 3.11)
- PostgreSQL 15
- Nginx (Load Balancer)
- SQLAlchemy (ORM)
- Docker & Docker Compose

## Prerequisites

- Docker
- Docker Compose
- Python 3.11+ (for local development)

## Getting Started

1. Clone the repository:
```bash
git clone <repository-url>
cd nginx_postgres_fastapi
```

2. Start the services:
```bash
docker-compose up -d
```

3. The following services will be available:
- API (Load Balanced): http://localhost:80
- PostgreSQL: localhost:5432

## API Endpoints

### Users
- `POST /users/`
  - Create a new user
  - Body: `{"username": "string", "email": "string"}`
  - Returns: User object with ID

### Purchases
- `POST /purchases/`
  - Create a new purchase
  - Body: `{"user_id": int, "sku_name": "string", "price": float, "quantity": int}`
  - Returns: Purchase object with ID and timestamp

- `GET /users/{user_id}/purchases/`
  - Get user's purchase history
  - Returns: List of purchases

## Development

1. Install development dependencies:
```bash
pip install -r requirements.txt
```

2. Run tests:
```bash
pytest
```

## Project Structure

```
.
├── app.py              # FastAPI application
├── models.py           # SQLAlchemy models
├── schemas.py          # Pydantic schemas
├── database.py         # Database configuration
├── init_db.py         # Database initialization
├── docker-compose.yml # Docker services configuration
├── Dockerfile         # FastAPI app container
├── Dockerfile.init    # Database initialization container
└── nginx.conf         # Nginx load balancer configuration
```

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
- `POSTGRES_USER`: Database user
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_DB`: Database name

## Docker Services

- `app1`, `app2`: FastAPI application instances
- `nginx`: Load balancer
- `db`: PostgreSQL database
- `db_init`: Database initialization

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

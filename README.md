# Django VPN Service 🌐🔒

This is a Django-based VPN service project that provides secure and anonymous browsing.

## Getting Started 🚀

Follow these steps to set up and run the project locally using Docker Compose.

### Prerequisites

- Docker
- Git

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kostomeister/py-vpn.git
    ```

2. Navigate to the project directory:

    ```bash
    cd py-vpn
    ```

3. Copy the environment file:

    ```bash
    cp .env.sample .env
    ```

    Edit the `.env` file and set the necessary values.
    - Ensure the `DEBUG` variable is set to `True`
    - Modify the `DATABASE_URL` to use the PostgreSQL database

4. Build and run with Docker Compose:

    ```bash
    docker-compose up --build
    ```

### Access the Application

Visit [http://localhost:8000](http://localhost:8000) in your web browser to access the Django VPN Service.

### Default User Credentials

You can log in as admin using the following default credentials:

- Username: admin1
- Password: 123321

### Loaded Data

The project comes with some pre-loaded data, including initial URLs for testing. Feel free to explore the VPN service features and manage URLs for secure browsing.

#### Note: The initial data includes pre-configured URLs for testing.

## Usage 🛠️

1. Register on the website.
2. Explore VPN service features.
3. Manage URLs for secure browsing.

## Running Tests 🧪

To run tests for the project, use the following command:

```bash
docker-compose run app python manage.py test
```

## Contributing 🤝

Feel free to contribute to the project by opening issues or submitting pull requests.

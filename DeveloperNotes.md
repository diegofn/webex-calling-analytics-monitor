
## Developer notes

### Logging and Console Output
* The application uses the LoggerManager class to manage logging and console output. This class provides methods for setting up the logger, thread-safe printing, logging and printing messages, and displaying data in a rich table format.
* Once 'call monitoring' has been initiated, a queue of Webex Calling Events will be logged to /app/logger/logs/app.log & displayed to the console, showing the call events that have been processed by the application.
* The LoggerManager class ensures that the application's logging and console output are well-organized, making it easier to track and debug call events and geolocation updates.
* The LoggerManager class also provides a rich table format for displaying data, making it easier to read and understand the application's output.


## Application Structure
The application is structured into several Python files and HTML templates:
- `app/`: Contains the main application code, including the FastAPI application and the Webex event handling logic.
- `main.py`: The main entry point of the application. It handles the routing and main logic of the application.
- `routes.py`: Contains the FastAPI routes for the application's API.
- `schemas.py`: Contains Pydantic models for data validation and serialization.
- `call_monitor.py`: Contains the logic for monitoring and processing call events using the Webex XSI events.
- `funcs.py`: Contains helper functions used throughout the application.
- `db.py`: Contains the SQLAlchemy engine and session configurations.
- `models.py`: Contains the SQLAlchemy ORM models for the application's database.
- `crud.py`: Contains the CRUD operations for the application's database.
- `logger/`: Contains the LoggerManager class for managing logging and console output.
- `templates/`: Contains the HTML templates for the application's frontend.
- `static/`: Contains the static files (e.g., CSS, JavaScript) for the application's frontend.
- `Dockerfile`: Contains the Docker configuration for building the application image.
- `docker-compose.yml`: Contains the Docker Compose configuration for running the application.
- `setup/`: Contains the setup script for configuring the environment variables.
- `config/`: Contains the configuration files for the application.
- `.env/`: Will need to be created in the config folder to store environment variables.
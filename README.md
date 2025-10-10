# Cisco Webex Calling XSI Analytics and Monitor
Python middleware for Webex Calling XSI interface to monitor and analyze the calls.

## Features
- Monitoring and managing call events in real-time using Webex XSI events
- OAuth for secure authentication and user identification
- Continuous geolocation updates / tracking using JavaScript - sends geolocation updates to the server every 30 seconds
- Dynamic call permission management based on geolocation data
- Blocking calls for users outside predefined geographical boundaries
- Secure session management and token refresh for continuous application use
- Database operations using SQLAlchemy for data storage and retrieval
- PostgreSQL database for storing user data, session tokens, and geolocation information

## User cases

### Block call by geo location.
First version for daemon that register the XSI Interface for the organization and check the Geolocation based on a webpage.



## Installation/Configuration

1. Clone this repository with `git clone https://github.com/diegofn/webex-calling-analytics-monitor`
2. Install the dependencies
```Shell
   sudo apt update
   sudo apt upgrade
   sudo apt install python3-pip
   sudo apt install libpq-dev
   sudo apt install python-is-python3
   sudo apt install postgresql postgresql-contrib
   sudo systemctl start postgresql.service
```

3. Create postgres user
```Shell
   sudo -i -u postgres
   createuser --interactive
   createdb webex
   psql
   alter user webex with encrypted password 'webex';
   grant all privileges on database webex to webex;
   exit
   sudo adduser webex
```

4. Install python requerimients
```Shell
pip install -r requirements.txt
```

5. Install uvicorn process
```Shell
python setup.py run
```

## Manually create and update the `.env` and update settings.py file:

To configure the application, you need to update the `.env` on the `app/config` folder with the appropriate values. 
This file contains key settings that the application uses to interact with the Webex APIs and to set up its environment.

1. **Webex Admin User ID**:
   - `WEBEX_ADMIN_UID`: The Webex admin user ID. This is used to fetch the Webex organization's details and used to verify the user's role in the organization after authentication.

2. **Client ID and Secret**:
   - `CLIENT_ID`: Your Webex Integration Client ID.
   - `CLIENT_SECRET`: Your Webex Integration Client Secret.

3. **Database Configuration**:
   - `SQLALCHEMY_DATABASE_URL`: The database URL for the application. The default is a PostgreSQL database, but you can replace it with a different database URL if needed.

### `.env` example
   ```script
   WEBEX_ADMIN_UID=YOUR_WEBEX_ADMIN_UID
   CLIENT_ID=YOUR_WEBEX_INTEGRATION_CLIENT_ID
   CLIENT_SECRET=YOUR_WEBEX_INTEGRATION_CLIENT_SECRET
   SQLALCHEMY_DATABASE_URL="postgresql://YOUR_USN:YOUR_PASSWORD@localhost/YOUR_DB_NAME"
   ```

## Manually Setting Up the `settings.py` File:
1. **Configure Geolocation Boundaries**: 
   - `LAT_MAX`: `LAT_MIN`, `LAT_MAX`, `LON_MIN`, `LON_MAX` are the latitude and longitude boundaries for the geofencing feature. Update these in settings.py as well.
2. **Geolocation Timeout**:
    - `GEOLOCATION_TIMEOUT`: The time interval (in seconds) for sending geolocation updates to the server. The default is 300 seconds.
3. **PUBLIC_URL**: 
   - `PUBLIC_URL`: The URL for the application for private or public environment, we suggest to have it on HTTPS

### `settings.py` example:
```script
# Required Environment Variables (app/config/.env file)
REQUIRED_ENV_VARS: List[str] = ['WEBEX_ADMIN_UID', 'CLIENT_ID', 'CLIENT_SECRET', 'SQLALCHEMY_DATABASE_URL']

# Required Settings
REQUIRED_SETTINGS: List[str] = ['LAT_MIN', 'LAT_MAX', 'LON_MIN', 'LON_MAX', 'GEOLOCATION_TIMEOUT']

# FastAPI Settings
APP_NAME: str = 'Webex Calling Analtyics and Monitoring'
APP_VERSION: str = 'POC v1.0'
UVICORN_LOG_LEVEL: str = 'WARNING'

# Webex Integration URLs
AUTHORIZATION_BASE_URL = 'https://api.ciscospark.com/v1/authorize'
TOKEN_URL = 'https://api.ciscospark.com/v1/access_token'
WEBEX_BASE_URL = 'https://webexapis.com/v1/'
SCOPE: List[str] =['spark:all', 'spark-admin:xsi', 'spark:xsi', 'spark-admin:locations_read', 'spark-admin:people_read', 'spark-admin:licenses_read']
PUBLIC_URL: str = 'http://127.0.0.1:8000'

# Geolocation bounding boxes &
LAT_MIN: float = 10.0
LAT_MAX: float = 20.0
LON_MIN: float = 100.0
LON_MAX: float = 30.1
GEOLOCATION_TIMEOUT: int = 20
```

## Usage
### Start the Application
To initiate the prototype, start the FastAPI application:
```
$ cd app
$ uvicorn main:app
$ uvicorn main:app --log-level warning
```



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

## Screenshots/GIFs
### Environment Variables & Settings Setup: <br>
![/IMAGES/setup.gif](/IMAGES/setup.gif)<br>

### PostgreSQL Setup:
![/IMAGES/psql_setup.gif](/IMAGES/psql_setup.gif)<br>

### Webex Calling Event Monitoring Setup:
![/IMAGES/call_monitor.gif](/IMAGES/call_monitor.gif)<br>

## Based on: gve_devnet_webex_xsi_call_block 
https://github.com/gve-sw/gve_devnet_webex_xsi_call_block
* Mark Orszycki
* Gerardo Chaves
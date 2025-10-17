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
   python -m venv .
   source bin/activate
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

4. **PUBLIC_URL**: 
   - `PUBLIC_URL`: The URL for the application for private or public environment, we suggest to have it on HTTPS


### `.env` example
   ```script
   WEBEX_ADMIN_UID=YOUR_WEBEX_ADMIN_UID
   CLIENT_ID=YOUR_WEBEX_INTEGRATION_CLIENT_ID
   CLIENT_SECRET=YOUR_WEBEX_INTEGRATION_CLIENT_SECRET
   SQLALCHEMY_DATABASE_URL="postgresql://YOUR_USN:YOUR_PASSWORD@localhost/YOUR_DB_NAME"
   PUBLIC_URL=https://subdomain.ngrok-free.app
   ```

## Manually Setting Up the `settings.py` File:
1. **Configure Geolocation Boundaries**: 
   - `LAT_MAX`: `LAT_MIN`, `LAT_MAX`, `LON_MIN`, `LON_MAX` are the latitude and longitude boundaries for the geofencing feature. Update these in settings.py as well.
2. **Geolocation Timeout**:
    - `GEOLOCATION_TIMEOUT`: The time interval (in seconds) for sending geolocation updates to the server. The default is 300 seconds.

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
AUTHORIZATION_BASE_URL = 'https://webexapis.com/v1/authorize'
TOKEN_URL = 'https://webexapis.com/v1/access_token'
WEBEX_BASE_URL = 'https://webexapis.com/v1/'
SCOPE: List[str] =['spark:all', 'spark-admin:xsi', 'spark:xsi', 'spark-admin:locations_read', 'spark-admin:people_read', 'spark-admin:licenses_read']

# Geolocation bounding boxes &
LAT_MIN: float = 10.0
LAT_MAX: float = 20.0
LON_MIN: float = 100.0
LON_MAX: float = 30.1
GEOLOCATION_TIMEOUT: int = 20
```

## Usage
### Start the Application
To initiate the App, start the FastAPI application:
```
   uvicorn main:app
   uvicorn main:app --log-level warning
```

## Screenshots/GIFs
### Environment Setup: <br>
![/images/setup.gif](/images/setup.gif)<br>

### Database Setup: <br>
![/images/database_setup.gif](/images/database_setup.gif)<br>

### Analyzer and monitoring setup <br>
![/images/app_setup.gif](/images/app_setup.gif)<br>

### Starting Call Monitoring <br>
![/images/call_monitor.gif](/images/call_monitor.gif)<br>

## Webex Calling XSI Documentation
https://developer.cisco.com/docs/webex-calling/developer-docs/

## Based on: gve_devnet_webex_xsi_call_block 
https://github.com/gve-sw/gve_devnet_webex_xsi_call_block
* Mark Orszycki
* Gerardo Chaves
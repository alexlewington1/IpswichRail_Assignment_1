# IpswichRail — Train Booking (Assignment 1)

A simple Django-based train booking demonstration web application built for the IpswichRail assignment. This project implements core booking pages, a train schedule model, and admin interfaces to manage available trains.

-- NOTE --
The HTML code of this was generated using ChatGPT and then modified by myself in order to better fit the project.

## Features
- Browse and filter available trains by departure station.
- Simple pages for Create Account, Login, Ticket Booking, and Ticket Search.
- Admin interface to manage train times.
- Uses SQLite (db.sqlite3) by default for quick setup and development.

## Project Structure
- `IpswichRail/` — Django project settings and root URLs.
- `TrainBooking/` — Django app containing models, views, URL routes, templates and admin registration.
- `TrainBooking/templates/` — Frontend HTML templates used by views.
- `db.sqlite3` — Default SQLite database (auto-generated).
- `requirements.txt` — Project Python dependencies.

Key models
- `TrainBooking/models.py` — Defines `TrainTime` which stores train schedule info (departure/arrival times and stations, duration, and price).

Key views and URLs
- `TrainBooking/views.py` — Contains simple view functions for the main pages and `available_trains`, which supports filtering by a station.
- `TrainBooking/urls.py` — Routes to the views (home, available trains, create account, login, ticket booking, ticket search).

## Getting Started (Development)
Prerequisites: Python 3.11+ recommended, virtual environment tool of your choice.

1. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Run database migrations
```
python manage.py migrate
```

4. Create a Django superuser (optional, for admin access)
```
python manage.py createsuperuser
```

5. Start the development server
```
python manage.py runserver
```
Open http://127.0.0.1:8000 in your browser.

6. Admin site
- Visit `/admin/` and sign in with the superuser to manage `TrainTime` entries.

## Sample data
Add `TrainTime` entries using the admin panel or via Django shell:
```
python manage.py shell
from TrainBooking.models import TrainTime
TrainTime.objects.create(departure_time='09:30', departure_station='Ipswich', arrival_time='11:15', arrival_station='London', duration='1h45', price=29.99)
```

## Tests
Run the Django test suite:
```
python manage.py test
```

## Notes
- This project is intended for demonstration and academic purposes — it is minimal and lacks production-ready features like authentication logic, input validation, and comprehensive error handling.
- The templates are located under `TrainBooking/templates/` and use Django template tags for static assets. Static files are expected to be managed for deployment (e.g., `collectstatic`) if serving in production.

## Contributing
This project is simple and used for learning. Please open issues or PRs with improvements.

## License
No explicit license provided. Contact the repository owner if you need licensing information.

# IpswichRail — Train Booking (Assignment 1)

A compact Django-based train booking demo used for the IpswichRail assignment. The project includes a small `TrainBooking` app with templates, views, and a `TrainTime` model to store schedule and pricing information.

## What changed / New code added
- New frontend templates and pages supporting booking flows and search:
	- `available_trains.html`, `ticketbook.html`, `ticketsearch.html`, `createaccount.html`, `login.html`, `bookingconfirmation.html`
- Routes and views added under `TrainBooking/urls.py` and `TrainBooking/views.py` to serve the pages and perform simple filtering of available trains.

-- NOTE -- The HTML code of this was generated using ChatGPT and then modified by myself in order to better fit the project.

Link to live site: https://ipswichrail-assignment-1-3.onrender.com/

## Features
- Browse and filter available trains by departure station.
- Pages for Create Account, Login, Ticket Booking, Ticket Search, and booking confirmation.
- Admin interface to create/manage `TrainTime` entries.
- Uses SQLite (`db.sqlite3`) by default for quick local development.

## Project layout (important files)
- `IpswichRail/` — Django project settings, root URL config.
- `TrainBooking/` — App code: models, views, URLs, templates, admin.
- `TrainBooking/templates/` — HTML templates listed above.
- `requirements.txt` — Python dependencies.

## Routes (available)
The app's routes (as defined in `TrainBooking/urls.py`) are:

- `/` → home/index page
- `/availabletrains/` → list and filter trains
- `/createaccount/` → signup page
- `/login/` → login page
- `/ticketbooking/` → book a ticket
- `/ticketsearch/` → search existing tickets
- `/bookingconfirmation/` → booking confirmation page

## Quick Start (development)
Prereqs: Python 3.11+ recommended, virtualenv or venv.

1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Apply migrations

```bash
python manage.py migrate
```

4. (Optional) Create a Django superuser to access the admin

```bash
python manage.py createsuperuser
```

5. Run the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.

Admin site is available at `/admin/` for managing `TrainTime` entries and other models.

## Adding sample data
Add `TrainTime` entries through the admin UI or the Django shell:

```bash
python manage.py shell
from TrainBooking.models import TrainTime
TrainTime.objects.create(departure_time='09:30', departure_station='Ipswich', arrival_time='11:15', arrival_station='London', duration='1h45', price=29.99)
exit()
```

## Tests
Run tests with:

```bash
python manage.py test
```

## Notes
- This project is a learning/demo app and is not production hardened (limited validation, auth, and error handling).
- For production deployments, configure static file serving, a production-ready DB, secure settings, and proper authentication.

## Contributing
Improvements and fixes are welcome — please open issues or pull requests.

## License
No license specified. Contact the repository owner for details.

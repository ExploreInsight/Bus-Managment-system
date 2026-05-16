# Bus Management System

A desktop GUI application for managing bus transportation operations — employees, fleet, routes, bookings, and payments.

Built with **Python + Tkinter + SQLite**.

## Features

- **Admin Login** — Secure authentication (default: `admin` / `admin`)
- **Employee Management** — Add, update, delete, search drivers and conductors (with photo upload)
- **Bus Fleet Management** — Track buses, seat inventory, purchase details
- **Route Management** — Define routes with locations and distance
- **Duty Allotment** — Assign buses and employees to routes with departure/reaching times
- **Customer Registration** — Passenger sign-up with duplicate detection
- **Seat Booking** — Per-seat selection with real-time availability
- **Payment Processing** — Auto-calculated fare (Rs.2 per km per seat)
- **Booking Cancellation** — Cancel bookings and restore seats
- **Status Views** — Tabular reports for employees, buses, routes, and route availability (JOIN query)

## Requirements

- **Python 3.10+** (with tkinter — included by default on Windows/macOS, install `python3-tk` on Linux)
- No database server required — uses SQLite (auto-created on first run)

## Quick Start

```bash
# 1. Clone
git clone https://github.com/ExploreInsight/Bus-Managment-system.git
cd Bus-Managment-system

# 2. Install dependencies
pip install Pillow tkcalendar

# 3. Run
python main.py
```

Default login: `admin` / `admin`

## Configuration

Database path can be customized via environment variable:

```bash
# Linux/macOS
export DB_PATH=/path/to/database.db

# Windows (PowerShell)
$env:DB_PATH = "C:\path\to\database.db"

# Or create a .env file (copy from .env.example)
cp .env.example .env
```

Default: `bus_management.db` (created in project root)

## Project Structure

```
Bus-Managment-system/
├── main.py              # Entry point
├── database.py          # SQLite connection and schema
├── requirements.txt     # Python dependencies
├── .env.example         # Environment config template
├── assests/             # UI images and backgrounds (32 files)
└── pages/               # Application screens (29 modules)
    ├── start.py         # Login screen
    ├── next.py          # Main dashboard
    ├── emp.py           # Employee registration
    ├── upd_emp.py       # Update employee
    ├── del_emp.py       # Delete employee
    ├── search_file.py   # Search employee
    ├── s_emp.py         # Employee status view
    ├── add_buses.py     # Add bus
    ├── update_buses.py  # Update bus
    ├── del_buses.py     # Delete bus
    ├── search_buses.py  # Search bus
    ├── s_bus.py         # Bus status view
    ├── addroutes.py     # Add route
    ├── update_routes.py # Update route
    ├── del_routes.py    # Delete route
    ├── search_routes.py # Search route
    ├── s_routes.py      # Route status view
    ├── route_allotment.py # Duty assignment
    ├── customer_reg.py  # Customer registration
    ├── customer.py      # Seat booking
    ├── payment.py       # Payment processing
    ├── cancel_payment.py # Cancel booking
    ├── inquiry.py       # Route availability
    └── ...
```

## Database Schema

9 tables auto-created on first run (SQLite):

| Table | Purpose |
|-------|---------|
| `admin` | Login credentials |
| `user` | Admin user management |
| `add_emp` | Employee records |
| `bus` | Bus fleet inventory |
| `routes` | Route definitions |
| `route_duty_allotment` | Bus + employee → route assignment |
| `customer` | Passenger records |
| `booking` | Seat bookings |
| `pay` | Payment records |

## Linux Note

If tkinter is not installed:
```bash
sudo apt install python3-tk
```

If pip install fails with "externally managed environment":
```bash
pip install --break-system-packages Pillow tkcalendar
# OR use a virtual environment
python3 -m venv venv && source venv/bin/activate && pip install Pillow tkcalendar
```

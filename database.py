import sqlite3
import os

DB_PATH = os.getenv("DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "bus_management.db"))


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS admin (
            username TEXT PRIMARY KEY,
            password TEXT
        );
        CREATE TABLE IF NOT EXISTS user (
            username TEXT PRIMARY KEY,
            password TEXT,
            full_name TEXT,
            email TEXT,
            date_of_registration TEXT,
            contact TEXT
        );
        CREATE TABLE IF NOT EXISTS add_emp (
            id_emp INTEGER PRIMARY KEY AUTOINCREMENT,
            name_emp TEXT,
            father_name TEXT,
            dob TEXT,
            email TEXT,
            gender TEXT,
            phone_no TEXT,
            desiganation TEXT,
            address TEXT,
            image TEXT
        );
        CREATE TABLE IF NOT EXISTS bus (
            bus_no TEXT PRIMARY KEY,
            bus_name TEXT,
            no_of_seats INTEGER,
            model_no TEXT,
            purchase_date TEXT,
            purchase_cost REAL,
            avail_seats TEXT
        );
        CREATE TABLE IF NOT EXISTS routes (
            route_no TEXT PRIMARY KEY,
            route_name TEXT,
            start TEXT,
            end TEXT,
            route_distance TEXT
        );
        CREATE TABLE IF NOT EXISTS route_duty_allotment (
            route_no TEXT,
            dep_time TEXT,
            reach_time TEXT,
            bus_no TEXT,
            id_emp TEXT
        );
        CREATE TABLE IF NOT EXISTS customer (
            login_name TEXT PRIMARY KEY,
            customer_name TEXT,
            phone_no TEXT,
            email TEXT,
            address TEXT
        );
        CREATE TABLE IF NOT EXISTS booking (
            login_name TEXT,
            route_name TEXT,
            start TEXT,
            end TEXT,
            seat_no TEXT,
            route_no TEXT,
            bus_no TEXT
        );
        CREATE TABLE IF NOT EXISTS pay (
            login_name TEXT,
            bus_no TEXT,
            start TEXT,
            end TEXT,
            dep_time TEXT,
            rech_time TEXT,
            total_charges TEXT,
            seat_no TEXT
        );
        INSERT OR IGNORE INTO admin (username, password) VALUES ('admin', 'admin');
    """)
    conn.commit()
    conn.close()

# lib/config.py
import sqlite3

CONN = sqlite3.connect('cars_database.db')
CURSOR = CONN.cursor()

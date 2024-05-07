import sqlite3

CONN = sqlite3.connect('./dealers.db')
CURSOR = CONN.cursor()
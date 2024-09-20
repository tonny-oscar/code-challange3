import sqlite3

# Reuse the database connection
conn = sqlite3.connect('concerts.db')
cur = conn.cursor()

class Venue:
    def __init__(self, venue_id):
        self.venue_id = venue_id

    def concerts(self):
        cur.execute('''
            SELECT * FROM concerts WHERE venue_id = ?
        ''', (self.venue_id,))
        return cur.fetchall()

    def bands(self):
        cur.execute('''
            SELECT DISTINCT bands.id, bands.name, bands.hometown
            FROM bands
            JOIN concerts ON concerts.band_id = bands.id
            WHERE concerts.venue_id = ?
        ''', (self.venue_id,))
        return cur.fetchall()

    def concert_on(self, date):
        cur.execute('''
            SELECT * FROM concerts
            WHERE venue_id = ? AND date = ?
            LIMIT 1
        ''', (self.venue_id, date))
        return cur.fetchone()

    def most_frequent_band(self):
        cur.execute('''
            SELECT bands.name, COUNT(concerts.id) AS performance_count
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.venue_id = ?
            GROUP BY bands.id
            ORDER BY performance_count DESC
            LIMIT 1
        ''', (self.venue_id,))
        return cur.fetchone()

from band import Band
from venue import Venue
from concert import Concert
import sqlite3

# Reuse the database connection
conn = sqlite3.connect('concerts.db')
cur = conn.cursor()

# Insert sample data
cur.execute("INSERT INTO bands (name, hometown) VALUES ('Band A', 'City A'), ('Band B', 'City B')")
cur.execute("INSERT INTO venues (title, city) VALUES ('Venue X', 'City A'), ('Venue Y', 'City B')")
cur.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-10-01'), (2, 2, '2024-10-02')")
conn.commit()

# Test Band methods
band = Band(1)
print("Band's concerts:", band.concerts())
print("Band's venues:", band.venues())
print("Band's introductions:", band.all_introductions())

# Test Venue methods
venue = Venue(1)
print("Venue's concerts:", venue.concerts())
print("Venue's bands:", venue.bands())

# Test Concert methods
concert = Concert(1)
print("Concert's band:", concert.band())
print("Concert's venue:", concert.venue())
print("Is hometown show?", concert.hometown_show())
print("Concert introduction:", concert.introduction())

conn.close()

#contains all your sql queries, and is imported into the last three files above.

'''
####      Changes      ####
songplay_id to SERIAL
user_d and start_time to NOT NULL
Deleted NOT NUll with Primary keys
deleted song_plays column within insert as now it is serial
On conflict solution placed
'''

# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplay_table_drop"
user_table_drop = "DROP TABLE IF EXISTS user_table_drop"
song_table_drop = "DROP TABLE IF EXISTS song_table_drop"
artist_table_drop = "DROP TABLE IF EXISTS artist_table_drop"
time_table_drop = "DROP TABLE IF EXISTS time_table_drop"

# CREATE TABLES
songplay_table_create = (""" 
                         create table if not exists songplays (
                         songplay_id SERIAL primary key,
                         start_time timestamp NOT NULL,
                         user_id varchar NOT NULL,
                         level varchar,
                         song_id varchar,
                         artist_id varchar,
                         session_id int,
                         location varchar,
                         user_agent varchar)
 """)

user_table_create = ("""
                        create table if not exists users (
                        user_id varchar primary key,
                        first_name varchar,
                        last_name varchar,
                        gender varchar,
                        level varchar
)

""")

song_table_create = ("""
                        create table if not exists songs (
                        song_id varchar primary key,
                        title varchar,
                        artist_id varchar,
                        year varchar,
                        duration float
                        )
""")

artist_table_create = ("""
                        create table if not exists artists (
                        artist_id varchar primary key,
                        name varchar,
                        location varchar,
                        latitude float,
                        longitude float)
                        """)

time_table_create = ("""
                        create table if not exists time (
                        start_time timestamp primary key,
                        hour int,
                        day int,
                        week int,
                        month int,
                        year int,
                        weekday int)
""")




# INSERT RECORDS
songplay_table_insert = ("""
                            INSERT INTO songplays (
                                 start_time,
                                 user_id,
                                 level,
                                 song_id,
                                 artist_id ,
                                 session_id ,
                                 location ,
                                 user_agent )
                                VALUES (%s, %s, %s, %s,%s,%s,%s,%s)
                                ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
                        INSERT INTO users (
                            user_id,
                            first_name,
                            last_name,
                            gender,
                            level)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT(user_id) DO UPDATE SET level = excluded.level
""")

song_table_insert = ("""
                        INSERT INTO songs (
                            song_id,
                            title,
                            artist_id,
                            year,
                            duration)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
                        INSERT into artists (
                            artist_id ,
                            name ,
                            location ,
                            latitude ,
                            longitude)
                            VALUES(%s,%s,%s,%s,%s)
                            ON CONFLICT DO NOTHING
""")

time_table_insert = ("""
                        INSERT into time(
                            start_time ,
                            hour ,
                            day ,
                            week ,
                            month ,
                            year ,
                            weekday )
                            VALUES (%s,%s,%s,%s,%s,%s,%s)
                            ON CONFLICT DO NOTHING
""")

# FIND SONGS
song_select = ("""
                    SELECT songs.song_id, artists.artist_id
                                       FROM songs 
                                       JOIN artists 
                                       ON songs.artist_id = artists.artist_id
                                       WHERE songs.title = %s 
                                       AND artists.name = %s             
                                       AND songs.duration = %s
""")



# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
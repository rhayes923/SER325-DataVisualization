import pymysql as ps

# name db = movies-on-streaming-platforms
# user_name = admin
# password: admin123

# make the connection to the db
def make_connection():
    return ps.connect(host='movies-on-streaming-platforms.ciwwpovuascr.us-east-1.rds.amazonaws.com', user='admin',
        passwd='zSFC60g3wza4wp9tw6*$rsrp!4GM8!',
            port=3306, autocommit=True)
                      
def setup_db(cur):
  # Set up db
    cur.execute('DROP DATABASE IF EXISTS movies_availableDB');
    cur.execute('CREATE DATABASE movies_availableDB');
    cur.execute('USE movies_availableDB');

    # Drop Existing Tables
    cur.execute('DROP TABLE IF EXISTS Movie_Language');
    cur.execute('DROP TABLE IF EXISTS Movie_Director');
    cur.execute('DROP TABLE IF EXISTS Movie_Genre');
    cur.execute('DROP TABLE IF EXISTS Movie_Country');
    cur.execute('DROP TABLE IF EXISTS Movie');
    cur.execute('DROP TABLE IF EXISTS Director');
    cur.execute('DROP TABLE IF EXISTS Language');
    cur.execute('DROP TABLE IF EXISTS Genre');
    cur.execute('DROP TABLE IF EXISTS Country');

    # Create Tables
    cur.execute(
        '''CREATE TABLE Movie(
        title VARCHAR(30) NOT NULL PRIMARY KEY,
        year INT,
        age VARCHAR(10),
        runtime INT,
        imdbReview FLOAT,
        rottenTomatoesReview INT,
        onNetflix BOOLEAN,
        onHulu BOOLEAN,
        onPrime BOOLEAN,
        onDisney BOOLEAN
        );''')
    cur.execute(
        '''CREATE TABLE Director (
        lastname VARCHAR(20) NOT NULL PRIMARY KEY,
        firstname VARCHAR(20)
        );''')
    cur.execute(
        '''CREATE TABLE Language (
        language VARCHAR(20) PRIMARY KEY
        );''')
    cur.execute(
        '''CREATE TABLE Genre (
        genre VARCHAR(20) PRIMARY KEY
        );''')
    cur.execute(
        '''CREATE TABLE Country (
        country VARCHAR(20) PRIMARY KEY
        );''')
    # Create Join Tables
    cur.execute(
        '''CREATE TABLE Movie_Language (
        title VARCHAR(30) NOT NULL,
        language VARCHAR(30) NOT NULL,
        FOREIGN KEY(title) REFERENCES Movie(title),
        FOREIGN KEY(language) REFERENCES Language(language)
        );''')
    cur.execute(
        '''CREATE TABLE Movie_Director (
        title VARCHAR(30) NOT NULL,
        lastname VARCHAR(20) NOT NULL,
        FOREIGN KEY(title) REFERENCES Movie(title),
        FOREIGN KEY(lastname) REFERENCES Director(lastname)
        );''')
    cur.execute(
        '''CREATE TABLE Movie_Genre (
        title VARCHAR(30) NOT NULL,
        genre VARCHAR(30) NOT NULL,
        FOREIGN KEY(title) REFERENCES Movie(title),
        FOREIGN KEY(genre) REFERENCES Genre(genre)
        );''')
    cur.execute(
        '''CREATE TABLE Movie_Country (
        title VARCHAR(30) NOT NULL,
        country VARCHAR(30) NOT NULL,
        FOREIGN KEY(title) REFERENCES Movie(title),
        FOREIGN KEY(country) REFERENCES Country(country)
        );''')      


def insert_data(cur):
            # Insertions for Movie table
        with open("data/MoviesOnStreamingPlatforms_movies.csv", 'r', encoding="utf-8") as r1:
            print("Starting Movies...")
            # skips first line the headers
            next(r1)
            for line in r1:
                line = line.split(',')
                title = line.__getitem__(2).encode("utf-8").strip()
                year = line.__getitem__(3).encode("utf-8").strip()
                age = line.__getitem__(4).encode("utf-8").strip()
                imdbReview = line.__getitem__(5).encode("utf-8").strip()
                rottenTomatoesReview = line.__getitem__(6).encode("utf-8").strip()
                onNetflix = bool(int(line.__getitem__(7)))
                onHulu = bool(int(line.__getitem__(8)))
                onPrime = bool(int(line.__getitem__(9)))
                onDisney = bool(int(line.__getitem__(10)))
                runtime = line.__getitem__(12).encode("utf-8").strip()
                #print(title, year, age, runtime, imdbReview, rottenTomatoesReview, onNetflix, onHulu, onPrime, onDisney)
                cur.execute(
                    'INSERT IGNORE INTO Movie(title, year, age, runtime, imdbReview, rottenTomatoesReview, onNetflix, onHulu, onPrime, onDisney) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (title, year, age, runtime, imdbReview, rottenTomatoesReview, onNetflix, onHulu, onPrime, onDisney))
            print("Finished Movies.")
            
        #Insertions for Director table
        with open("data/MoviesOnStreamingPlatforms_directors.csv", 'r', encoding="unicode_escape") as r1:
            print("Starting Director...")
            # skips first line the headers
            next(r1)
            for line in r1:
                dArr = line.split(",")
                directors = dArr[1:]
                title = dArr[0]
                for director in directors:
                    names = director.split(" ")
                    lastname = names[-1].replace("\"","")
                    firstname = names[0].replace("\"","")
                    cur.execute('INSERT IGNORE INTO Director(lastname, firstname) VALUES (%s, %s)', (lastname, firstname))
            print("Finished Director.")

            #Insertions for Movie-Director table
        with open("data/MoviesOnStreamingPlatforms_directors.csv", 'r', encoding="unicode_escape") as r1:
            print("Starting Movies_Director...")
            # skips first line the headers
            next(r1)
            for line in r1:
                dArr = line.split(",")
                directors = dArr[1:]
                title = dArr[0]
                for director in directors:
                    names = director.split(" ")
                    lastname = names[-1].replace("\"","")
                    cur.execute('INSERT IGNORE INTO Movie_Director(title, lastname) VALUES (%s, %s)', (title, lastname))
            print("Finished Movies_Director.")

        #Insertions for Genre table
        with open("data/MoviesOnStreamingPlatforms_genres.csv", 'r', encoding="unicode_escape") as r1:
            print("Starting Genre...")
            # skips first line the headers
            next(r1)
            for line in r1:
                line = line.split(',')
                for i in range(1, len(line)):
                    genre = line.__getitem__(i).replace("\"","").strip()
                    cur.execute('INSERT IGNORE INTO Genre(genre) VALUES (%s)', (genre))
            print("Finished Genre.")

            #Insertions for Movie-Genre table
        with open("data/MoviesOnStreamingPlatforms_genres.csv", 'r', encoding="unicode_escape") as r1:
            print("Starting Movie_Genre...")
            # skips first line the headers
            next(r1)
            for line in r1:
                line = line.split(',')
                title = line.__getitem__(0)
                for i in range(1, len(line)):
                    genre = line.__getitem__(i).replace("\"","").strip()
                    cur.execute('INSERT IGNORE INTO Movie_Genre(title, genre) VALUES (%s, %s)', (title, genre))
            print("Finished Movie_Genre.")
        

            #Insertions for Language table
        with open("data/MoviesOnStreamingPlatforms_languages.csv", 'r', encoding="unicode_escape") as r1:
            print("Starting Language...")
            # skips first line the headers
            next(r1)
            for line in r1:
                line = line.split(',')
                for i in range(1, len(line)):
                    language = line.__getitem__(i).replace("\"","").strip()
                    cur.execute('INSERT IGNORE INTO Language(language) VALUES (%s)', (language))
            print("Finished Language.")

            #Insertions for Movie-Language table
        with open("data/MoviesOnStreamingPlatforms_languages.csv", 'r', encoding="unicode_escape") as r1:
            print("Starting Movie-Language...")
            # skips first line the headers
            next(r1)
            for line in r1:
                line = line.split(',')
                title = line.__getitem__(0)
                for i in range(1, len(line)):
                    language = line.__getitem__(i).replace("\"","").strip()
                    cur.execute('INSERT IGNORE INTO Movie_Language(title, language) VALUES (%s, %s)', (title, language))
            print("Finished Movies_Language.")                
            

            #Insertions for Country table
        with open("data/MoviesOnStreamingPlatforms_countries.csv", 'r', encoding="unicode_escape") as r1:
            print("Starting Country...")
            # skips first line the headers
            next(r1)
            for line in r1:
                line = line.split(',')
                for i in range(1, len(line)):
                    country = line.__getitem__(i).replace("\"","").strip()
                    cur.execute('INSERT IGNORE INTO Country(country) VALUES (%s)', (country))
            print("Finished Country.")
            
            #Insertions for Movie-Country table
        with open("data/MoviesOnStreamingPlatforms_countries.csv", 'r', encoding="unicode_escape") as r1:
            print("Starting Movie-Country...")
            # skips first line the headers
            next(r1)
            for line in r1:
                line = line.split(',')
                title = line.__getitem__(0)
                for i in range(1, len(line)):
                    country = line.__getitem__(i).replace("\"","").strip()
                    cur.execute('INSERT IGNORE INTO Movie_Country(title, country) VALUES (%s, %s)', (title, country))
            print("Finished Movies_Country.") 
    
cnx = make_connection()
cur = cnx.cursor()
print("Starting Setup...")
setup_db(cur)
print("Finished Setup.")
print("Starting Insert...")
insert_data(cur)
print("Finished Insert.")
cur.close()
cnx.commit()
cnx.close()
print("FINISHED")

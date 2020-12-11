import pymysql as ps
import matplotlib.pyplot as plt
import matplotlib.widgets as w

# Make Connection to the DB
def make_connection():
    return ps.connect(host='movies-on-streaming-platforms.ciwwpovuascr.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='zSFC60g3wza4wp9tw6*$rsrp!4GM8!',
                      port=3306, autocommit=True)

conn = make_connection()
cur = conn.cursor()
cur.execute('USE movies_availableDB')

# Create figure
fig = plt.figure(figsize=(15, 7.5))
fig.canvas.set_window_title("Movies on Streaming Platforms")
fig.subplots_adjust(hspace=0.75, wspace=0.35)

#Create First Subplot
plt.subplot(2, 3, 1)

cur.execute('SELECT year, COUNT(year) FROM Movie WHERE onNetflix = "1" GROUP BY year HAVING COUNT(year) ORDER BY year')
rows = cur.fetchall()
x = []
y = []
i = 0
for row in rows:
    x.append(rows[i][0])
    y.append(rows[i][1])
    i += 1
plt.plot(x, y, label="Netflix")

cur.execute('SELECT year, COUNT(year) FROM Movie WHERE onHulu = "1" GROUP BY year HAVING COUNT(year) ORDER BY year')
rows = cur.fetchall()
x = []
y = []
i = 0
for row in rows:
    x.append(rows[i][0])
    y.append(rows[i][1])
    i += 1
plt.plot(x, y, label="Hulu")

cur.execute('SELECT year, COUNT(year) FROM Movie WHERE onPrime = "1" GROUP BY year HAVING COUNT(year) ORDER BY year')
rows = cur.fetchall()
x = []
y = []
i = 0
for row in rows:
    x.append(rows[i][0])
    y.append(rows[i][1])
    i += 1
plt.plot(x, y, label="Amazon Prime")

cur.execute('SELECT year, COUNT(year) FROM Movie WHERE onDisney = "1" GROUP BY year HAVING COUNT(year) ORDER BY year')
rows = cur.fetchall()
x = []
y = []
i = 0
for row in rows:
    x.append(rows[i][0])
    y.append(rows[i][1])
    i += 1
plt.plot(x, y, label="Disney+")

plt.title('Yearly Production of Movies By Streaming Platforms')
plt.xlabel("Year produced")
plt.ylabel("Number of Movies Made")
plt.xlim(1930, 2020)
plt.legend()
plt.grid(True, color='#f1f1f1')

# Create Second Subplot
plt.subplot(2, 3, 2)
cur.execute('SELECT G.genre, AVG(M.rottenTomatoesReview + M.imdbReview) FROM Genre G, Movie_Genre MG, Movie M WHERE G.genre = MG.genre AND MG.title = M.title AND M.rottenTomatoesReview != 0 AND M.imdbReview != 0 AND G.genre != "" GROUP BY G.genre HAVING AVG(M.rottenTomatoesReview + M.imdbReview) ORDER BY G.genre')
rows = cur.fetchall()
x = []
y = []
i = 0
for row in rows:
    x.append(rows[i][0])
    y.append(rows[i][1])
    i += 1
plt.scatter(x, y)
plt.title('Movie Quality Based Upon Genre')
plt.xlabel("Genre")
plt.xticks(x, rotation='vertical')
plt.ylabel("Movie Quality")
plt.grid(True, color='#f1f1f1')

# Create Third Subplot
plt.subplot(2, 3, 3)
cur.execute('SELECT D.lastname, AVG(M.rottenTomatoesReview + M.imdbReview) FROM Director D, Movie_Director MD, Movie M WHERE D.lastname = MD.lastname AND MD.title = M.title AND M.rottenTomatoesReview != 0 AND M.imdbReview != 0 GROUP BY D.lastname HAVING AVG(M.rottenTomatoesReview + M.imdbReview) ORDER BY D.lastname')
rows = cur.fetchall()
x = []
y = []
i = 0
for row in rows:
    x.append(rows[i][0])
    y.append(rows[i][1])
    i += 1
plt.scatter(x, y)
plt.title('Movie Quality Based Upon Director')
plt.xlabel("Director")
plt.xticks(x, rotation='vertical')
plt.locator_params(axis = 'x', nbins = 10)
plt.ylabel("Movie Quality")
plt.grid(True, color='#f1f1f1')

# Create Fourth Subplot
plt.subplot(2, 3, 4)
xPlatform = []
yPlatform = []
plt.barh(xPlatform, yPlatform, height=0.25)
plt.title("Movies on Streaming Platforms")
plt.ylabel("Streaming Platforms")
plt.xlim(0, 1)
plt.xticks(range(0, 2), ["", ""])
plt.yticks(range(0, 4), ["Netflix", "Hulu", "Amazon Prime", "Disney+"])

# Updates available movie platforms based on user input in the text box
def titleUpdate(text):
    global conn
    global cur
    conn = make_connection()
    cur = conn.cursor()
    plt.subplot(2, 3, 4).cla()
    cur.execute('USE movies_availableDB')
    query = 'SELECT onNetflix, onHulu, onPrime, onDisney FROM Movie WHERE title = '
    query = query + "'" + text + "'"
    cur.execute(query)
    rows = cur.fetchall()
    xPlatform = [0, 1, 2, 3]
    yPlatform = [rows[0][0], rows[0][1], rows[0][2], rows[0][3]]
    barlist = plt.barh(xPlatform, yPlatform, height=0.25)
    barlist[0].set_color('r')
    barlist[1].set_color('g')
    barlist[2].set_color('purple')
    barlist[3].set_color('b')
    plt.title("Movies on Streaming Platforms")
    plt.ylabel("Streaming Platforms")
    plt.xlim(0, 1)
    plt.xticks(range(0, 2), ["", ""])
    plt.yticks(range(0, 4), ["Netflix", "Hulu", "Amazon Prime", "Disney+"])
    plt.draw()
    conn.close()

# Creates the textbox
axbox = plt.axes([0.195, 0.05, 0.15, 0.025])
movie_title = w.TextBox(axbox, "Search Movie Title", initial="")
movie_title.on_submit(titleUpdate)

# Create Fifth Subplot
plt.subplot(2, 3, 5)
xTitle = []
yTitle = []
currentImdbVal = 0
currentRtVal = 0
annotate = ""
plt.scatter(xTitle, yTitle)
plt.title("Movies by Rating")
plt.xlabel("IMDb Rating")
plt.ylabel("Rotten Tomatoes Rating")
plt.xlim(0, 10)
plt.ylim(0, 100)

# Updates results based on change in imdbSlider
def imdbRatingUpdate(val):
    global currentImdbVal
    global conn
    global cur
    conn = make_connection()
    cur = conn.cursor()
    cur.execute('USE movies_availableDB')
    currentImdbVal = val
    plt.subplot(2, 3, 5).cla()
    query = 'SELECT title, imdbReview, rottenTomatoesReview FROM Movie WHERE imdbReview > '
    query = query + str(currentImdbVal) + ' AND rottenTomatoesReview > '
    query = query + "'" + str(currentRtVal) + "'"
    cur.execute(query)
    rows = cur.fetchall()
    xTitle = []
    yTitle = []
    i = 0
    for row in rows:
        xTitle.append(rows[i][1])
        yTitle.append(rows[i][2])
        i += 1
    plt.scatter(xTitle, yTitle)
    plt.title("Movies by Rating")
    plt.xlabel("IMDb Rating")
    plt.ylabel("Rotten Tomatoes Rating")
    plt.draw()
    conn.close()

# Updates results based on change in rtSlider
def rtRatingUpdate(val):
    global currentRtVal
    global conn
    global cur
    conn = make_connection()
    cur = conn.cursor()
    cur.execute('USE movies_availableDB')
    currentRtVal = val
    plt.subplot(2, 3, 5).cla()
    query = 'SELECT title, imdbReview, rottenTomatoesReview FROM Movie WHERE imdbReview > '
    query = query + str(currentImdbVal) + ' AND rottenTomatoesReview > '
    query = query + "'" + str(currentRtVal) + "'"
    cur.execute(query)
    rows = cur.fetchall()
    xTitle = []
    yTitle = []
    i = 0
    for row in rows:
        xTitle.append(rows[i][1])
        yTitle.append(rows[i][2])
        i += 1
    plt.scatter(xTitle, yTitle)
    plt.title("Movies by Rating")
    plt.xlabel("IMDb Rating")
    plt.ylabel("Rotten Tomatoes Rating")
    plt.draw()
    conn.close()

# Creates the Imdb and RT sliders
axIMDb = plt.axes([0.465, 0.030, 0.15, 0.015])
axRT = plt.axes([0.465, 0.0035, 0.15, 0.015])
imdbSlider = w.Slider(axIMDb, "IMDb Rating", 0, 10, 0)
rtSlider = w.Slider(axRT, "RT Rating", 0, 100, 0)
imdbSlider.on_changed(imdbRatingUpdate)
rtSlider.on_changed(rtRatingUpdate)

# Finalize figure and close DB connection
plt.suptitle("Movies on Streaming Platforms")
plt.show()
cur.close()
conn.close()

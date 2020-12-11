SELECT year, COUNT(year)
FROM Movie
WHERE onNetflix = '1'
GROUP BY year
HAVING COUNT(year)
ORDER BY year;

SELECT G.genre, AVG(M.rottenTomatoesReview + M.imdbReview)
FROM Genre G, Movie_Genre MG, Movie M
WHERE G.genre = MG.genre
AND MG.title = M.title
AND M.rottenTomatoesReview != 0
AND M.imdbReview != 0
AND G.genre != ""
GROUP BY G.genre
HAVING AVG(M.rottenTomatoesReview + M.imdbReview)
ORDER BY genre;

SELECT D.lastname, AVG(M.rottenTomatoesReview + M.imdbReview)
FROM Director D, Movie_Director MD, Movie M
WHERE D.lastname = MD.lastname
AND MD.title = M.title
AND M.rottenTomatoesReview != 0
AND M.imdbReview != 0
GROUP BY D.lastname
HAVING AVG(M.rottenTomatoesReview + M.imdbReview)
ORDER BY D.lastname;

SELECT onNetflix, onHulu, onPrime, onDisney 
FROM Movie 
WHERE title = " ";

SELECT title, imdbReview, rottenTomatoesReview
FROM Movie
WHERE imdbReview > 5
AND rottenTomatoesReview > 50;

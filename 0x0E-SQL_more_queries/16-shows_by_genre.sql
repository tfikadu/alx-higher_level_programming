-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT a.title, c.name
FROM tv_shows a
LEFT JOIN tv_show_genres b
ON a.id = b.show_id
LEFT JOIN tv_genres c
ON b.genre_id = c.id
ORDER BY a.title ASC, c.name ASC;

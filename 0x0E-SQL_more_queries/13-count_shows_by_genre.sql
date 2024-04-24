--  a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- join always come after FROM directly and before group by
SELECT tv_genres.name AS genre, COUNT(tv_genres.name) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY (tv_genres.name)
ORDER BY number_of_shows DESC;

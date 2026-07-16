# LeetCode 1341 - Movie Rating

QUERY = """
(SELECT u.name AS results
 FROM MovieRating r JOIN Users u USING (user_id)
 GROUP BY u.user_id, u.name
 ORDER BY COUNT(*) DESC, u.name
 LIMIT 1)
UNION ALL
(SELECT m.title AS results
 FROM MovieRating r JOIN Movies m USING (movie_id)
 WHERE r.created_at >= '2020-02-01' AND r.created_at < '2020-03-01'
 GROUP BY m.movie_id, m.title
 ORDER BY AVG(r.rating) DESC, m.title
 LIMIT 1)
"""

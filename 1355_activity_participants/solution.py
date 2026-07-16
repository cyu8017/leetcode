QUERY = """
SELECT activity
FROM Friends
GROUP BY activity
HAVING COUNT(*) NOT IN (
    SELECT MIN(cnt) FROM (SELECT COUNT(*) cnt FROM Friends GROUP BY activity) x
)
AND COUNT(*) NOT IN (
    SELECT MAX(cnt) FROM (SELECT COUNT(*) cnt FROM Friends GROUP BY activity) y
)
"""

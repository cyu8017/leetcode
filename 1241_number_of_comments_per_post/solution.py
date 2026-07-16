QUERY = """
SELECT s.sub_id AS post_id, COUNT(DISTINCT c.sub_id) AS number_of_comments
FROM Submissions s
LEFT JOIN Submissions c ON c.parent_id = s.sub_id
WHERE s.parent_id IS NULL
GROUP BY s.sub_id
ORDER BY s.sub_id
"""

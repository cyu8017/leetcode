# LeetCode 1308 - Running Total For Different Genders

QUERY = """
SELECT gender, day,
       SUM(score_points) OVER (PARTITION BY gender ORDER BY day) AS total
FROM Scores
ORDER BY gender, day
"""

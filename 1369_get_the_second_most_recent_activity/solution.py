QUERY = """
SELECT username, activity, startDate, endDate
FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY username ORDER BY startDate DESC) rn,
            COUNT(*) OVER (PARTITION BY username) cnt
  FROM UserActivity
) x
WHERE rn = CASE WHEN cnt = 1 THEN 1 ELSE 2 END
"""

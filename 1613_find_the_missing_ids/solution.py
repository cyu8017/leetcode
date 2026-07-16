QUERY = """
WITH RECURSIVE ids AS (
  SELECT 1 AS ids
  UNION ALL
  SELECT ids + 1 FROM ids WHERE ids < (SELECT MAX(customer_id) FROM Customers)
)
SELECT ids
FROM ids
WHERE ids NOT IN (SELECT customer_id FROM Customers)
ORDER BY ids;
"""

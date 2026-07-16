QUERY = """WITH ranked AS (
  SELECT customer_id, product_id, COUNT(*) AS cnt,
         DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(*) DESC) AS rk
  FROM Orders GROUP BY customer_id, product_id
)
SELECT r.customer_id, r.product_id, p.product_name
FROM ranked r JOIN Products p ON p.product_id = r.product_id
WHERE r.rk = 1\n"""

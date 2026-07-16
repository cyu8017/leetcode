QUERY = """
SELECT customer_id, customer_name
FROM Customers
GROUP BY customer_id, customer_name
HAVING SUM(product_name = 'A') > 0
   AND SUM(product_name = 'B') > 0
   AND SUM(product_name = 'C') = 0
"""

QUERY = """
SELECT seller_name
FROM Seller
WHERE seller_id NOT IN (
    SELECT seller_id FROM Orders
    WHERE sale_date BETWEEN '2020-01-01' AND '2020-12-31'
)
ORDER BY seller_name;
"""

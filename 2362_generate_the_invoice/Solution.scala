// LeetCode 2362 - Generate the Invoice
// https:// leetcode.com/problems/generate-the-invoice/

object Solution {
  final val QUERY: String = """WITH P AS (
    SELECT *
    FROM Purchases
    JOIN Products USING (product_id)
),
T AS (
    SELECT invoice_id, SUM(price * quantity) AS amount
    FROM P
    GROUP BY invoice_id
    ORDER BY amount DESC, invoice_id
    LIMIT 1
)
SELECT product_id, quantity, (quantity * price) AS price
FROM P
JOIN T USING (invoice_id)
ORDER BY product_id
"""
}

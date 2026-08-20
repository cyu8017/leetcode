// LeetCode 1565 - Unique Orders and Customers Per Month
// https://leetcode.com/problems/unique-orders-and-customers-per-month/

const QUERY = `
SELECT strftime('%Y-%m', order_date) AS month,
       COUNT(*) AS order_count, COUNT(DISTINCT customer_id) AS customer_count
FROM Orders
WHERE invoice > 20
GROUP BY strftime('%Y-%m', order_date)
ORDER BY month\n
`

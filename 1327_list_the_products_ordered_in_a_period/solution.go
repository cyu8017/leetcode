// LeetCode 1327 - List The Products Ordered In A Period
// https://leetcode.com/problems/list-the-products-ordered-in-a-period/

const QUERY = `
SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p
JOIN Orders o USING (product_id)
WHERE o.order_date >= '2020-02-01' AND o.order_date < '2020-03-01'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100
`

// LeetCode 1571 - Warehouse Manager
// https://leetcode.com/problems/warehouse-manager/

let QUERY = """
SELECT w.name AS warehouse_name,
       SUM(w.units * p.Width * p.Length * p.Height) AS volume
FROM Warehouse w JOIN Products p ON p.product_id = w.product_id
GROUP BY w.name\n
"""

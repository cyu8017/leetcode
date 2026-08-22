// LeetCode 1571 - Warehouse Manager
// https://leetcode.com/problems/warehouse-manager/

const char* QUERY =
    "\n"
    "SELECT w.name AS warehouse_name,\n"
    "       SUM(w.units * p.Width * p.Length * p.Height) AS volume\n"
    "FROM Warehouse w JOIN Products p ON p.product_id = w.product_id\n"
    "GROUP BY w.name\\n\n";

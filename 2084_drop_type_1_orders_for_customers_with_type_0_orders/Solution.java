// LeetCode 2084 - Drop Type 1 Orders for Customers With Type 0 Orders
// https://leetcode.com/problems/drop-type-1-orders-for-customers-with-type-0-orders/

class Solution {
    public static final String QUERY = """
WITH
    T AS (
        SELECT DISTINCT customer_id
        FROM Orders
        WHERE order_type = 0
    )
SELECT *
FROM Orders AS o
WHERE order_type = 0 OR NOT EXISTS (SELECT 1 FROM T AS t WHERE t.customer_id = o.customer_id)
""";
}

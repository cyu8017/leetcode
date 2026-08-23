// LeetCode 2686 - Immediate Food Delivery III
// https://leetcode.com/problems/immediate-food-delivery-iii/

class Solution {
    public static final String QUERY = """
SELECT
    order_date,
    ROUND(
        100 * SUM(IF(customer_pref_delivery_date = order_date, 1, 0)) / COUNT(*),
        2
    ) AS immediate_percentage
FROM Delivery
GROUP BY order_date
ORDER BY order_date
""";
}

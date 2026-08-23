// LeetCode 1173 - Immediate Food Delivery I
// https://leetcode.com/problems/immediate-food-delivery-i/

const char* QUERY = R"SQL(
SELECT ROUND(
    100.0 * SUM(order_date = customer_pref_delivery_date) / COUNT(*),
    2
) AS immediate_percentage
FROM Delivery
)SQL";

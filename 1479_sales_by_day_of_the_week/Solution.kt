// LeetCode 1479 - Sales By Day Of The Week
// https://leetcode.com/problems/sales-by-day-of-the-week/

class Solution {
    companion object {
        const val QUERY = "SELECT item_category AS CATEGORY,\n" +
            "       SUM(CASE WHEN DAYOFWEEK(order_date)=2 THEN quantity ELSE 0 END) AS MONDAY,\n" +
            "       SUM(CASE WHEN DAYOFWEEK(order_date)=3 THEN quantity ELSE 0 END) AS TUESDAY,\n" +
            "       SUM(CASE WHEN DAYOFWEEK(order_date)=4 THEN quantity ELSE 0 END) AS WEDNESDAY,\n" +
            "       SUM(CASE WHEN DAYOFWEEK(order_date)=5 THEN quantity ELSE 0 END) AS THURSDAY,\n" +
            "       SUM(CASE WHEN DAYOFWEEK(order_date)=6 THEN quantity ELSE 0 END) AS FRIDAY,\n" +
            "       SUM(CASE WHEN DAYOFWEEK(order_date)=7 THEN quantity ELSE 0 END) AS SATURDAY,\n" +
            "       SUM(CASE WHEN DAYOFWEEK(order_date)=1 THEN quantity ELSE 0 END) AS SUNDAY\n" +
            "FROM Items i LEFT JOIN Orders o ON i.item_id=o.item_id\n" +
            "GROUP BY item_category ORDER BY item_category"
    }
}

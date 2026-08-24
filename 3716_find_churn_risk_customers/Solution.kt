// LeetCode 3716 - Find Churn Risk Customers
// https://leetcode.com/problems/find-churn-risk-customers/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    user_with_last_event AS (\n" +
            "        SELECT\n" +
            "            s.*,\n" +
            "            ROW_NUMBER() OVER (\n" +
            "                PARTITION BY user_id\n" +
            "                ORDER BY event_date DESC, event_id DESC\n" +
            "            ) AS rn\n" +
            "        FROM subscription_events s\n" +
            "    ),\n" +
            "    user_history AS (\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            MIN(event_date) AS start_date,\n" +
            "            MAX(event_date) AS last_event_date,\n" +
            "            MAX(monthly_amount) AS max_historical_amount,\n" +
            "            SUM(\n" +
            "                CASE\n" +
            "                    WHEN event_type = 'downgrade' THEN 1\n" +
            "                    ELSE 0\n" +
            "                END\n" +
            "            ) AS downgrade_count\n" +
            "        FROM subscription_events\n" +
            "        GROUP BY user_id\n" +
            "    ),\n" +
            "    latest_event AS (\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            event_type AS last_event_type,\n" +
            "            plan_name AS current_plan,\n" +
            "            monthly_amount AS current_monthly_amount\n" +
            "        FROM user_with_last_event\n" +
            "        WHERE rn = 1\n" +
            "    )\n" +
            "SELECT\n" +
            "    l.user_id,\n" +
            "    l.current_plan,\n" +
            "    l.current_monthly_amount,\n" +
            "    h.max_historical_amount,\n" +
            "    DATEDIFF(h.last_event_date, h.start_date) AS days_as_subscriber\n" +
            "FROM\n" +
            "    latest_event l\n" +
            "    JOIN user_history h ON l.user_id = h.user_id\n" +
            "WHERE\n" +
            "    l.last_event_type <> 'cancel'\n" +
            "    AND h.downgrade_count >= 1\n" +
            "    AND l.current_monthly_amount < 0.5 * h.max_historical_amount\n" +
            "    AND DATEDIFF(h.last_event_date, h.start_date) >= 60\n" +
            "ORDER BY days_as_subscriber DESC, l.user_id ASC;"
    }
}

// LeetCode 3601 - Find Drivers With Improved Fuel Efficiency
// https://leetcode.com/problems/find-drivers-with-improved-fuel-efficiency/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            driver_id,\n" +
            "            AVG(distance_km / fuel_consumed) half_avg,\n" +
            "            CASE\n" +
            "                WHEN MONTH(trip_date) <= 6 THEN 1\n" +
            "                ELSE 2\n" +
            "            END half\n" +
            "        FROM trips\n" +
            "        GROUP BY driver_id, half\n" +
            "    )\n" +
            "SELECT\n" +
            "    t1.driver_id,\n" +
            "    d.driver_name,\n" +
            "    ROUND(t1.half_avg, 2) first_half_avg,\n" +
            "    ROUND(t2.half_avg, 2) second_half_avg,\n" +
            "    ROUND(t2.half_avg - t1.half_avg, 2) efficiency_improvement\n" +
            "FROM\n" +
            "    T t1\n" +
            "    JOIN T t2 ON t1.driver_id = t2.driver_id AND t1.half < t2.half AND t1.half_avg < t2.half_avg\n" +
            "    JOIN drivers d ON t1.driver_id = d.driver_id\n" +
            "ORDER BY efficiency_improvement DESC, d.driver_name;"
    }
}

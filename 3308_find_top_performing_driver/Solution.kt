// LeetCode 3308 - Find Top Performing Driver
// https://leetcode.com/problems/find-top-performing-driver/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            fuel_type,\n" +
            "            driver_id,\n" +
            "            ROUND(AVG(rating), 2) rating,\n" +
            "            SUM(distance) distance,\n" +
            "            SUM(accidents) accidents\n" +
            "        FROM\n" +
            "            Drivers\n" +
            "            JOIN Vehicles USING (driver_id)\n" +
            "            JOIN Trips USING (vehicle_id)\n" +
            "        GROUP BY fuel_type, driver_id\n" +
            "    ),\n" +
            "    P AS (\n" +
            "        SELECT\n" +
            "            *,\n" +
            "            RANK() OVER (\n" +
            "                PARTITION BY fuel_type\n" +
            "                ORDER BY rating DESC, distance DESC, accidents\n" +
            "            ) rk\n" +
            "        FROM T\n" +
            "    )\n" +
            "SELECT fuel_type, driver_id, rating, distance\n" +
            "FROM P\n" +
            "WHERE rk = 1\n" +
            "ORDER BY 1;"
    }
}

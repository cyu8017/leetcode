// LeetCode 2153 - The Number Of Passengers In Each Bus Ii
// https://leetcode.com/problems/the-number-of-passengers-in-each-bus-ii/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            *,\n" +
            "            SUM(cnt) OVER (ORDER BY dt, bus_id) AS cur,\n" +
            "            IF(@t > 0, @t := cnt, @t := @t + cnt) AS cur_sum\n" +
            "        FROM\n" +
            "            (\n" +
            "                SELECT bus_id, arrival_time AS dt, capacity AS cnt FROM Buses\n" +
            "                UNION ALL\n" +
            "                SELECT -1, arrival_time AS dt, -1 FROM Passengers\n" +
            "            ) AS a\n" +
            "            JOIN (SELECT @t := 0 AS x) AS b\n" +
            "    )\n" +
            "SELECT\n" +
            "    bus_id,\n" +
            "    IF(cur_sum > 0, cnt - cur_sum, cnt) AS passengers_cnt\n" +
            "FROM T\n" +
            "WHERE bus_id > 0\n" +
            "ORDER BY bus_id"
    }
}

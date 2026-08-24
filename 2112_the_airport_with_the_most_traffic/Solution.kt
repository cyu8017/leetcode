// LeetCode 2112 - The Airport With The Most Traffic
// https://leetcode.com/problems/the-airport-with-the-most-traffic/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT * FROM Flights\n" +
            "        UNION\n" +
            "        SELECT arrival_airport, departure_airport, flights_count FROM Flights\n" +
            "    ),\n" +
            "    P AS (\n" +
            "        SELECT departure_airport, SUM(flights_count) AS cnt\n" +
            "        FROM T\n" +
            "        GROUP BY 1\n" +
            "    )\n" +
            "SELECT departure_airport AS airport_id\n" +
            "FROM P\n" +
            "WHERE cnt = (SELECT MAX(cnt) FROM P)"
    }
}

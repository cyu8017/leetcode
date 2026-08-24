// LeetCode 3140 - Consecutive Available Seats Ii
// https://leetcode.com/problems/consecutive-available-seats-ii/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            *,\n" +
            "            seat_id - (RANK() OVER (ORDER BY seat_id)) AS gid\n" +
            "        FROM Cinema\n" +
            "        WHERE free = 1\n" +
            "    ),\n" +
            "    P AS (\n" +
            "        SELECT\n" +
            "            MIN(seat_id) AS first_seat_id,\n" +
            "            MAX(seat_id) AS last_seat_id,\n" +
            "            COUNT(1) AS consecutive_seats_len,\n" +
            "            RANK() OVER (ORDER BY COUNT(1) DESC) AS rk\n" +
            "        FROM T\n" +
            "        GROUP BY gid\n" +
            "    )\n" +
            "SELECT first_seat_id, last_seat_id, consecutive_seats_len\n" +
            "FROM P\n" +
            "WHERE rk = 1\n" +
            "ORDER BY 1;"
    }
}

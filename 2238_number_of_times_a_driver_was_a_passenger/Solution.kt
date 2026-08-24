// LeetCode 2238 - Number Of Times A Driver Was A Passenger
// https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger/

class Solution {
    companion object {
        const val QUERY = "WITH T AS (SELECT DISTINCT driver_id FROM Rides)\n" +
            "SELECT t.driver_id, COUNT(passenger_id) AS cnt\n" +
            "FROM\n" +
            "    T AS t\n" +
            "    LEFT JOIN Rides AS r ON t.driver_id = r.passenger_id\n" +
            "GROUP BY 1"
    }
}

// LeetCode 2238 - Number of Times a Driver Was a Passenger
// https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger/

const char* QUERY =
    "\n"
    "WITH T AS (SELECT DISTINCT driver_id FROM Rides)\n"
    "SELECT t.driver_id, COUNT(passenger_id) AS cnt\n"
    "FROM\n"
    "    T AS t\n"
    "    LEFT JOIN Rides AS r ON t.driver_id = r.passenger_id\n"
    "GROUP BY 1\n";

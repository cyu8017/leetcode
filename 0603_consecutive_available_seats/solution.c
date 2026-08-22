// LeetCode 0603 - Consecutive Available Seats
// https://leetcode.com/problems/consecutive-available-seats/

const char* QUERY =
    "\n"
    "SELECT DISTINCT c1.seat_id\n"
    "FROM Cinema c1\n"
    "JOIN Cinema c2 ON ABS(c1.seat_id - c2.seat_id) = 1\n"
    "WHERE c1.free = 1 AND c2.free = 1\n"
    "ORDER BY c1.seat_id\n";

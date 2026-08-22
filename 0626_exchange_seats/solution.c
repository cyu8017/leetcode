// LeetCode 0626 - Exchange Seats
// https://leetcode.com/problems/exchange-seats/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    CASE\n"
    "        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat) THEN id\n"
    "        WHEN id % 2 = 1 THEN id + 1\n"
    "        ELSE id - 1\n"
    "    END AS id,\n"
    "    student\n"
    "FROM Seat\n"
    "ORDER BY id\n";

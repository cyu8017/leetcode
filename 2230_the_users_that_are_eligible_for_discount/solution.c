// LeetCode 2230 - The Users That Are Eligible for Discount
// https://leetcode.com/problems/the-users-that-are-eligible-for-discount/

const char* QUERY =
    "\n"
    "CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)\n"
    "BEGIN\n"
    "  SELECT DISTINCT user_id\n"
    "  FROM Purchases\n"
    "  WHERE time_stamp BETWEEN startDate AND endDate\n"
    "    AND amount >= minAmount\n"
    "  ORDER BY user_id;\n"
    "END\n";

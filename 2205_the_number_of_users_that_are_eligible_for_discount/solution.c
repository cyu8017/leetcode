// LeetCode 2205 - The Number of Users That Are Eligible for Discount
// https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/

const char* QUERY =
    "\n"
    "CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT\n"
    "READS SQL DATA\n"
    "BEGIN\n"
    "  RETURN (\n"
    "    SELECT COUNT(DISTINCT user_id) AS user_cnt\n"
    "    FROM Purchases\n"
    "    WHERE time_stamp BETWEEN startDate AND endDate\n"
    "      AND amount >= minAmount\n"
    "  );\n"
    "END\n";

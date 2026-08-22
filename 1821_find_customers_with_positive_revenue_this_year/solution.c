// LeetCode 1821 - Find Customers With Positive Revenue this Year
// https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/

const char* QUERY =
    "\n"
    "SELECT customer_id\n"
    "FROM Customers\n"
    "WHERE year = 2021 AND revenue > 0\n";

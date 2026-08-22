// LeetCode 2082 - The Number of Rich Customers
// https://leetcode.com/problems/the-number-of-rich-customers/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    COUNT(DISTINCT customer_id) AS rich_count\n"
    "FROM Store\n"
    "WHERE amount > 500\n";

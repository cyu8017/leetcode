// LeetCode 3465 - Find Products with Valid Serial Numbers
// https://leetcode.com/problems/find-products-with-valid-serial-numbers/

const char* QUERY =
    "\n"
    "SELECT product_id, product_name, description\n"
    "FROM products\n"
    "WHERE description REGEXP '(?-i)\\\\bSN[0-9]{4}-[0-9]{4}\\\\b'\n"
    "ORDER BY 1;\n";

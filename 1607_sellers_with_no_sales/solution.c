// LeetCode 1607 - Sellers With No Sales
// https://leetcode.com/problems/sellers-with-no-sales/

const char* QUERY =
    "\n"
    "SELECT seller_name\n"
    "FROM Seller\n"
    "WHERE seller_id NOT IN (\n"
    "    SELECT seller_id FROM Orders\n"
    "    WHERE sale_date BETWEEN '2020-01-01' AND '2020-12-31'\n"
    ")\n"
    "ORDER BY seller_name;\n";

// LeetCode 1364 - Number of Trusted Contacts of a Customer
// https://leetcode.com/problems/number-of-trusted-contacts-of-a-customer/

const char* QUERY =
    "\n"
    "SELECT i.invoice_id, c.customer_name, i.price,\n"
    "       COUNT(co.contact_name) AS contacts_cnt,\n"
    "       COUNT(c2.customer_id) AS trusted_contacts_cnt\n"
    "FROM Invoices i\n"
    "JOIN Customers c ON c.customer_id = i.user_id\n"
    "LEFT JOIN Contacts co ON co.user_id = i.user_id\n"
    "LEFT JOIN Customers c2 ON c2.customer_name = co.contact_name\n"
    "GROUP BY i.invoice_id, c.customer_name, i.price\n"
    "ORDER BY i.invoice_id\n";

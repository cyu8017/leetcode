// LeetCode 1364 - Number Of Trusted Contacts Of A Customer
// https://leetcode.com/problems/number-of-trusted-contacts-of-a-customer/

export const QUERY = `SELECT i.invoice_id, c.customer_name, i.price,
       COUNT(co.contact_name) AS contacts_cnt,
       COUNT(c2.customer_id) AS trusted_contacts_cnt
FROM Invoices i
JOIN Customers c ON c.customer_id = i.user_id
LEFT JOIN Contacts co ON co.user_id = i.user_id
LEFT JOIN Customers c2 ON c2.customer_name = co.contact_name
GROUP BY i.invoice_id, c.customer_name, i.price
ORDER BY i.invoice_id`;

// LeetCode 2362 - Generate The Invoice
// https://leetcode.com/problems/generate-the-invoice/

class Solution {
    companion object {
        const val QUERY = "WITH P AS (\n" +
            "    SELECT *\n" +
            "    FROM Purchases\n" +
            "    JOIN Products USING (product_id)\n" +
            "),\n" +
            "T AS (\n" +
            "    SELECT invoice_id, SUM(price * quantity) AS amount\n" +
            "    FROM P\n" +
            "    GROUP BY invoice_id\n" +
            "    ORDER BY amount DESC, invoice_id\n" +
            "    LIMIT 1\n" +
            ")\n" +
            "SELECT product_id, quantity, (quantity * price) AS price\n" +
            "FROM P\n" +
            "JOIN T USING (invoice_id)\n" +
            "ORDER BY product_id"
    }
}

// LeetCode 1581 - Customer Who Visited But Did Not Make Any Transactions
// https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

class Solution {
    companion object {
        const val QUERY = "SELECT v.customer_id, COUNT(*) AS count_no_trans\n" +
            "FROM Visits v LEFT JOIN Transactions t ON t.visit_id = v.visit_id\n" +
            "WHERE t.transaction_id IS NULL\n" +
            "GROUP BY v.customer_id\\n"
    }
}

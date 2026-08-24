// LeetCode 1098 - Unpopular Books
// https://leetcode.com/problems/unpopular-books/

class Solution {
    companion object {
        const val QUERY = "SELECT b.book_id, b.name\n" +
            "FROM Books b\n" +
            "LEFT JOIN Orders o\n" +
            "    ON b.book_id = o.book_id\n" +
            "   AND o.dispatch_date >= '2018-06-23'\n" +
            "WHERE b.available_from <= '2019-05-23'\n" +
            "GROUP BY b.book_id, b.name\n" +
            "HAVING COALESCE(SUM(o.quantity), 0) < 10"
    }
}

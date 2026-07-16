class Solution {
    companion object {
        const val QUERY = "SELECT DISTINCT l1.num AS ConsecutiveNums\n" +
            "FROM Logs l1\n" +
            "JOIN Logs l2 ON l1.id = l2.id - 1 AND l1.num = l2.num\n" +
            "JOIN Logs l3 ON l2.id = l3.id - 1 AND l2.num = l3.num\n" +
            ""
    }
}

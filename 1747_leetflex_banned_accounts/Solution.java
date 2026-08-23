// LeetCode 1747 - Leetflex Banned Accounts
// https://leetcode.com/problems/leetflex-banned-accounts/

public class Solution {
    public static final String QUERY = "SELECT DISTINCT l1.account_id\n" +
        "FROM LogInfo l1\n" +
        "JOIN LogInfo l2\n" +
        "  ON l1.account_id = l2.account_id\n" +
        " AND l1.ip_address <> l2.ip_address\n" +
        " AND l1.login <= l2.logout\n" +
        " AND l2.login <= l1.logout;\n" +
        "";
}

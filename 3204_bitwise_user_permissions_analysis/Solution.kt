// LeetCode 3204 - Bitwise User Permissions Analysis
// https://leetcode.com/problems/bitwise-user-permissions-analysis/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    BIT_AND(permissions) AS common_perms,\n" +
            "    BIT_OR(permissions) AS any_perms\n" +
            "FROM user_permissions;"
    }
}

// LeetCode 3204 - Bitwise User Permissions Analysis
// https://leetcode.com/problems/bitwise-user-permissions-analysis/

public class Solution {
    public const string QUERY = @"
SELECT
    BIT_AND(permissions) AS common_perms,
    BIT_OR(permissions) AS any_perms
FROM user_permissions;
";
}

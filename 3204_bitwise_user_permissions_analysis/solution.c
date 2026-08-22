// LeetCode 3204 - Bitwise User Permissions Analysis
// https://leetcode.com/problems/bitwise-user-permissions-analysis/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    BIT_AND(permissions) AS common_perms,\n"
    "    BIT_OR(permissions) AS any_perms\n"
    "FROM user_permissions;\n";

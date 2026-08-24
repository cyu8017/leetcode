// LeetCode 1076 - Project Employees Ii
// https://leetcode.com/problems/project-employees-ii/

class Solution {
    companion object {
        const val QUERY = "SELECT project_id\n" +
            "FROM Project\n" +
            "GROUP BY project_id\n" +
            "HAVING COUNT(*) = (\n" +
            "    SELECT COUNT(*)\n" +
            "    FROM Project\n" +
            "    GROUP BY project_id\n" +
            "    ORDER BY COUNT(*) DESC\n" +
            "    LIMIT 1\n" +
            ")"
    }
}

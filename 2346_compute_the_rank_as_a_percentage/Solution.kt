// LeetCode 2346 - Compute The Rank As A Percentage
// https://leetcode.com/problems/compute-the-rank-as-a-percentage/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    student_id,\n" +
            "    department_id,\n" +
            "    IFNULL(\n" +
            "        ROUND(\n" +
            "            (\n" +
            "                RANK() OVER (\n" +
            "                    PARTITION BY department_id\n" +
            "                    ORDER BY mark DESC\n" +
            "                ) - 1\n" +
            "            ) * 100 / (COUNT(1) OVER (PARTITION BY department_id) - 1),\n" +
            "            2\n" +
            "        ),\n" +
            "        0\n" +
            "    ) AS percentage\n" +
            "FROM Students"
    }
}

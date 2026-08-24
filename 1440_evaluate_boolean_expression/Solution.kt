// LeetCode 1440 - Evaluate Boolean Expression
// https://leetcode.com/problems/evaluate-boolean-expression/

class Solution {
    companion object {
        const val QUERY = "SELECT e.left_operand, e.operator, e.right_operand,\n" +
            "       CASE\n" +
            "         WHEN e.operator = '>' AND lv.value > rv.value THEN 'true'\n" +
            "         WHEN e.operator = '<' AND lv.value < rv.value THEN 'true'\n" +
            "         WHEN e.operator = '=' AND lv.value = rv.value THEN 'true'\n" +
            "         ELSE 'false'\n" +
            "       END AS value\n" +
            "FROM Expressions e\n" +
            "JOIN Variables lv ON lv.name = e.left_operand\n" +
            "JOIN Variables rv ON rv.name = e.right_operand"
    }
}

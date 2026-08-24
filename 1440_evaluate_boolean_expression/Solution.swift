// LeetCode 1440 - Evaluate Boolean Expression
// https://leetcode.com/problems/evaluate-boolean-expression/

let QUERY = """
SELECT e.left_operand, e.operator, e.right_operand,
       CASE
         WHEN e.operator = '>' AND lv.value > rv.value THEN 'true'
         WHEN e.operator = '<' AND lv.value < rv.value THEN 'true'
         WHEN e.operator = '=' AND lv.value = rv.value THEN 'true'
         ELSE 'false'
       END AS value
FROM Expressions e
JOIN Variables lv ON lv.name = e.left_operand
JOIN Variables rv ON rv.name = e.right_operand
"""

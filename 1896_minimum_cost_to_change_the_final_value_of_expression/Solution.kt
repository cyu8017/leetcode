// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

class Solution {
    fun minOperationsToFlip(expression: String): Int {
        fun combine(left: IntArray, op: Char, right: IntArray): IntArray {
            val (leftVal, leftToZero, leftToOne) = Triple(left[0], left[1], left[2])
            val (rightVal, rightToZero, rightToOne) = Triple(right[0], right[1], right[2])
            return if (op == '&') {
                val andVal = leftVal and rightVal
                val andToZero = minOf(leftToZero, leftToOne + rightToZero)
                val andToOne = leftToOne + rightToOne
                val orToZero = leftToZero + rightToZero
                val orToOne = minOf(leftToOne, leftToZero + rightToOne, rightToZero + leftToOne)
                intArrayOf(andVal, minOf(andToZero, 1 + orToZero), minOf(andToOne, 1 + orToOne))
            } else {
                val orVal = leftVal or rightVal
                val orToZero = leftToZero + rightToZero
                val orToOne = minOf(leftToOne, leftToZero + rightToOne, rightToZero + leftToOne)
                val andToZero = minOf(leftToZero, leftToOne + rightToZero)
                val andToOne = leftToOne + rightToOne
                intArrayOf(orVal, minOf(orToZero, 1 + andToZero), minOf(orToOne, 1 + andToOne))
            }
        }
        var index = 0
        lateinit var parseExpr: () -> IntArray
        lateinit var parseFactor: () -> IntArray
        parseFactor = {
            if (expression[index] == '0' || expression[index] == '1') {
                val value = expression[index] - '0'
                index++
                intArrayOf(value, if (value == 0) 0 else 1, if (value == 0) 1 else 0)
            } else {
                index++
                val node = parseExpr()
                index++
                node
            }
        }
        parseExpr = {
            var node = parseFactor()
            while (index < expression.length && (expression[index] == '&' || expression[index] == '|')) {
                val op = expression[index]
                index++
                node = combine(node, op, parseFactor())
            }
            node
        }
        val result = parseExpr()
        return if (result[0] == 0) result[2] else result[1]
    }
}

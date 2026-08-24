// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

interface CustomFunction {
    fun f(x: Int, y: Int): Int
}

class Solution {
    fun findSolution(customfunction: CustomFunction, z: Int): List<List<Int>> {
        val answer = mutableListOf<List<Int>>()
        var x = 1
        var y = 1000
        while (x <= 1000 && y >= 1) {
            val value = customfunction.f(x, y)
            when {
                value == z -> {
                    answer.add(listOf(x, y))
                    x++
                    y--
                }
                value < z -> x++
                else -> y--
            }
        }
        return answer
    }
}

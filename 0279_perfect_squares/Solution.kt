// LeetCode 0279 - Perfect Squares
// https://leetcode.com/problems/perfect-squares/

import java.util.ArrayDeque

class Solution {
    fun numSquares(n: Int): Int {
        val squares = mutableListOf<Int>()
        var value = 1
        while (value * value <= n) {
            squares.add(value * value)
            value++
        }

        val queue = ArrayDeque<Pair<Int, Int>>()
        queue.add(n to 0)
        val visited = hashSetOf(n)

        while (queue.isNotEmpty()) {
            val (remain, steps) = queue.removeFirst()
            if (remain == 0) {
                return steps
            }
            for (square in squares) {
                val next = remain - square
                if (next < 0) {
                    break
                }
                if (visited.add(next)) {
                    queue.add(next to steps + 1)
                }
            }
        }
        return 0
    }
}

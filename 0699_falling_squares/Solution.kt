// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

class Solution {
    fun fallingSquares(positions: Array<IntArray>): MutableList<Int> {
        var intervals = ArrayList<IntArray>()
        var answer = ArrayList<Int>()
        var maxHeight = 0
        for (pos in positions) {
            var left = pos[0]
            var side = pos[1]
            var right = left + side
            var bas = 0
            for (it in intervals) {
                if (it[1] > left && it[0] < right) bas = maxOf(bas, it[2])
            }
            var height = bas + side
            intervals.add(intArrayOf(left, right, height))
            maxHeight = maxOf(maxHeight, height)
            answer.add(maxHeight)
        }
        return answer
    }
}

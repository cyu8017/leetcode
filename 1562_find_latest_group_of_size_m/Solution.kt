// LeetCode 1562 - Find Latest Group of Size M
// https://leetcode.com/problems/find-latest-group-of-size-m/

class Solution {
    fun findLatestStep(arr: IntArray, m: Int): Int {
        if (m == arr.size) return m
        val lengths = HashMap<Int, Int>()
        var answer = -1
        for (step in 1..arr.size) {
            val x = arr[step - 1]
            val left = lengths.getOrDefault(x - 1, 0)
            val right = lengths.getOrDefault(x + 1, 0)
            val size = left + 1 + right
            lengths[x - left] = size
            lengths[x + right] = size
            if (left == m || right == m) answer = step - 1
        }
        return answer
    }
}

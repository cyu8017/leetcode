// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

class Solution {
    fun removeInterval(intervals: Array<IntArray>, toBeRemoved: IntArray): Array<IntArray> {
        val left = toBeRemoved[0]
        val right = toBeRemoved[1]
        val answer = mutableListOf<IntArray>()
        for (interval in intervals) {
            val start = interval[0]
            val end = interval[1]
            if (end <= left || start >= right) {
                answer.add(intArrayOf(start, end))
            } else {
                if (start < left) answer.add(intArrayOf(start, left))
                if (end > right) answer.add(intArrayOf(right, end))
            }
        }
        return answer.toTypedArray()
    }
}

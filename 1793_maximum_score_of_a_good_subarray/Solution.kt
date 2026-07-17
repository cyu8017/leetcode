// LeetCode 1793 - Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/

class Solution {
    fun maximumScore(nums: IntArray, k: Int): Int {
        val n = nums.size
        val stack = ArrayDeque<Int>()
        var ans = 0L
        for (i in 0..n) {
            while (stack.isNotEmpty() && (i == n || nums[i] < nums[stack.last()])) {
                val mid = stack.removeLast()
                val left = if (stack.isNotEmpty()) stack.last() + 1 else 0
                val right = i - 1
                if (k in left..right) {
                    ans = maxOf(ans, nums[mid].toLong() * (right - left + 1))
                }
            }
            stack.addLast(i)
        }
        return ans.toInt()
    }
}

// LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution {
    fun maxScoreIndices(nums: IntArray): MutableList<Int> {
        var n: Int = nums.size
        var total1: Int = 0
        for (x in nums) total1 += x
        var best: Int = total1, left0 = 0, right1 = total1
        var ans = mutableListOf()
        ans.add(0)
        for (i in 0 until n) {
            if (nums[i] == 0) left0++
            else right1--
            var score: Int = left0 + right1
            if (score > best) { best = score; ans = mutableListOf(); ans.add(i + 1); }
            else if (score == best) ans.add(i + 1)
        }
        return ans
    }
}

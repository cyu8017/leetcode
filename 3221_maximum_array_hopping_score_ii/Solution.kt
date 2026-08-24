// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

class Solution {
    fun maxScore(nums: IntArray): Long {
        var stk = ArrayList<Int>()
        for (i in 0 until nums.size) {
            while (stk.size > 0 && nums[stk[stk.size - 1]] <= nums[i]) stk.remove(stk.size - 1)
            stk.add(i)
        }
        var ans = 0
        var cur = 0
        for (j in stk) {
            ans += (j - cur) * nums[j]
            cur = j
        }
        return ans
    }
}

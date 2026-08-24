// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

class Solution {
    fun maxSelectedElements(nums: IntArray): Int {
        nums.sort()
        var dp = HashMap<Int, Int>()
        var ans = 0
        for (num in nums) {
            var dn = dp.getOrDefault(num, 0)
            var dnm1 = dp.getOrDefault(num - 1, 0)
            dp[num + 1] = dn + 1
            dp[num] = dnm1 + 1
            ans = maxOf(ans, maxOf(dp[num], dp[num + 1]))
        }
        return ans
    }
}

// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

class Solution {
    fun resultArray(nums: IntArray, k: Int): LongArray {
        var ans = LongArray(k)
        var dp = LongArray(k)
        for (num in nums) {
            var newDp = LongArray(k)
            var nm = num % k
            newDp[nm] = 1
            for (i in 0 until k) { newDp[(i * nm) % k] += dp[i] }
            for (i in 0 until k) { ans[i] += newDp[i] }
            dp = newDp
        }
        return ans
    }
}

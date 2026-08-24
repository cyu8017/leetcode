// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

class Solution {
    fun countOppositeParity(nums: IntArray): IntArray {
        var cnt = { 0, 0 }
        for (x in nums) { cnt[x & 1]++ }
        var n = nums.size
        var ans = IntArray(n)
        for (i in 0 until n) {
            var x = nums[i]
            cnt[x & 1]--
            ans[i] = cnt[(x & 1) ^ 1]
        }
        return ans
    }
}

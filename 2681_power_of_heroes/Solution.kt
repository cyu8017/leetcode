// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

class Solution {
    fun sumOfPower(nums: IntArray): Int {
        val MOD = 1_000_000_007
        nums.sort()
        var ans = 0L
        var s = 0L
        for (x in nums) {
            ans = (ans + (s + x) % MOD * x % MOD * x) % MOD
            s = (s * 2 + x) % MOD
        }
        return ans.toInt()
    }
}

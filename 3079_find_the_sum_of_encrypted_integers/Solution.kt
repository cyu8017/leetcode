// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

class Solution {
    private fun encrypt(x0: Int): Int {
        var x = x0
        var mx = 0
        var p = 0
        while (x > 0) {
            mx = maxOf(mx, x % 10)
            p = p * 10 + 1
            x /= 10
        }
        return mx * p
    }

    fun sumOfEncryptedInt(nums: IntArray): Int {
        var ans = 0
        for (x in nums) ans += encrypt(x)
        return ans
    }
}

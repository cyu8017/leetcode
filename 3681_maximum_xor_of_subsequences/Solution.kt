// LeetCode 3681 - Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/

class Solution {
    fun maxXorSubsequences(nums: IntArray): Int {
        var basis = IntArray(32)
        for (x in nums) {
            var cur = x
            for (b in 31 downTo 0) {
                if ((cur & (1  shl  b)) == 0) continue
                if (basis[b] == 0) {
                    basis[b] = cur
                    break
                }
                cur ^= basis[b]
            }
        }
        var ans = 0
        for (b in 31 downTo 0) {
            if ((ans ^ basis[b]) > ans) ans ^= basis[b]
        }
        return ans
    }
}

// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

class Solution {
    fun duplicateNumbersXOR(nums: IntArray): Int {
        var cnt = IntArray(51)
        var ans = 0
        for (x in nums) {
            if (++cnt[x] == 2) ans ^= x
        }
        return ans
    }
}

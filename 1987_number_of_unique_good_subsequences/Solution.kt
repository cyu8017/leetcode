// LeetCode 1987
// https://leetcode.com/problems/number-of-unique-good-subsequences/

class Solution {
    fun numberOfUniqueGoodSubsequences(binary: String): Int {
        val mod = 1_000_000_007
        var ends0 = 0
        var ends1 = 0
        var has0 = false
        for (ch in binary) {
            if (ch == '0') {
                has0 = true
                ends0 = (ends0 + ends1) % mod
            } else {
                ends1 = (ends0 + ends1 + 1) % mod
            }
        }
        return (ends0 + ends1 + if (has0) 1 else 0) % mod
    }
}

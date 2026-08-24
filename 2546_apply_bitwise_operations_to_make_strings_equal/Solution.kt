// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

class Solution {
    fun makeStringsEqual(s: String, target: String): Boolean {
        var has1s = false
        var has1t = false
        for (i in 0 until s.length) {
            if (s[i] == '1') has1s = true
            if (target[i] == '1') has1t = true
        }
        return has1s == has1t
    }
}

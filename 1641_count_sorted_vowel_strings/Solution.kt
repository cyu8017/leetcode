// LeetCode 1641 - Count Sorted Vowel Strings
// https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution {
    fun countVowelStrings(n: Int): Int {
        // C(n+4, 4)
        var res = 1L
        for (i in 1..4) {
            res = res * (n + 4 - 4 + i) / i
        }
        return res.toInt()
    }
}

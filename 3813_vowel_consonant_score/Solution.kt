// LeetCode 3813 - Vowel Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

class Solution {
    fun vowelConsonantScore(s: String): Int {
        var v = 0
        var c = 0
        for (ch in s.toCharArray()) {
            if (ch.isLetter()) {
                c = c + 1
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') { v = v + 1 }
            }
        }
        c -= v
        if (c == 0) return 0
        return v / c
    }
}

// LeetCode 3813 - Vowel Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

class Solution {
    func vowelConsonantScore(_ s: String) -> Int {
        var v = 0, c = 0
        for ch in s where ch.isLetter {
            c += 1
            if "aeiou".contains(ch) { v += 1 }
        }
        c -= v
        if c == 0 { return 0 }
        return v / c
    }
}

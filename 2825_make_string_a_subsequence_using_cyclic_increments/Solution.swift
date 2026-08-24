// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution {
    func canMakeSubsequence(_ str1: String, _ str2: String) -> Bool {
        let a = Array(str1), b = Array(str2)
        var j = 0
        for ch in a where j < b.count {
            let av = Int(ch.asciiValue! - 97)
            let bv = Int(b[j].asciiValue! - 97)
            if av == bv || (av + 1) % 26 == bv { j += 1 }
        }
        return j == b.count
    }
}

// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution {
    func closeStrings(_ word1: String, _ word2: String) -> Bool {
        if word1.count != word2.count { return false }
        func count(_ s: String) -> [Int] {
            var c = Array(repeating: 0, count: 26)
            for ch in s.utf8 {
                c[Int(ch) - 97] += 1
            }
            return c
        }
        var a = count(word1)
        var b = count(word2)
        for i in 0..<26 {
            if (a[i] == 0) != (b[i] == 0) { return false }
        }
        a.sort()
        b.sort()
        return a == b
    }
}

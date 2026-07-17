// LeetCode 1790 - Check if One String Swap Can Make Strings Equal
// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution {
    func areAlmostEqual(_ s1: String, _ s2: String) -> Bool {
        let a = Array(s1)
        let b = Array(s2)
        var diff: [Int] = []
        for i in 0..<a.count where a[i] != b[i] {
            diff.append(i)
        }
        if diff.isEmpty { return true }
        return diff.count == 2 && a[diff[0]] == b[diff[1]] && a[diff[1]] == b[diff[0]]
    }
}

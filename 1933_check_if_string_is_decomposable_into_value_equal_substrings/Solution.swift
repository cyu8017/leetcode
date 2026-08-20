// LeetCode 1933 - Check if String Is Decomposable Into Value-Equal Substrings
// https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

class Solution {
    func isDecomposable(_ s: String) -> Bool {
        let chars = Array(s)
        let n = chars.count
        var i = 0, twos = 0
        while i < n {
            var j = i
            while j < n && chars[j] == chars[i] { j += 1 }
            let length = j - i
            if length % 3 == 1 { return false }
            if length % 3 == 2 {
                twos += 1
                if twos > 1 { return false }
            }
            i = j
        }
        return twos == 1
    }
}

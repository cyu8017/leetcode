// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

class Solution {
    func hasSameDigits(_ s: String) -> Bool {
        var b = Array(s).map { Int($0.asciiValue! - 48) }
        while b.count > 2 {
            var nb = [Int]()
            for i in 0..<(b.count - 1) { nb.append((b[i] + b[i + 1]) % 10) }
            b = nb
        }
        return b[0] == b[1]
    }
}

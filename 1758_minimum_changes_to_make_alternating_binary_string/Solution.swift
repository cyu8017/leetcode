// LeetCode 1758 - Minimum Changes To Make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution {
    func minOperations(_ s: String) -> Int {
        var alt1 = 0
        for (i, ch) in s.utf8.enumerated() {
            let expected: UInt8 = (i & 1) == 0 ? 48 : 49
            if ch != expected {
                alt1 += 1
            }
        }
        return min(alt1, s.count - alt1)
    }
}

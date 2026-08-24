// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution {
    func hasAlternatingBits(_ n: Int) -> Bool {
        var n = n
        var prev = n & 1
        n >>= 1
        while n > 0 {
            if (n & 1) == prev { return false }
            prev = n & 1
            n >>= 1
        }
        return true
    }
}

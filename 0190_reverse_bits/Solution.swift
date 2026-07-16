// LeetCode 0190 - Reverse Bits
// https://leetcode.com/problems/reverse-bits/

class Solution {
    func reverseBits(_ n: UInt32) -> UInt32 {
        var number = n
        var result: UInt32 = 0
        for _ in 0..<32 {
            result = (result << 1) | (number & 1)
            number >>= 1
        }
        return result
    }
}
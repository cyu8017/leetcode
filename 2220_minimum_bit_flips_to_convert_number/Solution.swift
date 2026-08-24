// LeetCode 2220 - Minimum Bit Flips to Convert Number
// https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution {
    func minBitFlips(_ start: Int, _ goal: Int) -> Int {
        var x = start ^ goal
        var ans = 0
        while x > 0 {
            ans += x & 1
            x >>= 1
        }
        return ans
    }
}

// LeetCode 0389 - Find the Difference
// https://leetcode.com/problems/find-the-difference/

class Solution {
    func findTheDifference(_ s: String, _ t: String) -> Character {
        var xorValue: UInt8 = 0
        for byte in (s + t).utf8 {
            xorValue ^= byte
        }
        return Character(UnicodeScalar(xorValue))
    }
}

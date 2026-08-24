// LeetCode 0717 - 1-bit and 2-bit Characters
// https://leetcode.com/problems/1-bit-and-2-bit-characters/

class Solution {
    func isOneBitCharacter(_ bits: [Int]) -> Bool {
        var i = 0
        while i < bits.count - 1 {
            i += bits[i] == 1 ? 2 : 1
        }
        return i == bits.count - 1
    }
}

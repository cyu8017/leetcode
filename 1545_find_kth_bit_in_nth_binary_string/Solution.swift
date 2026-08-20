// LeetCode 1545 - Find Kth Bit in Nth Binary String
// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution {
    func findKthBit(_ n: Int, _ k: Int) -> Character {
        var invert = false
        var length = (1 << n) - 1
        var k = k
        while k != 1 {
            let middle = length / 2 + 1
            if k == middle { return invert ? "0" : "1" }
            if k > middle {
                k = length - k + 1
                invert.toggle()
            }
            length /= 2
        }
        return invert ? "1" : "0"
    }
}

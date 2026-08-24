// LeetCode 2429 - Minimize XOR
// https://leetcode.com/problems/minimize-xor/

class Solution {
    func minimizeXor(_ num1: Int, _ num2: Int) -> Int {
        var bits = 0
        var x = num2
        while x != 0 {
            x &= x - 1
            bits += 1
        }
        var ans = 0
        var i = 31
        while i >= 0 && bits > 0 {
            if ((num1 >> i) & 1) != 0 {
                ans |= 1 << i
                bits -= 1
            }
            i -= 1
        }
        i = 0
        while i < 32 && bits > 0 {
            if ((ans >> i) & 1) == 0 {
                ans |= 1 << i
                bits -= 1
            }
            i += 1
        }
        return ans
    }
}

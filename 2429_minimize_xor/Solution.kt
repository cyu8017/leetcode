// LeetCode 2429 - Minimize XOR
// https://leetcode.com/problems/minimize-xor/

class Solution {
    fun minimizeXor(num1: Int, num2: Int): Int {
            var bits: Int = 0
            var x: Int = num2
    while (x != 0) {
    bits = bits + 1
    x &=x - 1
    }
            var ans: Int = 0
            var i: Int = 31
    while (i >= 0 && bits > 0) {
    
                if (((num1 >> i) & 1) != 0) {
                    ans |=1 << i
                    bits = bits - 1
                }
    
    i = i - 1
    }
            var i: Int = 0
    while (i < 32 && bits > 0) {
    
                if (((ans >> i) & 1) == 0) {
                    ans |=1 << i
                    bits = bits - 1
                }
    
    i = i + 1
    }
            return ans
    }
}

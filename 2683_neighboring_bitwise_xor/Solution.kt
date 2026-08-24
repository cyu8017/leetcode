// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

class Solution {
    fun doesValidArrayExist(derived: IntArray): Boolean {
        var x = 0
        for (v in derived) x = x xor v
        return x == 0
    }
}

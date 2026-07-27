// LeetCode 1611 - Minimum One Bit Operations to Make Integers Zero
// https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

class Solution {
    fun minimumOneBitOperations(n: Int): Int {
        var x = n
        var ans = 0
        while (x != 0) {
            ans = ans xor x
            x = x shr 1
        }
        return ans
    }
}

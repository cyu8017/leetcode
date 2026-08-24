// LeetCode 0868 - Binary Gap
// https://leetcode.com/problems/binary-gap/

class Solution {
    fun binaryGap(n: Int): Int {
        var last = -1
        var ans = 0
        var bit = 0
        while (n != 0) {
            if ((n & 1) == 1) {
                if (last != -1) ans = maxOf(ans, bit - last)
                last = bit
            }
            n >>= 1
            bit++
        }
        return ans
    }
}

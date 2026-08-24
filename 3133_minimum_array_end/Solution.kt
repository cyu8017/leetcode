// LeetCode 3133 - Minimum Array End
// https://leetcode.com/problems/minimum-array-end/

class Solution {
    fun minEnd(n: Int, x: Int): Long {
        n--
        var ans = x
        for (i in 0 until 31) {
            if (((x  shr  i) & 1) == 0) {
                ans |= (n & 1)  shl  i
                n >>= 1
            }
        }
        ans |= n  shl  31
        return ans
    }
}

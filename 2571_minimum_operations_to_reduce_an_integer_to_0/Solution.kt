// LeetCode 2571 - Minimum Operations to Reduce an Integer to 0
// https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

class Solution {
    fun minOperations(n: Int): Int {
        var ans = 0
        while (n > 0) {
            if ((n & 3) == 3) {
                n = n + 1
                ans = ans + 1
            } else if ((n & 1) != 0) {
                n = n - 1
                ans = ans + 1
            } else {
                n >>= 1
            }
        }
        return ans
    }
}

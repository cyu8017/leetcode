// LeetCode 1492 - The kth Factor of n
// https://leetcode.com/problems/the-kth-factor-of-n/

class Solution {
    fun kthFactor(n: Int, k: Int): Int {
        var remaining = k
        for (x in 1..n) {
            if (n % x == 0) {
                remaining--
                if (remaining == 0) return x
            }
        }
        return -1
    }
}

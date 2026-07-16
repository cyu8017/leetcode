// LeetCode 0231 - Power of Two
// https://leetcode.com/problems/power-of-two/

class Solution {
    fun isPowerOfTwo(n: Int): Boolean {
        return n > 0 && (n and (n - 1)) == 0
    }
}

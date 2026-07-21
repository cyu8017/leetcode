// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

class Solution {
    fun sumBase(n: Int, k: Int): Int {
        var num = n
        var total = 0
        while (num > 0) {
            total += num % k
            num /= k
        }
        return total
    }
}

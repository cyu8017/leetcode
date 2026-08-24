// LeetCode 2310 - Sum of Numbers With Units Digit K
// https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

class Solution {
    fun minimumNumbers(num: Int, k: Int): Int {
        if (num == 0) return 0
        for (count in 1..10) {
            if (count * k % 10 == num % 10 && count * k <= num) return count
        }
        return -1
    }
}

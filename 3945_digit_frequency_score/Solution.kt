// LeetCode 3945 - Digit Frequency Score
// https://leetcode.com/problems/digit-frequency-score/

class Solution {
    fun digitFrequencyScore(n: Int): Int {
        var ans = 0
        var x = n
        while (x > 0) {
            ans += x % 10
            x /= 10
        }
        return ans
    }
}

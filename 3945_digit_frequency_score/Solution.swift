// LeetCode 3945 - Digit Frequency Score
// https://leetcode.com/problems/digit-frequency-score/


class Solution {
    func digitFrequencyScore(_ n: Int) -> Int {
        var n = n, ans = 0
        while n > 0 {
            ans += n % 10
            n /= 10
        }
        return ans
    }
}

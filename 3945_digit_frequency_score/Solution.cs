// LeetCode 3945 - Digit Frequency Score
// https://leetcode.com/problems/digit-frequency-score/

public class Solution {
    public int DigitFrequencyScore(int n) {
        int ans = 0;
        for (; n > 0; n /= 10) ans += n % 10;
        return ans;
    }
}

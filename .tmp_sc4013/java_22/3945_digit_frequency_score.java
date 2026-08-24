// CONFIG class=Solution method=digitFrequencyScore types=None
// LeetCode 3945 - Digit Frequency Score
// https://leetcode.com/problems/digit-frequency-score/

class Solution {
    public int digitFrequencyScore(int n) {
        int ans = 0;
        for (; n > 0; n /= 10) ans += n % 10;
        return ans;
    }
}

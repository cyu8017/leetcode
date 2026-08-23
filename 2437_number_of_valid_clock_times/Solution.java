// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

class Solution {
    public int countTime(String time) {
        int ans = 0;
        for (int h = 0; h < 24; h++) {
            for (int m = 0; m < 60; m++) {
                char h0 = (char)('0' + h / 10), h1 = (char)('0' + h % 10);
                char m0 = (char)('0' + m / 10), m1 = (char)('0' + m % 10);
                if (time.charAt(0) != '?' && time.charAt(0) != h0) continue;
                if (time.charAt(1) != '?' && time.charAt(1) != h1) continue;
                if (time.charAt(3) != '?' && time.charAt(3) != m0) continue;
                if (time.charAt(4) != '?' && time.charAt(4) != m1) continue;
                ans++;
            }
        }
        return ans;
    }
}

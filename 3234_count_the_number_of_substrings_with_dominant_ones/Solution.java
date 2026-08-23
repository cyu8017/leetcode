// LeetCode 3234 - Count the Number of Substrings With Dominant Ones
// https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

class Solution {
    public int numberOfSubstrings(String s) {
        int n = s.length();
        int[] nxt = new int[n + 1];
        nxt[n] = n;
        for (int i = n - 1; i >= 0; i--) {
            nxt[i] = nxt[i + 1];
            if (s.charAt(i) == '0') nxt[i] = i;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int cnt0 = (s.charAt(i) == '0') ? 1 : 0;
            int j = i;
            while (j < n && (long)cnt0 * cnt0 <= n) {
                int cnt1 = nxt[j + 1] - i - cnt0;
                if (cnt1 >= cnt0 * cnt0) {
                    ans += Math.min(nxt[j + 1] - j, cnt1 - cnt0 * cnt0 + 1);
                }
                j = nxt[j + 1];
                cnt0++;
            }
        }
        return ans;
    }
}

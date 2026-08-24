// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

class Solution {
    public int largestVariance(String s) {
        int ans = 0;
        for (char a = 'a'; a <= 'z'; a++) {
            for (char b = 'a'; b <= 'z'; b++) {
                if (a == b) continue;
                int bal = 0;
                boolean hasB = false;
                for (char c : s.toCharArray()) {
                    if (c == a) bal++;
                    else if (c == b) { bal--; hasB = true; }
                    if (hasB) ans = Math.max(ans, bal);
                    if (bal < 0) { bal = 0; hasB = false; }
                }
            }
        }
        return ans;
    }
}

// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

using System;

public class Solution {
    public int LargestVariance(string s) {
        int ans = 0;
        for (char a = 'a'; a <= 'z'; a++) {
            for (char b = 'a'; b <= 'z'; b++) {
                if (a == b) continue;
                int bal = 0;
                bool hasB = false;
                foreach (char c in s) {
                    if (c == a) bal++;
                    else if (c == b) { bal--; hasB = true; }
                    if (hasB) ans = Math.Max(ans, bal);
                    if (bal < 0) { bal = 0; hasB = false; }
                }
            }
        }
        return ans;
    }
}

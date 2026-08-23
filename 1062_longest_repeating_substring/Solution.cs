// LeetCode 1062 - Longest Repeating Substring
// https://leetcode.com/problems/longest-repeating-substring/

using System.Collections.Generic;

public class Solution {
    public int LongestRepeatingSubstring(string s) {
        int n = s.Length;

        bool HasDup(int length) {
            var seen = new HashSet<string>();
            for (int i = 0; i <= n - length; i++) {
                string sub = s.Substring(i, length);
                if (!seen.Add(sub)) {
                    return true;
                }
            }
            return false;
        }

        int lo = 1, hi = n - 1, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (HasDup(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
}

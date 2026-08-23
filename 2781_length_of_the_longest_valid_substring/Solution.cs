// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

using System;
using System.Collections.Generic;

public class Solution {
    public int LongestValidSubstring(string word, IList<string> forbidden) {
        var forbid = new HashSet<string>();
        int maxLen = 0;
        foreach (var f in forbidden) {
            forbid.Add(f);
            maxLen = Math.Max(maxLen, f.Length);
        }
        int ans = 0, right = word.Length - 1;
        for (int left = word.Length - 1; left >= 0; left--) {
            for (int k = left; k <= right && k - left + 1 <= maxLen; k++) {
                if (forbid.Contains(word.Substring(left, k - left + 1))) {
                    right = k - 1;
                    break;
                }
            }
            ans = Math.Max(ans, right - left + 1);
        }
        return ans;
    }
}

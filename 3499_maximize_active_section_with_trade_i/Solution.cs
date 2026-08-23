// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

using System.Collections.Generic;

public class Solution {
    public int MaxActiveSectionsAfterTrade(string s) {
        int ones = 0;
        foreach (char c in s) if (c == '1') ones++;
        var zeros = new List<(int l, int r)>();
        int n = s.Length;
        for (int i = 0; i < n;) {
            if (s[i] != '0') { i++; continue; }
            int j = i;
            while (j < n && s[j] == '0') j++;
            zeros.Add((i, j - 1));
            i = j;
        }
        int best = 0;
        for (int i = 0; i + 1 < zeros.Count; i++) {
            int gain = (zeros[i].r - zeros[i].l + 1) + (zeros[i + 1].r - zeros[i + 1].l + 1);
            if (gain > best) best = gain;
        }
        return ones + best;
    }
}

// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

using System;
using System.Collections.Generic;

public class Solution {
    public int LongestWPI(int[] hours) {
        int score = 0, ans = 0;
        var firstSeen = new Dictionary<int, int> { [0] = -1 };
        for (int i = 0; i < hours.Length; i++) {
            score += hours[i] > 8 ? 1 : -1;
            if (score > 0) ans = i + 1;
            else if (firstSeen.ContainsKey(score - 1)) ans = Math.Max(ans, i - firstSeen[score - 1]);
            if (!firstSeen.ContainsKey(score)) firstSeen[score] = i;
        }
        return ans;
    }
}

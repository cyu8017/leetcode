// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int LargestValsFromLabels(int[] values, int[] labels, int numWanted, int useLimit) {
        var items = values.Zip(labels, (v, l) => (v, l)).OrderByDescending(x => x.v).ToList();
        var used = new Dictionary<int, int>();
        int ans = 0, taken = 0;
        foreach (var (value, label) in items) {
            if (taken == numWanted) {
                break;
            }
            int cnt = used.GetValueOrDefault(label);
            if (cnt < useLimit) {
                used[label] = cnt + 1;
                ans += value;
                taken++;
            }
        }
        return ans;
    }
}

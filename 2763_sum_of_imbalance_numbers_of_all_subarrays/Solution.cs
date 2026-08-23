// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

using System.Collections.Generic;

public class Solution {
    public int SumImbalanceNumbers(int[] nums) {
        int n = nums.Length, ans = 0;
        for (int i = 0; i < n; i++) {
            var seen = new HashSet<int>();
            var sortedVals = new SortedSet<int>();
            int imbalance = 0;
            for (int j = i; j < n; j++) {
                int x = nums[j];
                if (!seen.Contains(x)) {
                    seen.Add(x);
                    var greater = sortedVals.GetViewBetween(x, int.MaxValue);
                    int? next = null, prev = null;
                    foreach (var v in greater) { next = v; break; }
                    var lesser = sortedVals.GetViewBetween(int.MinValue, x);
                    foreach (var v in lesser) prev = v;
                    if (prev.HasValue && x - prev.Value != 1) imbalance++;
                    if (next.HasValue && next.Value - x != 1) imbalance++;
                    if (prev.HasValue && next.HasValue && next.Value - prev.Value > 1) imbalance--;
                    sortedVals.Add(x);
                }
                ans += imbalance;
            }
        }
        return ans;
    }
}

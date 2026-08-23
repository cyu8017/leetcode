// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

using System.Collections.Generic;

public class Solution {
    public int MaxNumberOfAlloys(int n, int k, int budget, IList<IList<int>> composition, IList<int> stock, IList<int> cost) {
        bool Ok(long machines) {
            foreach (var comp in composition) {
                long spend = 0;
                for (int i = 0; i < n; i++) {
                    long need = machines * comp[i] - stock[i];
                    if (need > 0) spend += need * cost[i];
                }
                if (spend <= budget) return true;
            }
            return false;
        }
        long lo = 0, hi = 1000000000L, ans = 0;
        while (lo <= hi) {
            long mid = (lo + hi) / 2;
            if (Ok(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return (int)ans;
    }
}

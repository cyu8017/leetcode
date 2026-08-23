// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

using System.Collections.Generic;

public class Solution {
    public int MinArrivalsToDiscard(int[] arrivals, int w, int m) {
        var cnt = new Dictionary<int, int>();
        int n = arrivals.Length;
        int[] marked = new int[n];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int x = arrivals[i];
            if (i >= w) {
                if (!cnt.ContainsKey(arrivals[i - w])) cnt[arrivals[i - w]] = 0;
                cnt[arrivals[i - w]] -= marked[i - w];
            }
            if (!cnt.ContainsKey(x)) cnt[x] = 0;
            if (cnt[x] >= m) ans++;
            else {
                marked[i] = 1;
                cnt[x]++;
            }
        }
        return ans;
    }
}

// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxCount(int[] banned, int n, long maxSum) {
        Array.Sort(banned);
        var uniq = new List<int>();
        foreach (int x in banned) {
            if (x >= 1 && x <= n && (uniq.Count == 0 || uniq[uniq.Count - 1] != x)) uniq.Add(x);
        }
        int ans = 0;
        int prev = 0;
        long remain = maxSum;
        void Check(long l, long r) {
            if (l > r || remain <= 0) return;
            long lo = l, hi = r, best = l - 1;
            while (lo <= hi) {
                long mid = (lo + hi) / 2;
                long cnt = mid - l + 1;
                long sum = (l + mid) * cnt / 2;
                if (sum <= remain) {
                    best = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            if (best >= l) {
                int cnt = (int)(best - l + 1);
                ans += cnt;
                remain -= (l + best) * cnt / 2;
            }
        }
        foreach (int b in uniq) {
            Check((long)prev + 1, (long)b - 1);
            prev = b;
        }
        Check((long)prev + 1, (long)n);
        return ans;
    }
}

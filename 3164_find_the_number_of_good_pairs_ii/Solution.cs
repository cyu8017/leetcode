// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public long NumberOfPairs(int[] nums1, int[] nums2, int k) {
        var cnt1 = new Dictionary<int, int>();
        foreach (int x in nums1) {
            if (x % k == 0) {
                int y = x / k;
                if (!cnt1.ContainsKey(y)) cnt1[y] = 0;
                cnt1[y]++;
            }
        }
        if (cnt1.Count == 0) return 0;
        var cnt2 = new Dictionary<int, int>();
        foreach (int x in nums2) {
            if (!cnt2.ContainsKey(x)) cnt2[x] = 0;
            cnt2[x]++;
        }
        int mx = 0;
        foreach (var kv in cnt1) mx = Math.Max(mx, kv.Key);
        long ans = 0;
        foreach (var kv in cnt2) {
            int x = kv.Key, v = kv.Value;
            int s = 0;
            for (int y = x; y <= mx; y += x) {
                if (cnt1.TryGetValue(y, out int c)) s += c;
            }
            ans += 1L * s * v;
        }
        return ans;
    }
}

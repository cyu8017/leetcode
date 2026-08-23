// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int LargestComponentSize(int[] nums) {
        int mx = nums.Max();
        int[] parent = new int[mx + 1];
        for (int i = 0; i <= mx; i++) parent[i] = i;
        int Find(int x) => parent[x] == x ? x : parent[x] = Find(parent[x]);
        void Unite(int a, int b) { parent[Find(a)] = Find(b); }
        List<int> Factors(int x) {
            var res = new List<int>();
            for (int d = 2; (long)d * d <= x; d++) {
                if (x % d == 0) {
                    res.Add(d);
                    while (x % d == 0) x /= d;
                }
            }
            if (x > 1) res.Add(x);
            return res;
        }
        foreach (int num in nums)
            foreach (int f in Factors(num)) Unite(num, f);
        var cnt = new Dictionary<int, int>();
        int ans = 0;
        foreach (int num in nums) {
            int r = Find(num);
            if (!cnt.ContainsKey(r)) cnt[r] = 0;
            ans = Math.Max(ans, ++cnt[r]);
        }
        return ans;
    }
}

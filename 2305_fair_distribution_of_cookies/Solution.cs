// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

using System;
using System.Collections.Generic;

public class Solution {
    public int DistributeCookies(int[] cookies, int k) {
        int n = cookies.Length;
        int[] bags = new int[k];
        int ans = int.MaxValue;
        void Dfs(int i) {
            if (i == n) {
                int mx = bags[0];
                for (int t = 1; t < k; t++) mx = Math.Max(mx, bags[t]);
                ans = Math.Min(ans, mx);
                return;
            }
            var seen = new HashSet<int>();
            for (int j = 0; j < k; ++j) {
                if (seen.Contains(bags[j])) continue;
                seen.Add(bags[j]);
                bags[j] += cookies[i];
                if (bags[j] < ans) Dfs(i + 1);
                bags[j] -= cookies[i];
                if (bags[j] == 0) break;
            }
        }
        Dfs(0);
        return ans;
    }
}

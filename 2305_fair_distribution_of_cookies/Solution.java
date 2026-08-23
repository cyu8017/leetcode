// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

import java.util.HashSet;
import java.util.Set;

class Solution {
    private int[] cookies;
    private int[] bags;
    private int ans = Integer.MAX_VALUE;

    public int distributeCookies(int[] cookies, int k) {
        this.cookies = cookies;
        bags = new int[k];
        ans = Integer.MAX_VALUE;
        dfs(0);
        return ans;
    }

    private void dfs(int i) {
        if (i == cookies.length) {
            int mx = 0;
            for (int b : bags) mx = Math.max(mx, b);
            ans = Math.min(ans, mx);
            return;
        }
        Set<Integer> seen = new HashSet<>();
        for (int j = 0; j < bags.length; ++j) {
            if (!seen.add(bags[j])) continue;
            bags[j] += cookies[i];
            if (bags[j] < ans) dfs(i + 1);
            bags[j] -= cookies[i];
            if (bags[j] == 0) break;
        }
    }
}

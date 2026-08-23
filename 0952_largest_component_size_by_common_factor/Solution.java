// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

import java.util.*;

class Solution {
    private int[] parent;

    public int largestComponentSize(int[] nums) {
        int mx = 0;
        for (int x : nums) mx = Math.max(mx, x);
        parent = new int[mx + 1];
        for (int i = 0; i <= mx; i++) parent[i] = i;
        for (int num : nums)
            for (int f : factors(num)) unite(num, f);
        Map<Integer, Integer> cnt = new HashMap<>();
        int ans = 0;
        for (int num : nums) {
            int r = find(num);
            int c = cnt.getOrDefault(r, 0) + 1;
            cnt.put(r, c);
            ans = Math.max(ans, c);
        }
        return ans;
    }

    private int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }

    private void unite(int a, int b) {
        parent[find(a)] = find(b);
    }

    private List<Integer> factors(int x) {
        List<Integer> res = new ArrayList<>();
        for (int d = 2; (long) d * d <= x; d++) {
            if (x % d == 0) {
                res.add(d);
                while (x % d == 0) x /= d;
            }
        }
        if (x > 1) res.add(x);
        return res;
    }
}

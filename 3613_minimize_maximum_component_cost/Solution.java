// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

import java.util.Arrays;

class Solution {
    private int[] p;

    private int find(int x) {
        return p[x] == x ? x : (p[x] = find(p[x]));
    }

    public int minCost(int n, int[][] edges, int k) {
        p = new int[n];
        for (int i = 0; i < n; i++) p[i] = i;
        if (k == n) return 0;
        Arrays.sort(edges, (a, b) -> Integer.compare(a[2], b[2]));
        int cnt = n;
        for (int[] e : edges) {
            int pu = find(e[0]), pv = find(e[1]);
            if (pu != pv) {
                p[pu] = pv;
                if (--cnt <= k) return e[2];
            }
        }
        return 0;
    }
}

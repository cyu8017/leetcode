// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;

class Solution {
    private int expandPal(List<Integer>[] g, String label, int l, int r) {
        Set<Long> vis = new HashSet<>();
        Queue<int[]> q = new ArrayDeque<>();
        int len0 = (l != r) ? 2 : 1;
        q.offer(new int[] {l, r, len0});
        int best = len0;
        vis.add(pack(Math.min(l, r), Math.max(l, r)));
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int a : g[cur[0]]) {
                for (int b : g[cur[1]]) {
                    if (a == b || label.charAt(a) != label.charAt(b)) continue;
                    long p = pack(Math.min(a, b), Math.max(a, b));
                    if (vis.contains(p)) continue;
                    vis.add(p);
                    int nl = cur[2] + 2;
                    best = Math.max(best, nl);
                    q.offer(new int[] {a, b, nl});
                }
            }
        }
        return best;
    }

    private static long pack(int a, int b) {
        return (((long) a) << 32) | (b & 0xffffffffL);
    }

    public int maxLen(int n, int[][] edges, String label) {
        @SuppressWarnings("unchecked")
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        int ans = 1;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, expandPal(g, label, i, i));
            for (int j : g[i]) {
                if (i < j && label.charAt(i) == label.charAt(j))
                    ans = Math.max(ans, expandPal(g, label, i, j));
            }
        }
        return ans;
    }
}

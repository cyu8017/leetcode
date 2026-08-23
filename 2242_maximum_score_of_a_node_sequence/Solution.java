// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int maximumScore(int[] scores, int[][] edges) {
        int n = scores.length;
        @SuppressWarnings("unchecked")
        List<Integer>[] top = new ArrayList[n];
        @SuppressWarnings("unchecked")
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            top[i] = new ArrayList<>();
            g[i] = new ArrayList<>();
        }
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        for (int i = 0; i < n; i++) {
            for (int v : g[i]) {
                top[i].add(v);
                for (int j = top[i].size() - 1; j > 0; j--) {
                    if (scores[top[i].get(j)] > scores[top[i].get(j - 1)]) {
                        int tmp = top[i].get(j);
                        top[i].set(j, top[i].get(j - 1));
                        top[i].set(j - 1, tmp);
                    }
                }
                if (top[i].size() > 3) top[i].subList(3, top[i].size()).clear();
            }
        }
        int ans = -1;
        for (int[] e : edges) {
            int a = e[0], b = e[1];
            for (int c : top[a]) {
                if (c == b) continue;
                for (int d : top[b]) {
                    if (d == a || d == c) continue;
                    ans = Math.max(ans, scores[a] + scores[b] + scores[c] + scores[d]);
                }
            }
        }
        return ans;
    }
}

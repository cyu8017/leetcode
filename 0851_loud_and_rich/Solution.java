// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

import java.util.*;

class Solution {
    private List<Integer>[] graph;
    private int[] quiet;
    private int[] ans;

    public int[] loudAndRich(int[][] richer, int[] quiet) {
        int n = quiet.length;
        this.quiet = quiet;
        graph = new List[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : richer) graph[e[1]].add(e[0]);
        ans = new int[n];
        Arrays.fill(ans, -1);
        for (int i = 0; i < n; i++) dfs(i);
        return ans;
    }

    private int dfs(int person) {
        if (ans[person] != -1) return ans[person];
        int best = person;
        for (int richerPerson : graph[person]) {
            int cand = dfs(richerPerson);
            if (quiet[cand] < quiet[best]) best = cand;
        }
        return ans[person] = best;
    }
}

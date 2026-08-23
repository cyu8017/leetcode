// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] permute(int n) {
        List<int[]> ans = new ArrayList<>();
        boolean[] used = new boolean[n + 1];
        List<Integer> cur = new ArrayList<>();
        dfs(n, used, cur, ans);
        int[][] res = new int[ans.size()][];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }

    private void dfs(int n, boolean[] used, List<Integer> cur, List<int[]> ans) {
        if (cur.size() == n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = cur.get(i);
            ans.add(a);
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (used[i]) continue;
            if (!cur.isEmpty() && (cur.get(cur.size() - 1) % 2 == i % 2)) continue;
            used[i] = true;
            cur.add(i);
            dfs(n, used, cur, ans);
            cur.remove(cur.size() - 1);
            used[i] = false;
        }
    }
}

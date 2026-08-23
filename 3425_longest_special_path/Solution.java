// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private List<int[]>[] g;
    private int[] nums;
    private int bestLen, bestNodes;
    private final Map<Integer, Integer> last = new HashMap<>();

    public int[] longestSpecialPath(int[][] edges, int[] nums) {
        this.nums = nums;
        int n = nums.length;
        @SuppressWarnings("unchecked")
        List<int[]>[] gg = new ArrayList[n];
        g = gg;
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(new int[]{e[1], e[2]});
            g[e[1]].add(new int[]{e[0], e[2]});
        }
        bestLen = 0;
        bestNodes = 1;
        last.clear();
        List<Integer> path = new ArrayList<>();
        dfs(0, -1, 0, 0, path);
        return new int[]{bestLen, bestNodes};
    }

    private void dfs(int u, int p, int dist, int left, List<Integer> path) {
        int prevPos = -1;
        boolean seen = last.containsKey(nums[u]);
        if (seen) prevPos = last.get(nums[u]);
        last.put(nums[u], path.size());
        int newLeft = left;
        if (seen && prevPos >= left) newLeft = prevPos + 1;
        path.add(dist);
        int length = dist - path.get(newLeft);
        int nodes = path.size() - newLeft;
        if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
            bestLen = length;
            bestNodes = nodes;
        }
        for (int[] e : g[u]) {
            if (e[0] == p) continue;
            dfs(e[0], u, dist + e[1], newLeft, path);
        }
        path.remove(path.size() - 1);
        if (seen) last.put(nums[u], prevPos);
        else last.remove(nums[u]);
    }
}

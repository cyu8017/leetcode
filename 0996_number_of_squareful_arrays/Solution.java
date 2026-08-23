// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

import java.util.*;

class Solution {
    private int ans;
    private Map<Integer, Integer> count;
    private Map<Integer, List<Integer>> graph;

    public int numSquarefulPerms(int[] nums) {
        count = new HashMap<>();
        for (int x : nums) count.merge(x, 1, Integer::sum);
        graph = new HashMap<>();
        for (int a : count.keySet()) graph.put(a, new ArrayList<>());
        for (int a : count.keySet()) {
            for (int b : count.keySet()) {
                long s = (long) a + b;
                long r = Math.round(Math.sqrt(s));
                if (r * r == s) graph.get(a).add(b);
            }
        }
        ans = 0;
        for (int x : new ArrayList<>(count.keySet())) {
            count.put(x, count.get(x) - 1);
            dfs(x, nums.length - 1);
            count.put(x, count.get(x) + 1);
        }
        return ans;
    }

    private void dfs(int x, int remain) {
        if (remain == 0) { ans++; return; }
        for (int y : graph.get(x)) {
            if (count.get(y) > 0) {
                count.put(y, count.get(y) - 1);
                dfs(y, remain - 1);
                count.put(y, count.get(y) + 1);
            }
        }
    }
}

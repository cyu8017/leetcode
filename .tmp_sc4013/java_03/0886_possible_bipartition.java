// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

import java.util.*;

class Solution {
    public boolean possibleBipartition(int n, int[][] dislikes) {
        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new ArrayList<>();
        for (int[] e : dislikes) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        Map<Integer, Integer> color = new HashMap<>();
        for (int start = 1; start <= n; start++) {
            if (color.containsKey(start)) continue;
            Queue<Integer> queue = new ArrayDeque<>();
            queue.offer(start);
            color.put(start, 0);
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int nei : graph[node]) {
                    if (!color.containsKey(nei)) {
                        color.put(nei, color.get(node) ^ 1);
                        queue.offer(nei);
                    } else if (color.get(nei).intValue() == color.get(node).intValue()) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}

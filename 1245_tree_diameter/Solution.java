// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

import java.util.*;

class Solution {
    public int treeDiameter(int[][] edges) {
        if (edges.length == 0) return 0;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] e : edges) {
            graph.computeIfAbsent(e[0], k -> new ArrayList<>()).add(e[1]);
            graph.computeIfAbsent(e[1], k -> new ArrayList<>()).add(e[0]);
        }
        int[] first = farthest(edges[0][0], graph);
        return farthest(first[0], graph)[1];
    }

    private int[] farthest(int start, Map<Integer, List<Integer>> graph) {
        Deque<int[]> q = new ArrayDeque<>();
        Set<Integer> seen = new HashSet<>();
        q.offer(new int[]{start, 0});
        seen.add(start);
        int[] last = new int[]{start, 0};
        while (!q.isEmpty()) {
            last = q.poll();
            for (int v : graph.getOrDefault(last[0], List.of())) {
                if (seen.add(v)) q.offer(new int[]{v, last[1] + 1});
            }
        }
        return last;
    }
}


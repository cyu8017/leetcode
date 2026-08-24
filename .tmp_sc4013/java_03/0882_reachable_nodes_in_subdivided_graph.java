// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

import java.util.*;

class Solution {
    public int reachableNodes(int[][] edges, int maxMoves, int n) {
        List<Map<Integer, Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new HashMap<>());
        for (int[] e : edges) {
            graph.get(e[0]).put(e[1], e[2]);
            graph.get(e[1]).put(e[0], e[2]);
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        pq.offer(new int[] {maxMoves, 0});
        Map<Integer, Integer> seen = new HashMap<>();
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int moves = cur[0], node = cur[1];
            if (seen.containsKey(node)) continue;
            seen.put(node, moves);
            for (Map.Entry<Integer, Integer> kv : graph.get(node).entrySet()) {
                int remain = moves - kv.getValue() - 1;
                if (!seen.containsKey(kv.getKey()) && remain >= 0) {
                    pq.offer(new int[] {remain, kv.getKey()});
                }
            }
        }
        int ans = seen.size();
        for (int[] e : edges) {
            int left = seen.getOrDefault(e[0], 0);
            int right = seen.getOrDefault(e[1], 0);
            ans += Math.min(e[2], left + right);
        }
        return ans;
    }
}

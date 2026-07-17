// LeetCode 1722 - Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private int[] parent;

    public int minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        int n = source.length;
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        for (int[] swap : allowedSwaps) {
            union(swap[0], swap[1]);
        }
        Map<Integer, Map<Integer, Integer>> groups = new HashMap<>();
        for (int i = 0; i < n; i++) {
            Map<Integer, Integer> counts = groups.computeIfAbsent(find(i), key -> new HashMap<>());
            counts.merge(source[i], 1, Integer::sum);
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            Map<Integer, Integer> counts = groups.get(find(i));
            int remaining = counts.getOrDefault(target[i], 0);
            if (remaining > 0) {
                counts.put(target[i], remaining - 1);
            } else {
                ans++;
            }
        }
        return ans;
    }

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void union(int a, int b) {
        int ra = find(a);
        int rb = find(b);
        if (ra != rb) {
            parent[rb] = ra;
        }
    }
}

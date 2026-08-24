// CONFIG class=Solution method=maxSubtreeInversionSum types=None
// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public long maxSubtreeInversionSum(int[][] edges, int[] nums, int k) {
        int n = nums.length;
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }
        int[] parent = new int[n];
        Arrays.fill(parent, -2);
        parent[0] = -1;
        List<Integer> order = new ArrayList<>();
        order.add(0);
        for (int i = 0; i < order.size(); i++) {
            int u = order.get(i);
            for (int v : graph[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    order.add(v);
                }
            }
        }
        final long infinity = 1L << 60;
        long[][] maximum = new long[n][];
        long[][] minimum = new long[n][];
        for (int oi = n - 1; oi >= 0; oi--) {
            int u = order.get(oi);
            long[] currentMax = new long[k + 1];
            long[] currentMin = new long[k + 1];
            Arrays.fill(currentMax, -infinity);
            Arrays.fill(currentMin, infinity);
            currentMax[k] = currentMin[k] = nums[u];
            for (int v : graph[u]) {
                if (parent[v] != u) continue;
                long[] nextMax = new long[k + 1];
                long[] nextMin = new long[k + 1];
                Arrays.fill(nextMax, -infinity);
                Arrays.fill(nextMin, infinity);
                for (int first = 0; first <= k; first++) {
                    if (currentMax[first] == -infinity) continue;
                    for (int childDistance = 0; childDistance <= k; childDistance++) {
                        if (maximum[v][childDistance] == -infinity) continue;
                        int second = childDistance + 1;
                        if (second > k) second = k;
                        if (first < k && second < k && first + second < k) continue;
                        int distance = Math.min(first, second);
                        long maxValue = currentMax[first] + maximum[v][childDistance];
                        long minValue = currentMin[first] + minimum[v][childDistance];
                        nextMax[distance] = Math.max(nextMax[distance], maxValue);
                        nextMin[distance] = Math.min(nextMin[distance], minValue);
                    }
                }
                currentMax = nextMax;
                currentMin = nextMin;
            }
            if (-currentMin[k] > currentMax[0]) currentMax[0] = -currentMin[k];
            if (-currentMax[k] < currentMin[0]) currentMin[0] = -currentMax[k];
            maximum[u] = currentMax;
            minimum[u] = currentMin;
        }
        long answer = -(1L << 60);
        for (long value : maximum[0]) answer = Math.max(answer, value);
        return answer;
    }
}

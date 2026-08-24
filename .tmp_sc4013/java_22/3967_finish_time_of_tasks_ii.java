// CONFIG class=Solution method=minFinishTime types=None
// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    static class Edge {
        int to, reverse;
        Edge(int to, int reverse) { this.to = to; this.reverse = reverse; }
    }

    private static long combine(long minimum, long maximum, int count, int base) {
        if (count == 0) return base;
        return 2 * maximum - minimum + base;
    }

    public long minFinishTime(int n, int[][] edges, int[] baseTime) {
        List<Edge>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            int iu = graph[u].size(), iv = graph[v].size();
            graph[u].add(new Edge(v, iv));
            graph[v].add(new Edge(u, iu));
        }
        int[] parent = new int[n], parentEdge = new int[n];
        Arrays.fill(parent, -2);
        parent[0] = -1;
        List<Integer> order = new ArrayList<>();
        order.add(0);
        for (int i = 0; i < order.size(); i++) {
            int u = order.get(i);
            for (Edge edge : graph[u]) {
                if (parent[edge.to] == -2) {
                    parent[edge.to] = u;
                    parentEdge[edge.to] = edge.reverse;
                    order.add(edge.to);
                }
            }
        }
        long[][] incoming = new long[n][];
        for (int i = 0; i < n; i++) incoming[i] = new long[graph[i].size()];
        for (int oi = n - 1; oi > 0; oi--) {
            int u = order.get(oi);
            long minimum = 1L << 62, maximum = -1;
            int count = 0;
            for (int edgeIndex = 0; edgeIndex < incoming[u].length; edgeIndex++) {
                if (edgeIndex == parentEdge[u]) continue;
                long value = incoming[u][edgeIndex];
                minimum = Math.min(minimum, value);
                maximum = Math.max(maximum, value);
                count++;
            }
            long value = combine(minimum, maximum, count, baseTime[u]);
            int parentNode = parent[u];
            int reverseIndex = graph[u].get(parentEdge[u]).reverse;
            incoming[parentNode][reverseIndex] = value;
        }
        long answer = 1L << 62;
        for (int u : order) {
            long min1 = 1L << 62, min2 = 1L << 62;
            int minIndex = -1;
            long max1 = -1, max2 = -1;
            int maxIndex = -1;
            for (int i = 0; i < incoming[u].length; i++) {
                long value = incoming[u][i];
                if (value < min1) {
                    min2 = min1;
                    min1 = value;
                    minIndex = i;
                } else if (value < min2) min2 = value;
                if (value > max1) {
                    max2 = max1;
                    max1 = value;
                    maxIndex = i;
                } else if (value > max2) max2 = value;
            }
            long rootValue = combine(min1, max1, graph[u].size(), baseTime[u]);
            answer = Math.min(answer, rootValue);
            for (int i = 0; i < graph[u].size(); i++) {
                Edge edge = graph[u].get(i);
                if (edge.to == parent[u]) continue;
                if (graph[u].size() == 1) {
                    incoming[edge.to][edge.reverse] = baseTime[u];
                    continue;
                }
                long minimum = min1, maximum = max1;
                if (i == minIndex) minimum = min2;
                if (i == maxIndex) maximum = max2;
                incoming[edge.to][edge.reverse] = combine(minimum, maximum, graph[u].size() - 1, baseTime[u]);
            }
        }
        return answer;
    }
}

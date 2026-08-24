// CONFIG class=Solution method=minMoves types=None
// LeetCode 4004 - Minimum Moves to Balance Circular Array II
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;

class Solution {
    private static final int INF = 1000000000;

    static class Edge {
        int to, cap, cost, rev;
        Edge(int to, int cap, int cost, int rev) {
            this.to = to; this.cap = cap; this.cost = cost; this.rev = rev;
        }
    }

    static class MinCostMaxFlow {
        int n;
        List<Edge>[] graph;

        @SuppressWarnings("unchecked")
        MinCostMaxFlow(int n_) {
            n = n_;
            graph = new ArrayList[n];
            for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        }

        void addEdge(int u, int v, int cap, int cost) {
            graph[u].add(new Edge(v, cap, cost, graph[v].size()));
            graph[v].add(new Edge(u, 0, -cost, graph[u].size() - 1));
        }

        long minCostFlow(int source, int sink, int maxFlow) {
            long totalCost = 0;
            int currentFlow = 0;
            while (currentFlow < maxFlow) {
                int[] dist = new int[n], parentNode = new int[n], parentEdge = new int[n];
                boolean[] inQueue = new boolean[n];
                Arrays.fill(dist, INF);
                Arrays.fill(parentNode, -1);
                Arrays.fill(parentEdge, -1);
                Deque<Integer> q = new ArrayDeque<>();
                q.add(source);
                dist[source] = 0;
                inQueue[source] = true;
                while (!q.isEmpty()) {
                    int u = q.poll();
                    inQueue[u] = false;
                    for (int i = 0; i < graph[u].size(); i++) {
                        Edge e = graph[u].get(i);
                        if (e.cap > 0 && dist[e.to] > dist[u] + e.cost) {
                            dist[e.to] = dist[u] + e.cost;
                            parentNode[e.to] = u;
                            parentEdge[e.to] = i;
                            if (!inQueue[e.to]) {
                                inQueue[e.to] = true;
                                q.add(e.to);
                            }
                        }
                    }
                }
                if (dist[sink] == INF) return -1;
                int pushFlow = maxFlow - currentFlow;
                for (int cur = sink; cur != source; cur = parentNode[cur]) {
                    Edge e = graph[parentNode[cur]].get(parentEdge[cur]);
                    if (e.cap < pushFlow) pushFlow = e.cap;
                }
                for (int cur = sink; cur != source; cur = parentNode[cur]) {
                    int p = parentNode[cur];
                    int idx = parentEdge[cur];
                    int rev = graph[p].get(idx).rev;
                    graph[p].get(idx).cap -= pushFlow;
                    graph[cur].get(rev).cap += pushFlow;
                }
                currentFlow += pushFlow;
                totalCost += (long) pushFlow * dist[sink];
            }
            return totalCost;
        }
    }

    public long minMoves(int[] balance) {
        int totalBalance = 0, totalDeficit = 0;
        for (int x : balance) {
            totalBalance += x;
            if (x < 0) totalDeficit += -x;
        }
        if (totalBalance < 0) return -1;
        if (totalDeficit == 0) return 0;
        int n = balance.length;
        int source = n, sink = n + 1;
        MinCostMaxFlow mcmf = new MinCostMaxFlow(n + 2);
        for (int i = 0; i < n; i++) {
            int x = balance[i];
            if (x > 0) mcmf.addEdge(source, i, x, 0);
            else if (x < 0) mcmf.addEdge(i, sink, -x, 0);
            mcmf.addEdge(i, (i + 1) % n, INF, 1);
            mcmf.addEdge(i, (i - 1 + n) % n, INF, 1);
        }
        return mcmf.minCostFlow(source, sink, totalDeficit);
    }
}

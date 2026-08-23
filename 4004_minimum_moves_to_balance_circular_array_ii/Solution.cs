// LeetCode 4004 - Minimum Moves to Balance Circular Array II
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

using System.Collections.Generic;

public class Solution {
    const int INF = 1000000000;

    class Edge {
        public int To, Cap, Cost, Rev;
        public Edge(int to, int cap, int cost, int rev) {
            To = to; Cap = cap; Cost = cost; Rev = rev;
        }
    }

    class MinCostMaxFlow {
        public int N;
        public List<Edge>[] Graph;
        public MinCostMaxFlow(int n) {
            N = n;
            Graph = new List<Edge>[n];
            for (int i = 0; i < n; i++) Graph[i] = new List<Edge>();
        }
        public void AddEdge(int u, int v, int cap, int cost) {
            Graph[u].Add(new Edge(v, cap, cost, Graph[v].Count));
            Graph[v].Add(new Edge(u, 0, -cost, Graph[u].Count - 1));
        }
        public long MinCostFlow(int source, int sink, int maxFlow) {
            long totalCost = 0;
            int currentFlow = 0;
            while (currentFlow < maxFlow) {
                int[] dist = new int[N], parentNode = new int[N], parentEdge = new int[N];
                bool[] inQueue = new bool[N];
                for (int i = 0; i < N; i++) { dist[i] = INF; parentNode[i] = -1; parentEdge[i] = -1; }
                var q = new Queue<int>();
                q.Enqueue(source);
                dist[source] = 0;
                inQueue[source] = true;
                while (q.Count > 0) {
                    int u = q.Dequeue();
                    inQueue[u] = false;
                    for (int i = 0; i < Graph[u].Count; i++) {
                        Edge e = Graph[u][i];
                        if (e.Cap > 0 && dist[e.To] > dist[u] + e.Cost) {
                            dist[e.To] = dist[u] + e.Cost;
                            parentNode[e.To] = u;
                            parentEdge[e.To] = i;
                            if (!inQueue[e.To]) {
                                inQueue[e.To] = true;
                                q.Enqueue(e.To);
                            }
                        }
                    }
                }
                if (dist[sink] == INF) return -1;
                int pushFlow = maxFlow - currentFlow;
                for (int cur = sink; cur != source; cur = parentNode[cur]) {
                    Edge e = Graph[parentNode[cur]][parentEdge[cur]];
                    if (e.Cap < pushFlow) pushFlow = e.Cap;
                }
                for (int cur = sink; cur != source; cur = parentNode[cur]) {
                    int p = parentNode[cur];
                    int idx = parentEdge[cur];
                    int rev = Graph[p][idx].Rev;
                    Graph[p][idx].Cap -= pushFlow;
                    Graph[cur][rev].Cap += pushFlow;
                }
                currentFlow += pushFlow;
                totalCost += (long)pushFlow * dist[sink];
            }
            return totalCost;
        }
    }

    public long MinMoves(int[] balance) {
        int totalBalance = 0, totalDeficit = 0;
        foreach (int x in balance) {
            totalBalance += x;
            if (x < 0) totalDeficit += -x;
        }
        if (totalBalance < 0) return -1;
        if (totalDeficit == 0) return 0;
        int n = balance.Length;
        int source = n, sink = n + 1;
        var mcmf = new MinCostMaxFlow(n + 2);
        for (int i = 0; i < n; i++) {
            int x = balance[i];
            if (x > 0) mcmf.AddEdge(source, i, x, 0);
            else if (x < 0) mcmf.AddEdge(i, sink, -x, 0);
            mcmf.AddEdge(i, (i + 1) % n, INF, 1);
            mcmf.AddEdge(i, (i - 1 + n) % n, INF, 1);
        }
        return mcmf.MinCostFlow(source, sink, totalDeficit);
    }
}

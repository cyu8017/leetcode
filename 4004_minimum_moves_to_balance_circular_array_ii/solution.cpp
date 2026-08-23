// LeetCode 4004 - Minimum Moves to Balance Circular Array II
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

#include <cstdint>
#include <queue>
#include <vector>

class Solution {
    static constexpr int INF = 1000000000;

    struct Edge {
        int to, cap, cost, rev;
    };

    struct MinCostMaxFlow {
        int n;
        std::vector<std::vector<Edge>> graph;

        explicit MinCostMaxFlow(int n_) : n(n_), graph(n_) {}

        void addEdge(int u, int v, int cap, int cost) {
            graph[u].push_back({v, cap, cost, (int)graph[v].size()});
            graph[v].push_back({u, 0, -cost, (int)graph[u].size() - 1});
        }

        int64_t minCostFlow(int source, int sink, int maxFlow) {
            int64_t totalCost = 0;
            int currentFlow = 0;

            while (currentFlow < maxFlow) {
                std::vector<int> dist(n, INF), parentNode(n, -1), parentEdge(n, -1);
                std::vector<char> inQueue(n, 0);
                std::queue<int> q;
                q.push(source);
                dist[source] = 0;
                inQueue[source] = 1;

                while (!q.empty()) {
                    int u = q.front();
                    q.pop();
                    inQueue[u] = 0;
                    for (int i = 0; i < (int)graph[u].size(); i++) {
                        Edge& e = graph[u][i];
                        if (e.cap > 0 && dist[e.to] > dist[u] + e.cost) {
                            dist[e.to] = dist[u] + e.cost;
                            parentNode[e.to] = u;
                            parentEdge[e.to] = i;
                            if (!inQueue[e.to]) {
                                inQueue[e.to] = 1;
                                q.push(e.to);
                            }
                        }
                    }
                }

                if (dist[sink] == INF) return -1;

                int pushFlow = maxFlow - currentFlow;
                for (int cur = sink; cur != source; cur = parentNode[cur]) {
                    Edge& e = graph[parentNode[cur]][parentEdge[cur]];
                    if (e.cap < pushFlow) pushFlow = e.cap;
                }
                for (int cur = sink; cur != source; cur = parentNode[cur]) {
                    int p = parentNode[cur];
                    int idx = parentEdge[cur];
                    int rev = graph[p][idx].rev;
                    graph[p][idx].cap -= pushFlow;
                    graph[cur][rev].cap += pushFlow;
                }
                currentFlow += pushFlow;
                totalCost += (int64_t)pushFlow * dist[sink];
            }
            return totalCost;
        }
    };

public:
    long long minMoves(std::vector<int>& balance) {
        int totalBalance = 0, totalDeficit = 0;
        for (int x : balance) {
            totalBalance += x;
            if (x < 0) totalDeficit += -x;
        }
        if (totalBalance < 0) return -1;
        if (totalDeficit == 0) return 0;

        int n = (int)balance.size();
        int source = n, sink = n + 1;
        MinCostMaxFlow mcmf(n + 2);

        for (int i = 0; i < n; i++) {
            int x = balance[i];
            if (x > 0) mcmf.addEdge(source, i, x, 0);
            else if (x < 0) mcmf.addEdge(i, sink, -x, 0);
            mcmf.addEdge(i, (i + 1) % n, INF, 1);
            mcmf.addEdge(i, (i - 1 + n) % n, INF, 1);
        }
        return mcmf.minCostFlow(source, sink, totalDeficit);
    }
};

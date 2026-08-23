// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/

#include <algorithm>
#include <vector>

class Solution {
    struct Edge {
        int to, reverse;
    };

    static long long combine(long long minimum, long long maximum, int count, int base) {
        if (count == 0) return base;
        return 2 * maximum - minimum + base;
    }

public:
    long long minFinishTime(int n, std::vector<std::vector<int>>& edges, std::vector<int>& baseTime) {
        std::vector<std::vector<Edge>> graph(n);
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            int iu = (int)graph[u].size(), iv = (int)graph[v].size();
            graph[u].push_back({v, iv});
            graph[v].push_back({u, iu});
        }
        std::vector<int> parent(n, -2), parentEdge(n, 0);
        parent[0] = -1;
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (auto& edge : graph[u]) {
                if (parent[edge.to] == -2) {
                    parent[edge.to] = u;
                    parentEdge[edge.to] = edge.reverse;
                    order.push_back(edge.to);
                }
            }
        }
        std::vector<std::vector<long long>> incoming(n);
        for (int i = 0; i < n; i++) incoming[i].assign(graph[i].size(), 0);
        for (int oi = n - 1; oi > 0; oi--) {
            int u = order[oi];
            long long minimum = 1LL << 62, maximum = -1;
            int count = 0;
            for (int edgeIndex = 0; edgeIndex < (int)incoming[u].size(); edgeIndex++) {
                if (edgeIndex == parentEdge[u]) continue;
                long long value = incoming[u][edgeIndex];
                minimum = std::min(minimum, value);
                maximum = std::max(maximum, value);
                count++;
            }
            long long value = combine(minimum, maximum, count, baseTime[u]);
            int parentNode = parent[u];
            int reverseIndex = graph[u][parentEdge[u]].reverse;
            incoming[parentNode][reverseIndex] = value;
        }
        long long answer = 1LL << 62;
        for (int u : order) {
            long long min1 = 1LL << 62, min2 = 1LL << 62;
            int minIndex = -1;
            long long max1 = -1, max2 = -1;
            int maxIndex = -1;
            for (int i = 0; i < (int)incoming[u].size(); i++) {
                long long value = incoming[u][i];
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
            long long rootValue = combine(min1, max1, (int)graph[u].size(), baseTime[u]);
            answer = std::min(answer, rootValue);
            for (int i = 0; i < (int)graph[u].size(); i++) {
                auto& edge = graph[u][i];
                if (edge.to == parent[u]) continue;
                if ((int)graph[u].size() == 1) {
                    incoming[edge.to][edge.reverse] = baseTime[u];
                    continue;
                }
                long long minimum = min1, maximum = max1;
                if (i == minIndex) minimum = min2;
                if (i == maxIndex) maximum = max2;
                incoming[edge.to][edge.reverse] = combine(minimum, maximum, (int)graph[u].size() - 1, baseTime[u]);
            }
        }
        return answer;
    }
};

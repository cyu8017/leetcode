// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxSubtreeInversionSum(std::vector<std::vector<int>>& edges, std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<std::vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        std::vector<int> parent(n, -2);
        parent[0] = -1;
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (int v : graph[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    order.push_back(v);
                }
            }
        }
        const long long infinity = 1LL << 60;
        std::vector<std::vector<long long>> maximum(n), minimum(n);
        for (int oi = n - 1; oi >= 0; oi--) {
            int u = order[oi];
            std::vector<long long> currentMax(k + 1, -infinity), currentMin(k + 1, infinity);
            currentMax[k] = currentMin[k] = nums[u];
            for (int v : graph[u]) {
                if (parent[v] != u) continue;
                std::vector<long long> nextMax(k + 1, -infinity), nextMin(k + 1, infinity);
                for (int first = 0; first <= k; first++) {
                    if (currentMax[first] == -infinity) continue;
                    for (int childDistance = 0; childDistance <= k; childDistance++) {
                        if (maximum[v][childDistance] == -infinity) continue;
                        int second = childDistance + 1;
                        if (second > k) second = k;
                        if (first < k && second < k && first + second < k) continue;
                        int distance = std::min(first, second);
                        long long maxValue = currentMax[first] + maximum[v][childDistance];
                        long long minValue = currentMin[first] + minimum[v][childDistance];
                        nextMax[distance] = std::max(nextMax[distance], maxValue);
                        nextMin[distance] = std::min(nextMin[distance], minValue);
                    }
                }
                currentMax.swap(nextMax);
                currentMin.swap(nextMin);
            }
            if (-currentMin[k] > currentMax[0]) currentMax[0] = -currentMin[k];
            if (-currentMax[k] < currentMin[0]) currentMin[0] = -currentMax[k];
            maximum[u] = currentMax;
            minimum[u] = currentMin;
        }
        long long answer = -(1LL << 60);
        for (long long value : maximum[0]) answer = std::max(answer, value);
        return answer;
    }
};

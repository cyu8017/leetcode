// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

#include <algorithm>
#include <queue>
#include <string>
#include <vector>

class Solution {
public:
    int largestPathValue(std::string colors, std::vector<std::vector<int>>& edges) {
        int n = static_cast<int>(colors.size());
        std::vector<int> indegree(n, 0);
        std::vector<std::vector<int>> adjacency(n);
        for (const auto& edge : edges) {
            adjacency[edge[0]].push_back(edge[1]);
            indegree[edge[1]]++;
        }

        std::queue<int> queue;
        for (int node = 0; node < n; node++) {
            if (indegree[node] == 0) {
                queue.push(node);
            }
        }

        std::vector<std::vector<int>> dp(n, std::vector<int>(26, 0));
        for (int node = 0; node < n; node++) {
            dp[node][colors[node] - 'a'] = 1;
        }

        int processed = 0;
        int answer = 0;
        while (!queue.empty()) {
            int node = queue.front();
            queue.pop();
            processed++;
            answer = std::max(answer, *std::max_element(dp[node].begin(), dp[node].end()));

            for (int neighbor : adjacency[node]) {
                int neighborColor = colors[neighbor] - 'a';
                for (int colorIndex = 0; colorIndex < 26; colorIndex++) {
                    int candidate = dp[node][colorIndex] + (colorIndex == neighborColor ? 1 : 0);
                    if (candidate > dp[neighbor][colorIndex]) {
                        dp[neighbor][colorIndex] = candidate;
                    }
                }
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    queue.push(neighbor);
                }
            }
        }
        return processed == n ? answer : -1;
    }
};

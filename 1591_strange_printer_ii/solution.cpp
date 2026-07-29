// LeetCode 1591 - Strange Printer II
// https://leetcode.com/problems/strange-printer-ii/

#include <algorithm>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool isPrintable(std::vector<std::vector<int>>& targetGrid) {
        std::unordered_set<int> colors;
        for (const auto& row : targetGrid) {
            for (int x : row) {
                colors.insert(x);
            }
        }
        std::unordered_map<int, std::vector<int>> bounds;
        for (int c : colors) {
            bounds[c] = {1000000000, 1000000000, -1, -1};
        }
        for (int r = 0; r < static_cast<int>(targetGrid.size()); ++r) {
            for (int col = 0; col < static_cast<int>(targetGrid[r].size()); ++col) {
                const int c = targetGrid[r][col];
                auto& b = bounds[c];
                b[0] = std::min(b[0], r);
                b[1] = std::min(b[1], col);
                b[2] = std::max(b[2], r);
                b[3] = std::max(b[3], col);
            }
        }
        std::unordered_map<int, std::unordered_set<int>> graph;
        std::unordered_map<int, int> indegree;
        for (int c : colors) {
            indegree[c] = 0;
        }
        for (const auto& [c, b] : bounds) {
            const int r1 = b[0], c1 = b[1], r2 = b[2], c2 = b[3];
            for (int r = r1; r <= r2; ++r) {
                for (int col = c1; col <= c2; ++col) {
                    const int other = targetGrid[r][col];
                    if (other != c && !graph[c].count(other)) {
                        graph[c].insert(other);
                        indegree[other] += 1;
                    }
                }
            }
        }
        std::queue<int> queue;
        for (int c : colors) {
            if (indegree[c] == 0) {
                queue.push(c);
            }
        }
        int seen = 0;
        while (!queue.empty()) {
            const int c = queue.front();
            queue.pop();
            ++seen;
            for (int nxt : graph[c]) {
                if (--indegree[nxt] == 0) {
                    queue.push(nxt);
                }
            }
        }
        return seen == static_cast<int>(colors.size());
    }
};

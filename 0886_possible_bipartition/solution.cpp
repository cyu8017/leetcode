// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
public:
    bool possibleBipartition(int n, std::vector<std::vector<int>>& dislikes) {
        std::vector<std::vector<int>> graph(n + 1);
        for (auto& e : dislikes) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        std::unordered_map<int, int> color;
        for (int start = 1; start <= n; ++start) {
            if (color.count(start)) {
                continue;
            }
            std::queue<int> queue;
            queue.push(start);
            color[start] = 0;
            while (!queue.empty()) {
                int node = queue.front();
                queue.pop();
                for (int nei : graph[node]) {
                    if (!color.count(nei)) {
                        color[nei] = color[node] ^ 1;
                        queue.push(nei);
                    } else if (color[nei] == color[node]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
};

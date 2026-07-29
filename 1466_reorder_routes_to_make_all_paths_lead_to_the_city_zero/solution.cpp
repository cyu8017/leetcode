#include <unordered_set>
#include <vector>
#include <utility>

class Solution {
public:
    int minReorder(int n, std::vector<std::vector<int>>& connections) {
        std::vector<std::vector<std::pair<int,int>>> graph(n);
        for (auto& e : connections) {
            graph[e[0]].push_back({e[1], 1});
            graph[e[1]].push_back({e[0], 0});
        }
        int ans = 0;
        std::vector<int> stack{0};
        std::unordered_set<int> seen{0};
        while (!stack.empty()) {
            int node = stack.back(); stack.pop_back();
            for (auto [nei, cost] : graph[node]) {
                if (!seen.count(nei)) {
                    seen.insert(nei);
                    stack.push_back(nei);
                    ans += cost;
                }
            }
        }
        return ans;
    }
};

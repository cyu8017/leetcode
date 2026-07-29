// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    std::vector<int> shortestAlternatingPaths(int n, std::vector<std::vector<int>>& redEdges,
                                              std::vector<std::vector<int>>& blueEdges) {
        std::vector<std::vector<int>> red(n), blue(n);
        for (const auto& e : redEdges) red[e[0]].push_back(e[1]);
        for (const auto& e : blueEdges) blue[e[0]].push_back(e[1]);
        std::vector<int> ans(n, -1);
        std::vector<std::vector<bool>> seen(n, std::vector<bool>(2, false));
        std::queue<std::tuple<int, int, int>> q;
        q.emplace(0, 0, 0);
        q.emplace(0, 1, 0);
        seen[0][0] = seen[0][1] = true;
        while (!q.empty()) {
            auto [node, color, dist] = q.front();
            q.pop();
            if (ans[node] == -1) ans[node] = dist;
            const auto& nextEdges = color == 0 ? red[node] : blue[node];
            const int nextColor = 1 - color;
            for (int nxt : nextEdges) {
                if (!seen[nxt][nextColor]) {
                    seen[nxt][nextColor] = true;
                    q.emplace(nxt, nextColor, dist + 1);
                }
            }
        }
        return ans;
    }
};

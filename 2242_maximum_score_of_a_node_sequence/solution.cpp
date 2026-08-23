// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

#include <vector>

class Solution {
public:
    int maximumScore(std::vector<int>& scores, std::vector<std::vector<int>>& edges) {
        int n = (int)scores.size();
        std::vector<std::vector<int>> top(n), g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        for (int i = 0; i < n; ++i) {
            for (int v : g[i]) {
                top[i].push_back(v);
                for (int j = (int)top[i].size() - 1; j > 0; --j) {
                    if (scores[top[i][j]] > scores[top[i][j - 1]])
                        std::swap(top[i][j], top[i][j - 1]);
                }
                if ((int)top[i].size() > 3) top[i].resize(3);
            }
        }
        int ans = -1;
        for (auto& e : edges) {
            int a = e[0], b = e[1];
            for (int c : top[a]) {
                if (c == b) continue;
                for (int d : top[b]) {
                    if (d == a || d == c) continue;
                    ans = std::max(ans, scores[a] + scores[b] + scores[c] + scores[d]);
                }
            }
        }
        return ans;
    }
};

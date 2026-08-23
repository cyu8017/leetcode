// LeetCode 3249 - Count the Number of Good Nodes
// https://leetcode.com/problems/count-the-number-of-good-nodes/

#include <functional>
#include <vector>

class Solution {
public:
    int countGoodNodes(std::vector<std::vector<int>>& edges) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int ans = 0;
        std::function<int(int, int)> dfs = [&](int a, int fa) -> int {
            int pre = -1, cnt = 1, ok = 1;
            for (int b : g[a]) {
                if (b != fa) {
                    int cur = dfs(b, a);
                    cnt += cur;
                    if (pre < 0) pre = cur;
                    else if (pre != cur) ok = 0;
                }
            }
            ans += ok;
            return cnt;
        };
        dfs(0, -1);
        return ans;
    }
};

#include <algorithm>
#include <vector>

class Solution {
    std::vector<std::vector<int>> children;
    std::vector<int> informTime;
    int dfs(int u) {
        int best = 0;
        for (int v : children[u]) best = std::max(best, dfs(v));
        return informTime[u] + best;
    }
public:
    int numOfMinutes(int n, int headID, std::vector<int>& manager, std::vector<int>& informTime_) {
        children.assign(n, {});
        informTime = informTime_;
        for (int i = 0; i < n; ++i)
            if (manager[i] != -1) children[manager[i]].push_back(i);
        return dfs(headID);
    }
};

// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

#include <cstdlib>
#include <queue>
#include <vector>

class Solution {
public:
    std::vector<int> resultsArray(std::vector<std::vector<int>>& queries, int k) {
        std::priority_queue<int> h;
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int d = std::abs(queries[i][0]) + std::abs(queries[i][1]);
            h.push(d);
            if ((int)h.size() > k) h.pop();
            ans[i] = ((int)h.size() < k) ? -1 : h.top();
        }
        return ans;
    }
};

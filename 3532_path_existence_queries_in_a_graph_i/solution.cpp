// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

#include <vector>

class Solution {
public:
    std::vector<bool> pathExistenceQueries(int n, std::vector<int>& nums, int maxDiff, std::vector<std::vector<int>>& queries) {
        std::vector<int> g(n);
        int cnt = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] - nums[i - 1] > maxDiff) cnt++;
            g[i] = cnt;
        }
        std::vector<bool> ans;
        for (auto& q : queries) ans.push_back(g[q[0]] == g[q[1]]);
        return ans;
    }
};

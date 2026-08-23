// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

#include <vector>
#include <algorithm>
#include <array>

class Solution {
public:
    std::vector<int> pathExistenceQueries(int n, std::vector<int>& nums, int maxDiff, std::vector<std::vector<int>>& queries) {
        std::vector<std::array<int, 2>> pairs(n);
        for (int i = 0; i < n; i++) pairs[i] = {nums[i], i};
        std::sort(pairs.begin(), pairs.end());
        int m = 20;
        std::vector<std::vector<int>> f(n, std::vector<int>(m));
        int r = n - 1;
        for (int l = n - 1; l >= 0; l--) {
            while (pairs[r][0] - pairs[l][0] > maxDiff) r--;
            int i = pairs[l][1], j = pairs[r][1];
            f[i][0] = j;
            for (int k = 1; k < m; k++) f[i][k] = f[f[i][k - 1]][k - 1];
        }
        std::vector<int> ans;
        for (auto& q : queries) {
            int i = q[0], j = q[1];
            if (nums[i] > nums[j]) std::swap(i, j);
            if (i == j) { ans.push_back(0); continue; }
            if (nums[i] == nums[j]) { ans.push_back(1); continue; }
            int d = 0;
            for (int k = m - 1; k >= 0; k--) {
                if (nums[f[i][k]] < nums[j]) {
                    d |= 1 << k;
                    i = f[i][k];
                }
            }
            if (nums[f[i][0]] < nums[j]) ans.push_back(-1);
            else ans.push_back(d + 1);
        }
        return ans;
    }
};

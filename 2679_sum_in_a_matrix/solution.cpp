// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

#include <vector>
#include <algorithm>

class Solution {
public:
    int matrixSum(std::vector<std::vector<int>>& nums) {
        for (auto& row : nums) std::sort(row.begin(), row.end());
        int ans = 0, n = (int)nums[0].size();
        for (int j = 0; j < n; j++) {
            int mx = 0;
            for (auto& row : nums) mx = std::max(mx, row[j]);
            ans += mx;
        }
        return ans;
    }
};

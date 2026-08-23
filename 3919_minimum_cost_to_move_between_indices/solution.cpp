// LeetCode 3919 - Minimum Cost To Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

#include <vector>

class Solution {
public:
    std::vector<int> minCost(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> s1(n, 0), s2(n, 0);
        for (int i = 1; i < n; i++) {
            int c1 = 1;
            if (i > 1 && nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1]) c1 = nums[i] - nums[i - 1];
            int c2 = 1;
            if (i < n - 1 && nums[i] - nums[i - 1] > nums[i + 1] - nums[i]) c2 = nums[i] - nums[i - 1];
            s1[i] = s1[i - 1] + c1;
            s2[i] = s2[i - 1] + c2;
        }
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int l = queries[i][0], r = queries[i][1];
            ans[i] = (l < r) ? (s1[r] - s1[l]) : (s2[l] - s2[r]);
        }
        return ans;
    }
};

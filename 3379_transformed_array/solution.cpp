// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

#include <vector>

class Solution {
public:
    std::vector<int> constructTransformedArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            int j = ((i + nums[i]) % n + n) % n;
            ans[i] = nums[j];
        }
        return ans;
    }
};

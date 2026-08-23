// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/

#include <vector>

class Solution {
public:
    long long countQuadruplets(std::vector<int>& nums) {
        int n = (int)nums.size();
        long long ans = 0;
        std::vector<int> great(n);
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < j; ++i) {
                if (nums[i] < nums[j]) ans += great[i];
                else if (nums[i] > nums[j]) great[i]++;
            }
        }
        return ans;
    }
};

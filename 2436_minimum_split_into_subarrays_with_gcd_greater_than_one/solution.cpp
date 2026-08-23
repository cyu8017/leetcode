// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

#include <numeric>
#include <vector>

class Solution {
public:
    int minimumSplits(std::vector<int>& nums) {
        int ans = 1;
        int g = nums[0];
        for (int i = 1; i < (int)nums.size(); i++) {
            int ng = std::gcd(g, nums[i]);
            if (ng == 1) {
                ans++;
                g = nums[i];
            } else {
                g = ng;
            }
        }
        return ans;
    }
};

// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

#include <vector>
#include <algorithm>

class Solution {
public:
    double minimumAverage(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        int ans = 1 << 30;
        for (int i = 0; i < n / 2; i++) ans = std::min(ans, nums[i] + nums[n - i - 1]);
        return ans / 2.0;
    }
};

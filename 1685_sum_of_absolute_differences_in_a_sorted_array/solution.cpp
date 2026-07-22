// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

#include <numeric>
#include <vector>

class Solution {
public:
    std::vector<int> getSumAbsoluteDifferences(std::vector<int>& nums) {
        long long total = std::accumulate(nums.begin(), nums.end(), 0LL);
        long long left = 0;
        int n = static_cast<int>(nums.size());
        std::vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            long long x = nums[i];
            ans[i] = static_cast<int>(x * i - left + (total - left - x) - x * (n - i - 1));
            left += x;
        }
        return ans;
    }
};

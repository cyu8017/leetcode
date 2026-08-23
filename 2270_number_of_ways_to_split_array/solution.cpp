// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

#include <vector>

class Solution {
public:
    int waysToSplitArray(std::vector<int>& nums) {
        long long total = 0;
        for (int v : nums) total += v;
        long long left = 0;
        int ans = 0;
        for (size_t i = 0; i + 1 < nums.size(); ++i) {
            left += nums[i];
            if (left >= total - left) ans++;
        }
        return ans;
    }
};

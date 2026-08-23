// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxProduct(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        long long a = nums[0], b = nums[1], c = nums[n - 2], d = nums[n - 1];
        const long long x = 100000;
        return std::max({a * b * x, c * d * x, -a * d * x});
    }
};

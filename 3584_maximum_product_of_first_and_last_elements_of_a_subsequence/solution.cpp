// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long maximumProduct(std::vector<int>& nums, int m) {
        long long ans = LLONG_MIN;
        int mx = INT_MIN, mi = INT_MAX;
        for (int i = m - 1; i < (int)nums.size(); i++) {
            int x = nums[i], y = nums[i - m + 1];
            mi = std::min(mi, y);
            mx = std::max(mx, y);
            ans = std::max(ans, std::max(1LL * x * mi, 1LL * x * mx));
        }
        return ans;
    }
};

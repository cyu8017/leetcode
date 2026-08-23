// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minRemoval(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size(), cnt = 0;
        for (int i = 0; i < n; i++) {
            int j = n;
            if (1LL * nums[i] * k <= nums[n - 1]) {
                long long target = 1LL * nums[i] * k + 1;
                j = (int)(std::lower_bound(nums.begin(), nums.end(), target) - nums.begin());
            }
            cnt = std::max(cnt, j - i);
        }
        return n - cnt;
    }
};

// LeetCode 3788 - Maximum Score Of A Split
// https://leetcode.com/problems/maximum-score-of-a-split/

#include <algorithm>
#include <cstdint>
#include <limits>
#include <vector>

class Solution {
public:
    long long maximumScore(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int64_t> suf(n);
        suf[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) suf[i] = std::min((int64_t)nums[i], suf[i + 1]);
        int64_t pre = 0;
        int64_t ans = std::numeric_limits<int64_t>::min();
        for (int i = 0; i < n - 1; i++) {
            pre += nums[i];
            ans = std::max(ans, pre - suf[i + 1]);
        }
        return ans;
    }
};

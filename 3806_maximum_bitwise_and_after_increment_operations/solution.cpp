// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

#include <algorithm>
#include <vector>

class Solution {
    static int bitLen(unsigned x) {
        return x == 0 ? 0 : 32 - __builtin_clz(x);
    }

public:
    int maximumAND(std::vector<int>& nums, int k, int m) {
        int mxVal = *std::max_element(nums.begin(), nums.end()) + k;
        int mx = bitLen((unsigned)mxVal);
        int ans = 0;
        std::vector<int> cost(nums.size());
        for (int bit = mx - 1; bit >= 0; bit--) {
            int target = ans | (1 << bit);
            for (int i = 0; i < (int)nums.size(); i++) {
                int x = nums[i];
                int j = bitLen((unsigned)(target & ~x));
                int mask = (1 << j) - 1;
                cost[i] = (target & mask) - (x & mask);
            }
            std::sort(cost.begin(), cost.end());
            int sum = 0;
            for (int i = 0; i < m; i++) sum += cost[i];
            if (sum <= k) ans = target;
        }
        return ans;
    }
};

// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

#include <vector>
#include <map>
#include <array>
#include <algorithm>
#include <cstdlib>

class Solution {
    static const int MIN = -5000;
    std::map<std::array<int, 4>, int> memo;
    std::vector<int> nums;
    int limit;
    int dp(int i, int product, int state, int kk) {
        if (i == (int)nums.size()) {
            if (kk == 0 && state != 0 && product <= limit) return product;
            return MIN;
        }
        std::array<int, 4> key = {i, product, state, kk};
        if (memo.count(key)) return memo[key];
        int res = dp(i + 1, product, state, kk);
        if (state == 0) res = std::max(res, dp(i + 1, nums[i], 1, kk - nums[i]));
        if (state == 1) {
            int np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = std::max(res, dp(i + 1, np, 2, kk + nums[i]));
        }
        if (state == 2) {
            int np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = std::max(res, dp(i + 1, np, 1, kk - nums[i]));
        }
        return memo[key] = res;
    }
public:
    int maxProduct(std::vector<int>& nums_, int k, int limit_) {
        nums = nums_;
        limit = limit_;
        memo.clear();
        int sumAll = 0;
        for (int v : nums) sumAll += v;
        if (std::abs(k) > sumAll) return -1;
        int ans = dp(0, 1, 0, k);
        return ans == MIN ? -1 : ans;
    }
};

// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        long long ans = 1LL << 62;
        for (int i = 0; i + k <= n; i++) {
            std::vector<int> sub(nums.begin() + i, nums.begin() + i + k);
            std::sort(sub.begin(), sub.end());
            int med = sub[k / 2];
            long long cost = 0;
            for (int x : sub) cost += std::abs(x - med);
            if (cost < ans) ans = cost;
        }
        return ans;
    }
};

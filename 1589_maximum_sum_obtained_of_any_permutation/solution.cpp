// LeetCode 1589 - Maximum Sum Obtained of Any Permutation
// https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxSumRangeQuery(std::vector<int>& nums, std::vector<std::vector<int>>& requests) {
        const int MOD = 1000000007;
        const int n = static_cast<int>(nums.size());
        std::vector<long long> diff(n + 1, 0);
        for (const auto& req : requests) {
            diff[req[0]] += 1;
            diff[req[1] + 1] -= 1;
        }
        for (int i = 1; i < n; ++i) {
            diff[i] += diff[i - 1];
        }
        std::sort(nums.begin(), nums.end());
        std::sort(diff.begin(), diff.begin() + n);
        long long answer = 0;
        for (int i = 0; i < n; ++i) {
            answer = (answer + nums[i] * diff[i]) % MOD;
        }
        return static_cast<int>(answer);
    }
};

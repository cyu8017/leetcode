// LeetCode 0891 - Sum of Subsequence Widths
// https://leetcode.com/problems/sum-of-subsequence-widths/

#include <algorithm>
#include <vector>

class Solution {
public:
    int sumSubseqWidths(std::vector<int>& nums) {
        const int MOD = 1'000'000'007;
        std::sort(nums.begin(), nums.end());
        int n = static_cast<int>(nums.size());
        std::vector<long long> pow2(n, 1);
        for (int i = 1; i < n; ++i) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = (ans + nums[i] * (pow2[i] - pow2[n - 1 - i])) % MOD;
        }
        return static_cast<int>((ans + MOD) % MOD);
    }
};

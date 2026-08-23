// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

#include <vector>

class Solution {
public:
    int maxSum(std::vector<int>& nums, int k) {
        const int mod = 1000000007;
        std::vector<int> cnt(32);
        for (int v : nums)
            for (int b = 0; b < 32; b++)
                if (v & (1 << b)) cnt[b]++;
        int ans = 0;
        for (int i = 0; i < k; i++) {
            int cur = 0;
            for (int b = 0; b < 32; b++) {
                if (cnt[b] > 0) {
                    cur |= 1 << b;
                    cnt[b]--;
                }
            }
            ans = (ans + 1LL * (cur % mod) * (cur % mod) % mod) % mod;
        }
        return ans;
    }
};

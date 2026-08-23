// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int rangeSum(std::vector<int>& nums) {
        const int mod = 1000000007;
        std::unordered_map<int, int> cnt, sum;
        int ans = 0;
        for (int x : nums) {
            int cL = cnt[x - 1], sL = sum[x - 1];
            int cR = cnt[x + 1], sR = sum[x + 1];
            int c = (1 + cL + cR) % mod;
            int s = (int)(((long long)x + sL + (long long)cL * x % mod + sR + (long long)cR * x % mod) % mod);
            if (cL > 0 && cR > 0) {
                c = (c + (int)((long long)cL * cR % mod)) % mod;
                s = (int)((s + (long long)sL * cR % mod + (long long)sR * cL % mod + (long long)cL * cR % mod * x % mod) % mod);
            }
            cnt[x] = (cnt[x] + c) % mod;
            sum[x] = (sum[x] + s) % mod;
            ans = (ans + s) % mod;
        }
        return ans;
    }
};

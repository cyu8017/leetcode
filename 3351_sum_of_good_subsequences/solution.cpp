// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int sumOfGoodSubsequences(std::vector<int>& nums) {
        const int mod = 1000000007;
        std::unordered_map<int, int> cnt, sum;
        int ans = 0;
        for (int x : nums) {
            int c = 1;
            int s = x;
            if (cnt.count(x - 1) && cnt[x - 1] > 0) {
                c = (c + cnt[x - 1]) % mod;
                s = (int)(((long long)s + sum[x - 1] + (long long)cnt[x - 1] * x % mod) % mod);
            }
            if (cnt.count(x + 1) && cnt[x + 1] > 0) {
                c = (c + cnt[x + 1]) % mod;
                s = (int)(((long long)s + sum[x + 1] + (long long)cnt[x + 1] * x % mod) % mod);
            }
            cnt[x] = (cnt[x] + c) % mod;
            sum[x] = (sum[x] + s) % mod;
            ans = (ans + s) % mod;
        }
        return ans;
    }
};

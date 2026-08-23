// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int countSubMultisets(std::vector<int>& nums, int l, int r) {
        const int mod = 1000000007;
        std::unordered_map<int, int> freq;
        int total = 0;
        for (int v : nums) {
            freq[v]++;
            total += v;
        }
        if (total < l) return 0;
        if (r > total) r = total;
        std::vector<int> dp(r + 1);
        dp[0] = 1;
        int zeros = freq[0];
        freq.erase(0);
        for (auto& [v, c] : freq) {
            std::vector<int> ndp(r + 1);
            for (int sum = 0; sum <= r; sum++) {
                if (dp[sum] == 0) continue;
                for (int k = 0; k <= c && sum + k * v <= r; k++)
                    ndp[sum + k * v] = (ndp[sum + k * v] + dp[sum]) % mod;
            }
            dp.swap(ndp);
        }
        int ans = 0;
        for (int s = l; s <= r; s++) ans = (ans + dp[s]) % mod;
        ans = 1LL * ans * (zeros + 1) % mod;
        return ans;
    }
};

// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

#include <vector>

class Solution {
public:
    int countEffectiveSubsequences(std::vector<int>& nums) {
        const int mod = 1000000007;
        int all = 0;
        for (int x : nums) all |= x;
        std::vector<int> bits;
        for (int b = 0; b < 20; b++) if ((all >> b) & 1) bits.push_back(b);
        int m = (int)bits.size();
        std::vector<int> freq(1 << m);
        for (int x : nums) {
            int mask = 0;
            for (int i = 0; i < m; i++) if ((x >> bits[i]) & 1) mask |= 1 << i;
            freq[mask]++;
        }
        std::vector<int> disjoint = freq;
        for (int b = 0; b < m; b++) {
            for (int mask = 0; mask < (1 << m); mask++) {
                if ((mask >> b) & 1) disjoint[mask] += disjoint[mask ^ (1 << b)];
            }
        }
        std::vector<int> pow2(nums.size() + 1);
        pow2[0] = 1;
        for (int i = 1; i <= (int)nums.size(); i++) pow2[i] = pow2[i - 1] * 2 % mod;
        int ans = 0, full = (1 << m) - 1;
        for (int s = 1; s <= full; s++) {
            int ways = pow2[disjoint[full ^ s]];
            int bc = __builtin_popcount(s);
            if (bc & 1) {
                ans += ways;
                if (ans >= mod) ans -= mod;
            } else {
                ans -= ways;
                if (ans < 0) ans += mod;
            }
        }
        return ans;
    }
};

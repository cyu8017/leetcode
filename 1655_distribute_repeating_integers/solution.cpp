// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    bool canDistribute(std::vector<int>& nums, std::vector<int>& quantity) {
        std::unordered_map<int, int> freq;
        for (int x : nums) {
            ++freq[x];
        }
        std::vector<int> cnt;
        for (const auto& [_, c] : freq) {
            cnt.push_back(c);
        }
        std::sort(quantity.rbegin(), quantity.rend());
        int m = static_cast<int>(quantity.size());
        int full = (1 << m) - 1;
        std::vector<int> sums(1 << m, 0);
        for (int mask = 1; mask <= full; ++mask) {
            int bit = mask & -mask;
            int idx = 0;
            while ((1 << idx) != bit) {
                ++idx;
            }
            sums[mask] = sums[mask ^ bit] + quantity[idx];
        }
        std::vector<char> dp(1 << m, 0);
        dp[0] = 1;
        for (int c : cnt) {
            std::vector<char> nxt = dp;
            for (int mask = 0; mask <= full; ++mask) {
                if (!dp[mask]) {
                    continue;
                }
                int left = full ^ mask;
                for (int sub = left; sub; sub = (sub - 1) & left) {
                    if (sums[sub] <= c) {
                        nxt[mask | sub] = 1;
                    }
                }
            }
            dp.swap(nxt);
        }
        return dp[full];
    }
};

// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

#include <algorithm>
#include <bitset>
#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minimumIncompatibility(std::vector<int>& nums, int k) {
        int n = static_cast<int>(nums.size());
        int size = n / k;
        int full = (1 << n) - 1;
        std::unordered_map<int, int> groups;
        for (int mask = 0; mask <= full; ++mask) {
            if (std::bitset<32>(static_cast<unsigned>(mask)).count() != static_cast<size_t>(size)) {
                continue;
            }
            std::vector<int> vals;
            for (int i = 0; i < n; ++i) {
                if (mask >> i & 1) {
                    vals.push_back(nums[i]);
                }
            }
            std::sort(vals.begin(), vals.end());
            bool ok = true;
            for (int i = 1; i < size; ++i) {
                if (vals[i] == vals[i - 1]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                groups[mask] = vals.back() - vals.front();
            }
        }
        std::vector<int> dp(1 << n, INT_MAX / 2);
        dp[0] = 0;
        for (int mask = 0; mask < full; ++mask) {
            if (dp[mask] >= INT_MAX / 2) {
                continue;
            }
            int first = 0;
            while (mask >> first & 1) {
                ++first;
            }
            for (const auto& [g, cost] : groups) {
                if ((g >> first & 1) && !(g & mask)) {
                    dp[mask | g] = std::min(dp[mask | g], dp[mask] + cost);
                }
            }
        }
        return dp[full] >= INT_MAX / 2 ? -1 : dp[full];
    }
};

// LeetCode 3801 - Minimum Cost to Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long minMergeCost(std::vector<std::vector<int>>& lists) {
        int m = (int)lists.size();
        int totalMasks = 1 << m;
        std::vector<std::vector<int>> merged(totalMasks);
        std::vector<int> length(totalMasks), median(totalMasks);
        for (int mask = 1; mask < totalMasks; mask++) {
            int bit = mask & -mask;
            int index = 0;
            while ((1 << index) != bit) index++;
            auto& previous = merged[mask ^ bit];
            auto& current = lists[index];
            std::vector<int> out;
            out.reserve(previous.size() + current.size());
            int i = 0, j = 0;
            while (i < (int)previous.size() || j < (int)current.size()) {
                if (j == (int)current.size() || (i < (int)previous.size() && previous[i] <= current[j])) {
                    out.push_back(previous[i++]);
                } else {
                    out.push_back(current[j++]);
                }
            }
            merged[mask] = out;
            length[mask] = (int)out.size();
            median[mask] = out[(out.size() - 1) / 2];
        }
        const int64_t INF = 1LL << 62;
        std::vector<int64_t> dp(totalMasks, 0);
        for (int mask = 1; mask < totalMasks; mask++) {
            if ((mask & (mask - 1)) == 0) continue;
            dp[mask] = INF;
            int firstBit = mask & -mask;
            for (int left = (mask - 1) & mask; left > 0; left = (left - 1) & mask) {
                if ((left & firstBit) == 0) continue;
                int right = mask ^ left;
                if (right == 0) continue;
                int diff = median[left] - median[right];
                if (diff < 0) diff = -diff;
                int64_t candidate = dp[left] + dp[right] + length[mask] + diff;
                if (candidate < dp[mask]) dp[mask] = candidate;
            }
        }
        return dp[totalMasks - 1];
    }
};

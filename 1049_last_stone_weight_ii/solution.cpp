// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int lastStoneWeightII(std::vector<int>& stones) {
        int total = std::accumulate(stones.begin(), stones.end(), 0);
        int target = total / 2;
        std::vector<bool> dp(target + 1, false);
        dp[0] = true;
        for (int stone : stones) {
            for (int s = target; s >= stone; --s) {
                if (dp[s - stone]) dp[s] = true;
            }
        }
        for (int s = target; s >= 0; --s) {
            if (dp[s]) return total - 2 * s;
        }
        return total;
    }
};


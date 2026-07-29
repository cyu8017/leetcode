// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int minSwaps(std::vector<int>& data) {
        int ones = std::accumulate(data.begin(), data.end(), 0);
        if (ones <= 1) return 0;
        int cur = std::accumulate(data.begin(), data.begin() + ones, 0);
        int best = cur;
        for (int i = ones; i < static_cast<int>(data.size()); ++i) {
            cur += data[i] - data[i - ones];
            best = std::max(best, cur);
        }
        return ones - best;
    }
};

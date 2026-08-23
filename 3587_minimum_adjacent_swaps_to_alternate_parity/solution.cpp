// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

#include <algorithm>
#include <cmath>
#include <vector>

class Solution {
public:
    int minSwaps(std::vector<int>& nums) {
        std::vector<int> pos[2];
        for (int i = 0; i < (int)nums.size(); i++) pos[nums[i] & 1].push_back(i);
        if (std::abs((int)pos[0].size() - (int)pos[1].size()) > 1) return -1;
        auto calc = [&](int k) {
            int res = 0;
            for (int i = 0; i < (int)nums.size(); i += 2) res += std::abs(pos[k][i / 2] - i);
            return res;
        };
        if (pos[0].size() > pos[1].size()) return calc(0);
        if (pos[0].size() < pos[1].size()) return calc(1);
        return std::min(calc(0), calc(1));
    }
};

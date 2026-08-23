// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minMoves(std::vector<int>& nums) {
        int mx = 0, s = 0;
        for (int x : nums) {
            mx = std::max(mx, x);
            s += x;
        }
        return mx * (int)nums.size() - s;
    }
};

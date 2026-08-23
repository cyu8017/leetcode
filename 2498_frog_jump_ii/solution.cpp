// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

#include <vector>

class Solution {
public:
    int maxJump(std::vector<int>& stones) {
        int ans = stones[1] - stones[0];
        for (int i = 2; i < (int)stones.size(); i++) {
            int diff = stones[i] - stones[i - 2];
            if (diff > ans) ans = diff;
        }
        return ans;
    }
};

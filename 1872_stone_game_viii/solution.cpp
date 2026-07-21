// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int stoneGameVIII(std::vector<int>& stones) {
        int n = static_cast<int>(stones.size());
        for (int i = 1; i < n; i++) {
            stones[i] += stones[i - 1];
        }
        int score = stones.back();
        for (int i = n - 2; i >= 1; i--) {
            score = std::max(stones[i] - score, score);
        }
        return score;
    }
};

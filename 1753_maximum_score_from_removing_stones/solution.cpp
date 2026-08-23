// LeetCode 1753 - Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
    int maximumScore(int a, int b, int c) {
        std::vector<int> stones = { a, b, c };
        std::sort(stones.begin(), stones.end(), std::greater<int>());
        int score = 0;
        while (stones[0] > 0 && stones[1] > 0) {
            stones[0]--;
            stones[1]--;
            score++;
            std::sort(stones.begin(), stones.end(), std::greater<int>());
        }
        return score;
    }
};

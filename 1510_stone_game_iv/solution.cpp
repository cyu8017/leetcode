// LeetCode 1510 - Stone Game IV
// https://leetcode.com/problems/stone-game-iv/

#include <vector>

class Solution {
public:
    bool winnerSquareGame(int n) {
        std::vector<bool> win(n + 1, false);
        for (int value = 1; value <= n; ++value) {
            for (int root = 1; root * root <= value; ++root) {
                if (!win[value - root * root]) {
                    win[value] = true;
                    break;
                }
            }
        }
        return win[n];
    }
};

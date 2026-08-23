// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

#include <vector>

class Solution {
public:
    int isWinner(std::vector<int>& player1, std::vector<int>& player2) {
        auto score = [](std::vector<int>& p) {
            int s = 0;
            for (int i = 0; i < (int)p.size(); i++) {
                int mul = 1;
                if ((i > 0 && p[i-1] == 10) || (i > 1 && p[i-2] == 10)) mul = 2;
                s += mul * p[i];
            }
            return s;
        };
        int a = score(player1), b = score(player2);
        if (a > b) return 1;
        if (b > a) return 2;
        return 0;
    }
};

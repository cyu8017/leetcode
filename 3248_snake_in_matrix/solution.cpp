// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

#include <string>
#include <vector>

class Solution {
public:
    int finalPositionOfSnake(int n, std::vector<std::string>& commands) {
        int x = 0, y = 0;
        for (auto& c : commands) {
            switch (c[0]) {
                case 'U': x--; break;
                case 'D': x++; break;
                case 'L': y--; break;
                case 'R': y++; break;
            }
        }
        return x * n + y;
    }
};

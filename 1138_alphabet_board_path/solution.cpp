// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

#include <string>

class Solution {
public:
    std::string alphabetBoardPath(std::string target) {
        int row = 0, col = 0;
        std::string ans;
        for (char ch : target) {
            int r = (ch - 'a') / 5, c = (ch - 'a') % 5;
            while (row > r) { ans += 'U'; --row; }
            while (col > c) { ans += 'L'; --col; }
            while (row < r) { ans += 'D'; ++row; }
            while (col < c) { ans += 'R'; ++col; }
            ans += '!';
        }
        return ans;
    }
};

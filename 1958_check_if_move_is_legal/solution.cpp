// LeetCode 1958 - Check if Move is Legal
#include <string>
#include <vector>

class Solution {
public:
    bool checkMove(std::vector<std::vector<char>>& board, int rMove, int cMove, char color) {
        char opp = color == 'B' ? 'W' : 'B';
        static const int D[8][2] = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
        for (auto& d : D) {
            int r = rMove + d[0], c = cMove + d[1], steps = 0;
            while (r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] == opp) {
                r += d[0]; c += d[1]; steps++;
            }
            if (steps && r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] == color) return true;
        }
        return false;
    }
};

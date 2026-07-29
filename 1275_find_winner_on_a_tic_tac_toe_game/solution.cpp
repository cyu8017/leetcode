// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

#include <string>
#include <vector>

class Solution {
public:
    std::string tictactoe(std::vector<std::vector<int>>& moves) {
        int board[3][3] = {};
        for (int i = 0; i < static_cast<int>(moves.size()); ++i) {
            board[moves[i][0]][moves[i][1]] = (i % 2 == 0) ? 1 : -1;
        }
        auto check = [&](int a, int b, int c, int d, int e, int f) {
            int sum = board[a][b] + board[c][d] + board[e][f];
            if (sum == 3) {
                return "A";
            }
            if (sum == -3) {
                return "B";
            }
            return "";
        };
        std::string lines[] = {
            check(0, 0, 0, 1, 0, 2), check(1, 0, 1, 1, 1, 2), check(2, 0, 2, 1, 2, 2),
            check(0, 0, 1, 0, 2, 0), check(0, 1, 1, 1, 2, 1), check(0, 2, 1, 2, 2, 2),
            check(0, 0, 1, 1, 2, 2), check(0, 2, 1, 1, 2, 0),
        };
        for (const std::string& s : lines) {
            if (!s.empty()) {
                return s;
            }
        }
        return moves.size() == 9 ? "Draw" : "Pending";
    }
};

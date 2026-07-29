// LeetCode 0999 - Available Captures for Rook
// https://leetcode.com/problems/available-captures-for-rook/

#include <vector>

class Solution {
public:
    int numRookCaptures(std::vector<std::vector<char>>& board) {
        int m = (int)board.size(), n = (int)board[0].size();
        int r = -1, c = -1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'R') { r = i; c = j; }
            }
        }
        if (r < 0) return 0;
        int ans = 0;
        const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        for (auto& d : dirs) {
            int i = r + d[0], j = c + d[1];
            while (i >= 0 && i < m && j >= 0 && j < n) {
                if (board[i][j] == 'B') break;
                if (board[i][j] == 'p') { ans++; break; }
                i += d[0];
                j += d[1];
            }
        }
        return ans;
    }
};

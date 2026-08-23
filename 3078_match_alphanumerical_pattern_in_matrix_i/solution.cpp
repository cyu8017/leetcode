// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> findPattern(std::vector<std::vector<int>>& board, std::vector<std::string>& pattern) {
        int m = (int)board.size(), n = (int)board[0].size();
        int r = (int)pattern.size(), c = (int)pattern[0].size();
        auto check = [&](int i, int j) {
            int d1[26] = {}, d2[10] = {};
            for (int a = 0; a < r; a++) {
                for (int b = 0; b < c; b++) {
                    int x = i + a, y = j + b;
                    char ch = pattern[a][b];
                    if (ch >= '0' && ch <= '9') {
                        if ((int)(ch - '0') != board[x][y]) return false;
                    } else {
                        int v = ch - 'a';
                        if (d1[v] > 0 && d1[v] - 1 != board[x][y]) return false;
                        if (d2[board[x][y]] > 0 && d2[board[x][y]] - 1 != v) return false;
                        d1[v] = board[x][y] + 1;
                        d2[board[x][y]] = v + 1;
                    }
                }
            }
            return true;
        };
        for (int i = 0; i < m - r + 1; i++)
            for (int j = 0; j < n - c + 1; j++)
                if (check(i, j)) return {i, j};
        return {-1, -1};
    }
};

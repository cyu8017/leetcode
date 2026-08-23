// LeetCode 1728 - Cat and Mouse II
// https://leetcode.com/problems/cat-and-mouse-ii/

#include <string>
#include <vector>

class Solution {
    int rows = 0;
    int cols = 0;
    int cells = 0;
    int food = 0;
    int maxTurn = 0;
    std::vector<std::vector<int>> mouseMoves;
    std::vector<std::vector<int>> catMoves;
    std::vector<signed char> memo;

    std::vector<int> computeMoves(const std::vector<std::string>& grid, int pos, int jump) {
        int r = pos / cols;
        int c = pos % cols;
        std::vector<int> out{pos};
        const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (const auto& dir : dirs) {
            for (int step = 1; step <= jump; step++) {
                int nr = r + dir[0] * step;
                int nc = c + dir[1] * step;
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == '#') break;
                out.push_back(nr * cols + nc);
            }
        }
        return out;
    }

    bool win(int m, int c, int turn) {
        if (turn >= maxTurn) return false;
        if (m == food) return true;
        if (c == food || c == m) return false;
        int key = (m * cells + c) * maxTurn + turn;
        if (memo[key] != 0) return memo[key] == 1;
        bool result;
        if (turn % 2 == 0) {
            result = false;
            for (int nm : mouseMoves[m]) {
                if (win(nm, c, turn + 1)) {
                    result = true;
                    break;
                }
            }
        } else {
            result = true;
            for (int nc : catMoves[c]) {
                if (!win(m, nc, turn + 1)) {
                    result = false;
                    break;
                }
            }
        }
        memo[key] = result ? 1 : 2;
        return result;
    }

public:
    bool canMouseWin(std::vector<std::string>& grid, int catJump, int mouseJump) {
        rows = grid.size();
        cols = grid[0].size();
        int totalOpen = 0;
        int mouse = 0;
        int cat = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                char cell = grid[r][c];
                if (cell != '#') totalOpen++;
                if (cell == 'M') mouse = r * cols + c;
                else if (cell == 'C') cat = r * cols + c;
                else if (cell == 'F') food = r * cols + c;
            }
        }
        cells = rows * cols;
        mouseMoves.assign(cells, {});
        catMoves.assign(cells, {});
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] != '#') {
                    int pos = r * cols + c;
                    mouseMoves[pos] = computeMoves(grid, pos, mouseJump);
                    catMoves[pos] = computeMoves(grid, pos, catJump);
                }
            }
        }
        maxTurn = 2 * totalOpen;
        memo.assign(static_cast<size_t>(cells) * cells * maxTurn, 0);
        return win(mouse, cat, 0);
    }
};

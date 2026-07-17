// LeetCode 1728 - Cat and Mouse II
// https://leetcode.com/problems/cat-and-mouse-ii/

import java.util.Arrays;

class Solution {
    private int rows;
    private int cols;
    private int cells;
    private int food;
    private int maxTurn;
    private int[][] mouseMoves;
    private int[][] catMoves;
    private byte[] memo;

    public boolean canMouseWin(String[] grid, int catJump, int mouseJump) {
        rows = grid.length;
        cols = grid[0].length();
        int totalOpen = 0;
        int mouse = 0;
        int cat = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                char cell = grid[r].charAt(c);
                if (cell != '#') totalOpen++;
                if (cell == 'M') mouse = r * cols + c;
                else if (cell == 'C') cat = r * cols + c;
                else if (cell == 'F') food = r * cols + c;
            }
        }
        cells = rows * cols;
        mouseMoves = new int[cells][];
        catMoves = new int[cells][];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r].charAt(c) != '#') {
                    int pos = r * cols + c;
                    mouseMoves[pos] = computeMoves(grid, pos, mouseJump);
                    catMoves[pos] = computeMoves(grid, pos, catJump);
                }
            }
        }
        maxTurn = 2 * totalOpen;
        memo = new byte[cells * cells * maxTurn];
        return win(mouse, cat, 0);
    }

    private int[] computeMoves(String[] grid, int pos, int jump) {
        int r = pos / cols;
        int c = pos % cols;
        int[] out = new int[1 + 4 * jump];
        int size = 0;
        out[size++] = pos;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] dir : dirs) {
            for (int step = 1; step <= jump; step++) {
                int nr = r + dir[0] * step;
                int nc = c + dir[1] * step;
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr].charAt(nc) == '#') break;
                out[size++] = nr * cols + nc;
            }
        }
        return Arrays.copyOf(out, size);
    }

    private boolean win(int m, int c, int turn) {
        if (turn >= maxTurn) return false;
        if (m == food) return true;
        if (c == food || c == m) return false;
        int key = (m * cells + c) * maxTurn + turn;
        if (memo[key] != 0) return memo[key] == 1;
        boolean result;
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
        memo[key] = (byte) (result ? 1 : 2);
        return result;
    }
}

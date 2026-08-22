// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int* findPattern(int** board, int boardSize, int* boardColSize, char** pattern, int patternSize, int* returnSize) {
    int m = boardSize, n = boardColSize[0];
    int r = patternSize, c = (int)strlen(pattern[0]);
    int* ans = (int*)malloc(2 * sizeof(int));
    for (int i = 0; i <= m - r; i++) {
        for (int j = 0; j <= n - c; j++) {
            int d1[26] = {0}, d2[10] = {0};
            bool ok = true;
            for (int a = 0; a < r && ok; a++) {
                for (int b = 0; b < c && ok; b++) {
                    int x = i + a, y = j + b;
                    char ch = pattern[a][b];
                    if (ch >= '0' && ch <= '9') {
                        if ((ch - '0') != board[x][y]) ok = false;
                    } else {
                        int v = ch - 'a';
                        if (d1[v] > 0 && d1[v] - 1 != board[x][y]) ok = false;
                        if (d2[board[x][y]] > 0 && d2[board[x][y]] - 1 != v) ok = false;
                        d1[v] = board[x][y] + 1;
                        d2[board[x][y]] = v + 1;
                    }
                }
            }
            if (ok) { ans[0] = i; ans[1] = j; *returnSize = 2; return ans; }
        }
    }
    ans[0] = -1; ans[1] = -1; *returnSize = 2; return ans;
}

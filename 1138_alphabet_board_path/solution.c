// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

#include <stdlib.h>
#include <string.h>

char* alphabetBoardPath(char* target) {
    int n = (int)strlen(target);
    char* ans = (char*)malloc((size_t)(n * 12 + 1));
    int len = 0, row = 0, col = 0;
    for (int i = 0; i < n; i++) {
        int r = (target[i] - 'a') / 5;
        int c = (target[i] - 'a') % 5;
        while (row > r) { ans[len++] = 'U'; row--; }
        while (col > c) { ans[len++] = 'L'; col--; }
        while (row < r) { ans[len++] = 'D'; row++; }
        while (col < c) { ans[len++] = 'R'; col++; }
        ans[len++] = '!';
    }
    ans[len] = '\0';
    return ans;
}

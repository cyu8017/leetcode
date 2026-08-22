// LeetCode 2194 - Cells in a Range on an Excel Sheet
// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

#include <stdlib.h>

char** cellsInRange(char* s, int* returnSize) {
    int cols = s[3] - s[0] + 1, rows = s[4] - s[1] + 1;
    int total = cols * rows;
    char** ans = (char**)malloc((size_t)total * sizeof(char*));
    int an = 0;
    for (char c = s[0]; c <= s[3]; c++) {
        for (char r = s[1]; r <= s[4]; r++) {
            ans[an] = (char*)malloc(3);
            ans[an][0] = c; ans[an][1] = r; ans[an][2] = '\0';
            an++;
        }
    }
    *returnSize = an;
    return ans;
}

// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int minDeletionSize(char** strs, int strsSize) {
    int m = (int)strlen(strs[0]);
    bool* sorted = (bool*)calloc((size_t)(strsSize - 1), sizeof(bool));
    int deleted = 0;
    for (int c = 0; c < m; c++) {
        int bad = 0;
        for (int r = 0; r + 1 < strsSize; r++) {
            if (!sorted[r] && strs[r][c] > strs[r + 1][c]) { bad = 1; break; }
        }
        if (bad) { deleted++; continue; }
        for (int r = 0; r + 1 < strsSize; r++) {
            if (strs[r][c] < strs[r + 1][c]) sorted[r] = true;
        }
    }
    free(sorted);
    return deleted;
}

// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

#include <string.h>

int minDeletionSize(char** strs, int strsSize) {
    int cols = (int)strlen(strs[0]);
    int ans = 0;
    for (int c = 0; c < cols; c++) {
        for (int r = 0; r + 1 < strsSize; r++) {
            if (strs[r][c] > strs[r + 1][c]) { ans++; break; }
        }
    }
    return ans;
}

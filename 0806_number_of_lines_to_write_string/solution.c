// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberOfLines(int* widths, int widthsSize, char* s, int* returnSize) {
    (void)widthsSize;
    int lines = 1, width = 0;
    for (int i = 0; s[i]; i++) {
        int w = widths[s[i] - 'a'];
        if (width + w > 100) {
            lines++;
            width = w;
        } else {
            width += w;
        }
    }
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = lines;
    ans[1] = width;
    *returnSize = 2;
    return ans;
}

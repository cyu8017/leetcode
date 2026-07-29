// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

#include <stdlib.h>
#include <string.h>

int** largeGroupPositions(char* s, int* returnSize, int** returnColumnSizes) {
    int n = (int)strlen(s);
    int** ans = (int**)malloc((size_t)n * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)n * sizeof(int));
    int count = 0, i = 0;
    while (i < n) {
        int j = i;
        while (j < n && s[j] == s[i]) j++;
        if (j - i >= 3) {
            ans[count] = (int*)malloc(2 * sizeof(int));
            ans[count][0] = i;
            ans[count][1] = j - 1;
            (*returnColumnSizes)[count] = 2;
            count++;
        }
        i = j;
    }
    *returnSize = count;
    return ans;
}

// LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
// https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

#include <stdlib.h>
#include <string.h>

int* executeInstructions(int n, int* startPos, int startPosSize, char* s, int* returnSize) {
    (void)startPosSize;
    int m = (int)strlen(s);
    int* ans = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        int r = startPos[0], c = startPos[1], cnt = 0;
        for (int j = i; j < m; j++) {
            if (s[j] == 'L') c--;
            else if (s[j] == 'R') c++;
            else if (s[j] == 'U') r--;
            else r++;
            if (r < 0 || r >= n || c < 0 || c >= n) break;
            cnt++;
        }
        ans[i] = cnt;
    }
    *returnSize = m;
    return ans;
}

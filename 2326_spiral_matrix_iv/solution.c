// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

int** spiralMatrix(int m, int n, struct ListNode* head, int* returnSize, int** returnColumnSizes) {
    int** ans = (int**)malloc((size_t)m * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        ans[i] = (int*)malloc((size_t)n * sizeof(int));
        (*returnColumnSizes)[i] = n;
        for (int j = 0; j < n; j++) ans[i][j] = -1;
    }
    int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int r = 0, c = 0, d = 0;
    while (head) {
        ans[r][c] = head->val;
        head = head->next;
        int nr = r + dirs[d][0], nc = c + dirs[d][1];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n || ans[nr][nc] != -1) {
            d = (d + 1) % 4;
            nr = r + dirs[d][0];
            nc = c + dirs[d][1];
        }
        r = nr;
        c = nc;
    }
    *returnSize = m;
    return ans;
}

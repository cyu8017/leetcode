// LeetCode 3030 - Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/

#include <stdlib.h>
#include <string.h>

static int iabs(int x) { return x < 0 ? -x : x; }

int** resultGrid(int** image, int imageSize, int* imageColSize, int threshold, int* returnSize, int** returnColumnSizes) {
    int n = imageSize, m = imageColSize[0];
    int** ans = (int**)malloc((size_t)n * sizeof(int*));
    int** ct = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        ans[i] = (int*)calloc((size_t)m, sizeof(int));
        ct[i] = (int*)calloc((size_t)m, sizeof(int));
    }
    for (int i = 0; i + 2 < n; i++) {
        for (int j = 0; j + 2 < m; j++) {
            int region = 1;
            for (int k = 0; k < 3; k++) for (int l = 0; l < 2; l++)
                region = region && iabs(image[i+k][j+l] - image[i+k][j+l+1]) <= threshold;
            for (int k = 0; k < 2; k++) for (int l = 0; l < 3; l++)
                region = region && iabs(image[i+k][j+l] - image[i+k+1][j+l]) <= threshold;
            if (region) {
                int tot = 0;
                for (int k = 0; k < 3; k++) for (int l = 0; l < 3; l++) tot += image[i+k][j+l];
                for (int k = 0; k < 3; k++) for (int l = 0; l < 3; l++) {
                    ct[i+k][j+l]++;
                    ans[i+k][j+l] += tot / 9;
                }
            }
        }
    }
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
        if (ct[i][j] == 0) ans[i][j] = image[i][j];
        else ans[i][j] /= ct[i][j];
    }
    for (int i = 0; i < n; i++) free(ct[i]);
    free(ct);
    *returnSize = n;
    *returnColumnSizes = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) (*returnColumnSizes)[i] = m;
    return ans;
}

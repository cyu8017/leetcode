// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

#include <stdlib.h>
#include <string.h>

char*** mostPopularCreator(char** creators, int creatorsSize, char** ids, int idsSize, int* views, int viewsSize, int* returnSize, int** returnColumnSizes) {
    (void)idsSize; (void)viewsSize;
    int n = creatorsSize;
    char** uniq = (char**)malloc((size_t)n * sizeof(char*));
    long long* total = (long long*)calloc((size_t)n, sizeof(long long));
    char** bestID = (char**)malloc((size_t)n * sizeof(char*));
    int* bestViews = (int*)malloc((size_t)n * sizeof(int));
    int uc = 0;
    long long maxTotal = 0;
    for (int i = 0; i < n; i++) {
        int idx = -1;
        for (int j = 0; j < uc; j++) {
            if (strcmp(uniq[j], creators[i]) == 0) { idx = j; break; }
        }
        if (idx < 0) {
            idx = uc++;
            uniq[idx] = creators[i];
            total[idx] = 0;
            bestID[idx] = ids[i];
            bestViews[idx] = views[i];
        }
        total[idx] += views[i];
        if (views[i] > bestViews[idx] || (views[i] == bestViews[idx] && strcmp(ids[i], bestID[idx]) < 0)) {
            bestViews[idx] = views[i];
            bestID[idx] = ids[i];
        }
        if (total[idx] > maxTotal) maxTotal = total[idx];
    }
    char*** ans = (char***)malloc((size_t)uc * sizeof(char**));
    int* cols = (int*)malloc((size_t)uc * sizeof(int));
    int cnt = 0;
    for (int i = 0; i < uc; i++) {
        if (total[i] == maxTotal) {
            ans[cnt] = (char**)malloc(2 * sizeof(char*));
            ans[cnt][0] = uniq[i];
            ans[cnt][1] = bestID[i];
            cols[cnt] = 2;
            cnt++;
        }
    }
    free(uniq); free(total); free(bestID); free(bestViews);
    *returnSize = cnt;
    *returnColumnSizes = cols;
    return ans;
}

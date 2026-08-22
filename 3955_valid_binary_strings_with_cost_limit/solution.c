// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

#include <stdlib.h>
#include <string.h>

static char** ans3955;
static int an3955, acap3955;
static char* path3955;
static int n3955, k3955;

static void dfs3955(int i, int tot) {
    if (i >= n3955) {
        if (an3955 == acap3955) {
            acap3955 = acap3955 ? acap3955 * 2 : 8;
            ans3955 = realloc(ans3955, (size_t)acap3955 * sizeof(char*));
        }
        ans3955[an3955] = malloc((size_t)n3955 + 1);
        memcpy(ans3955[an3955], path3955, (size_t)n3955);
        ans3955[an3955][n3955] = 0;
        an3955++;
        return;
    }
    path3955[i] = '0';
    dfs3955(i + 1, tot);
    if ((i == 0 || path3955[i - 1] == '0') && tot + i <= k3955) {
        path3955[i] = '1';
        dfs3955(i + 1, tot + i);
    }
}

char** generateValidStrings(int n, int k, int* returnSize) {
    n3955 = n; k3955 = k; an3955 = 0; acap3955 = 0; ans3955 = NULL;
    path3955 = malloc((size_t)n + 1);
    dfs3955(0, 0);
    free(path3955);
    *returnSize = an3955;
    return ans3955;
}

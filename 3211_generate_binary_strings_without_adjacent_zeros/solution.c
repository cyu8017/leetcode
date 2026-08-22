// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

#include <stdlib.h>
#include <string.h>

static char** ans3211;
static int an3211, ac3211, n3211;
static char* t3211;

static void dfs3211(int i) {
    if (i >= n3211) {
        if (an3211 == ac3211) {
            ac3211 = ac3211 ? ac3211 * 2 : 16;
            ans3211 = realloc(ans3211, ac3211 * sizeof(char*));
        }
        ans3211[an3211] = malloc(n3211 + 1);
        memcpy(ans3211[an3211], t3211, n3211);
        ans3211[an3211][n3211] = 0;
        an3211++;
        return;
    }
    for (int j = 0; j < 2; j++) {
        if ((j == 0 && (i == 0 || t3211[i - 1] == '1')) || j == 1) {
            t3211[i] = '0' + j;
            dfs3211(i + 1);
        }
    }
}

char** validStrings(int n, int* returnSize) {
    n3211 = n; an3211 = 0; ac3211 = 0; ans3211 = NULL;
    t3211 = malloc(n + 1);
    dfs3211(0);
    free(t3211);
    *returnSize = an3211;
    return ans3211;
}

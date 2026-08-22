// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

#include <stdlib.h>
#include <string.h>

char** stringSequence(char* target, int* returnSize) {
    int m = (int)strlen(target);
    int cap = m * 26 + 8;
    char** ans = (char**)malloc((size_t)cap * sizeof(char*));
    int alen = 0;
    char* cur = (char*)malloc((size_t)m + 1);
    int clen = 0;
    cur[0] = 0;
    for (int ti = 0; ti < m; ti++) {
        char ch = target[ti];
        cur[clen++] = 'a';
        cur[clen] = 0;
        ans[alen] = (char*)malloc((size_t)clen + 1);
        memcpy(ans[alen], cur, (size_t)clen + 1);
        alen++;
        while (cur[clen - 1] != ch) {
            cur[clen - 1]++;
            ans[alen] = (char*)malloc((size_t)clen + 1);
            memcpy(ans[alen], cur, (size_t)clen + 1);
            alen++;
        }
    }
    free(cur);
    *returnSize = alen;
    return ans;
}

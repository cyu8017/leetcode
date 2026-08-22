// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char** twoEditWords(char** queries, int queriesSize, char** dictionary, int dictionarySize, int* returnSize) {
    char** ans = (char**)malloc((size_t)queriesSize * sizeof(char*));
    int cnt = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        char* q = queries[qi];
        int len = (int)strlen(q);
        bool ok = false;
        for (int di = 0; di < dictionarySize; di++) {
            char* d = dictionary[di];
            int diff = 0;
            for (int i = 0; i < len; i++) {
                if (q[i] != d[i]) {
                    diff++;
                    if (diff > 2) break;
                }
            }
            if (diff <= 2) { ok = true; break; }
        }
        if (ok) ans[cnt++] = q;
    }
    *returnSize = cnt;
    return ans;
}

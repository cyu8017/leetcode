// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char** partitionString(char* s, int* returnSize) {
    /* store seen strings in simple list */
    char** seen = NULL; int seenN = 0, seenCap = 0;
    char** ans = NULL; int ansN = 0, ansCap = 0;
    char buf[512]; int blen = 0;
    for (int i = 0; s[i]; i++) {
        buf[blen++] = s[i]; buf[blen] = '\0';
        bool found = false;
        for (int j = 0; j < seenN; j++) if (strcmp(seen[j], buf) == 0) { found = true; break; }
        if (!found) {
            if (seenN == seenCap) { seenCap = seenCap ? seenCap*2 : 8; seen = realloc(seen, (size_t)seenCap*sizeof(char*)); }
            seen[seenN] = (char*)malloc((size_t)blen+1); strcpy(seen[seenN], buf); seenN++;
            if (ansN == ansCap) { ansCap = ansCap ? ansCap*2 : 8; ans = realloc(ans, (size_t)ansCap*sizeof(char*)); }
            ans[ansN] = (char*)malloc((size_t)blen+1); strcpy(ans[ansN], buf); ansN++;
            blen = 0;
        }
    }
    for (int j = 0; j < seenN; j++) free(seen[j]);
    free(seen);
    *returnSize = ansN;
    return ans;
}

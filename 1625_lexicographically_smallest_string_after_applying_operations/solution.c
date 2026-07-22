// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

#include <stdlib.h>
#include <string.h>

char* findLexSmallestString(char* s, int a, int b) {
    int n = (int)strlen(s);
    char** q = (char**)malloc(100000 * sizeof(char*));
    char** seen = (char**)malloc(100000 * sizeof(char*));
    int front = 0, back = 0, seenN = 0;
    char* start = (char*)malloc((size_t)n + 1);
    strcpy(start, s);
    q[back++] = start;
    seen[seenN++] = start;
    char* ans = start;
    while (front < back) {
        char* cur = q[front++];
        if (strcmp(cur, ans) < 0) ans = cur;
        char* add = (char*)malloc((size_t)n + 1);
        for (int i = 0; i < n; i++) {
            int d = cur[i] - '0';
            if (i % 2) d = (d + a) % 10;
            add[i] = (char)('0' + d);
        }
        add[n] = 0;
        char* rot = (char*)malloc((size_t)n + 1);
        memcpy(rot, cur + n - b, (size_t)b);
        memcpy(rot + b, cur, (size_t)(n - b));
        rot[n] = 0;
        char* cands[2] = {add, rot};
        for (int c = 0; c < 2; c++) {
            int found = 0;
            for (int i = 0; i < seenN; i++) {
                if (strcmp(seen[i], cands[c]) == 0) { found = 1; break; }
            }
            if (!found) {
                seen[seenN++] = cands[c];
                q[back++] = cands[c];
            } else {
                free(cands[c]);
            }
        }
    }
    char* result = (char*)malloc((size_t)n + 1);
    strcpy(result, ans);
    for (int i = 0; i < seenN; i++) free(seen[i]);
    free(q); free(seen);
    return result;
}

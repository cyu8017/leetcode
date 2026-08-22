// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static int digits2468(int x) {
    if (x == 0) return 1;
    int d = 0;
    while (x > 0) { d++; x /= 10; }
    return d;
}

char** splitMessage(char* message, int limit, int* returnSize) {
    int n = (int)strlen(message);
    for (int parts = 1; parts <= n; parts++) {
        int sbDigits = digits2468(parts);
        int ok = 1;
        int idx = 0;
        char** res = (char**)malloc((size_t)parts * sizeof(char*));
        int cnt = 0;
        for (int i = 1; i <= parts; i++) {
            int tail = 3 + digits2468(i) + sbDigits;
            int cap = limit - tail;
            if (cap <= 0 || idx >= n) { ok = 0; break; }
            int take = cap;
            if (take > n - idx) take = n - idx;
            res[cnt] = (char*)malloc((size_t)(take + tail + 1));
            memcpy(res[cnt], message + idx, (size_t)take);
            sprintf(res[cnt] + take, "<%d/%d>", i, parts);
            idx += take;
            cnt++;
        }
        if (ok && idx == n && cnt == parts) {
            *returnSize = parts;
            return res;
        }
        for (int i = 0; i < cnt; i++) free(res[i]);
        free(res);
    }
    *returnSize = 0;
    return NULL;
}

// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

#include <stdlib.h>

typedef struct {
    int user;
    int minute;
} UamPair;

static int cmpUamPair(const void* a, const void* b) {
    const UamPair* x = (const UamPair*)a;
    const UamPair* y = (const UamPair*)b;
    if (x->user != y->user) return (x->user > y->user) - (x->user < y->user);
    return (x->minute > y->minute) - (x->minute < y->minute);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findingUsersActiveMinutes(int** logs, int logsSize, int* logsColSize, int k, int* returnSize) {
    (void)logsColSize;
    UamPair* pairs = (UamPair*)malloc((size_t)logsSize * sizeof(UamPair));
    for (int i = 0; i < logsSize; i++) {
        pairs[i].user = logs[i][0];
        pairs[i].minute = logs[i][1];
    }
    qsort(pairs, (size_t)logsSize, sizeof(UamPair), cmpUamPair);

    int* answer = (int*)calloc((size_t)k, sizeof(int));
    int i = 0;
    while (i < logsSize) {
        int user = pairs[i].user;
        int unique = 0;
        int lastMinute = -1;
        while (i < logsSize && pairs[i].user == user) {
            if (pairs[i].minute != lastMinute) {
                unique++;
                lastMinute = pairs[i].minute;
            }
            i++;
        }
        if (unique >= 1 && unique <= k) answer[unique - 1]++;
    }

    free(pairs);
    *returnSize = k;
    return answer;
}

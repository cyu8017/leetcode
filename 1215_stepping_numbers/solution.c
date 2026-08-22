// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int* countSteppingNumbers(int low, int high, int* returnSize) {
    int* answer = (int*)malloc(10000 * sizeof(int));
    int count = 0;
    if (low == 0) answer[count++] = 0;
    long long* queue = (long long*)malloc(100000 * sizeof(long long));
    int qs = 0, qe = 0;
    for (int d = 1; d <= 9; d++) queue[qe++] = d;
    while (qs < qe) {
        long long x = queue[qs++];
        if (x > high) continue;
        if (x >= low) answer[count++] = (int)x;
        int last = (int)(x % 10);
        if (last > 0) queue[qe++] = x * 10 + last - 1;
        if (last < 9) queue[qe++] = x * 10 + last + 1;
    }
    free(queue);
    qsort(answer, (size_t)count, sizeof(int), cmpInt);
    *returnSize = count;
    return answer;
}

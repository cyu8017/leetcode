// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int* findOriginalArray(int* changed, int changedSize, int* returnSize) {
    if (changedSize % 2 != 0) {
        *returnSize = 0;
        return NULL;
    }
    qsort(changed, (size_t)changedSize, sizeof(int), cmpInt);
    int maxv = changed[changedSize - 1];
    int* freq = (int*)calloc((size_t)(maxv + 1), sizeof(int));
    for (int i = 0; i < changedSize; i++) freq[changed[i]]++;
    int* ans = (int*)malloc((size_t)(changedSize / 2) * sizeof(int));
    int n = 0;
    for (int i = 0; i < changedSize; i++) {
        int x = changed[i];
        if (freq[x] == 0) continue;
        freq[x]--;
        if (2 * x > maxv || freq[2 * x] == 0) {
            free(freq); free(ans);
            *returnSize = 0;
            return NULL;
        }
        freq[2 * x]--;
        ans[n++] = x;
    }
    free(freq);
    *returnSize = n;
    return ans;
}

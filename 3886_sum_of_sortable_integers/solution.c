// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

#include <stdlib.h>
#include <string.h>

static int cmpInt3886(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int rotationMatches3886(int* block, int* target, int k) {
    int* prefix = calloc((size_t)k, sizeof(int));
    for (int i = 1; i < k; i++) {
        int j = prefix[i - 1];
        while (j > 0 && target[i] != target[j]) j = prefix[j - 1];
        if (target[i] == target[j]) j++;
        prefix[i] = j;
    }
    int matched = 0, ok = 0;
    for (int i = 0; i < 2 * k - 1; i++) {
        int x = block[i % k];
        while (matched > 0 && x != target[matched]) matched = prefix[matched - 1];
        if (x == target[matched]) matched++;
        if (matched == k) { ok = 1; break; }
    }
    free(prefix);
    return ok;
}

int sumOfSortableIntegers(int* nums, int numsSize) {
    int n = numsSize;
    int* sorted = malloc((size_t)n * sizeof(int));
    memcpy(sorted, nums, (size_t)n * sizeof(int));
    qsort(sorted, (size_t)n, sizeof(int), cmpInt3886);
    int* divisors = malloc((size_t)(n + 1) * sizeof(int));
    int dcnt = 0;
    for (int d = 1; d * d <= n; d++) {
        if (n % d == 0) {
            divisors[dcnt++] = d;
            if (d * d != n) divisors[dcnt++] = n / d;
        }
    }
    int answer = 0;
    for (int di = 0; di < dcnt; di++) {
        int k = divisors[di];
        int ok = 1;
        for (int start = 0; start < n; start += k) {
            if (!rotationMatches3886(nums + start, sorted + start, k)) { ok = 0; break; }
        }
        if (ok) answer += k;
    }
    free(sorted); free(divisors);
    return answer;
}

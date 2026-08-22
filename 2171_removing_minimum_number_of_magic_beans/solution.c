// LeetCode 2171 - Removing Minimum Number of Magic Beans
// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

#include <stdlib.h>

static int cmpAsc(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

long long minimumRemoval(int* beans, int beansSize) {
    qsort(beans, (size_t)beansSize, sizeof(int), cmpAsc);
    long long sum = 0;
    for (int i = 0; i < beansSize; i++) sum += beans[i];
    long long ans = sum;
    for (int i = 0; i < beansSize; i++) {
        long long remain = (long long)(beansSize - i) * beans[i];
        if (sum - remain < ans) ans = sum - remain;
    }
    return ans;
}

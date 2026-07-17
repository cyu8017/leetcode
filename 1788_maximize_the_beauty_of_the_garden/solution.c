// LeetCode 1788 - Maximize the Beauty of the Garden
// https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

#include <stdlib.h>

#define VALUE_OFFSET 10000
#define VALUE_RANGE 20001

int maximumBeauty(int* flowers, int flowersSize) {
    int* first = (int*)malloc(VALUE_RANGE * sizeof(int));
    for (int i = 0; i < VALUE_RANGE; i++) {
        first[i] = -1;
    }
    long long* prefix = (long long*)malloc((flowersSize + 1) * sizeof(long long));
    prefix[0] = 0;
    for (int i = 0; i < flowersSize; i++) {
        prefix[i + 1] = prefix[i] + (flowers[i] > 0 ? flowers[i] : 0);
    }
    long long best = -0x7fffffffffffffffLL;
    for (int i = 0; i < flowersSize; i++) {
        int index = flowers[i] + VALUE_OFFSET;
        if (first[index] >= 0) {
            int left = first[index];
            long long between = prefix[i] - prefix[left + 1];
            long long candidate = (long long)flowers[left] + flowers[i] + between;
            if (candidate > best) {
                best = candidate;
            }
        } else {
            first[index] = i;
        }
    }
    free(first);
    free(prefix);
    return (int)best;
}

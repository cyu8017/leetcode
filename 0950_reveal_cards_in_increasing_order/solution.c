// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int* deckRevealedIncreasing(int* deck, int deckSize, int* returnSize) {
    qsort(deck, (size_t)deckSize, sizeof(int), cmpInt);
    int* idx = (int*)malloc((size_t)deckSize * 2 * sizeof(int));
    int head = 0, tail = 0;
    for (int i = 0; i < deckSize; i++) idx[tail++] = i;
    int* ans = (int*)calloc((size_t)deckSize, sizeof(int));
    for (int i = 0; i < deckSize; i++) {
        ans[idx[head++]] = deck[i];
        if (head < tail) idx[tail++] = idx[head++];
    }
    free(idx);
    *returnSize = deckSize;
    return ans;
}

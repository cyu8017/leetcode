// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

#include <stdlib.h>

typedef struct { int price, count; } Batch3947;
static int cmp3947(const void* a, const void* b) {
    return ((const Batch3947*)a)->price - ((const Batch3947*)b)->price;
}

int maxItems(int** items, int itemsSize, int* itemsColSize, int budget) {
    (void)itemsColSize;
    int n = itemsSize;
    int* frequency = calloc((size_t)(n + 1), sizeof(int));
    int minimumPrice = items[0][1];
    for (int i = 0; i < n; i++) {
        frequency[items[i][0]]++;
        if (items[i][1] < minimumPrice) minimumPrice = items[i][1];
    }
    Batch3947* batches = malloc((size_t)n * sizeof(Batch3947));
    int bn = 0;
    for (int i = 0; i < n; i++) {
        int gain = 0;
        for (int multiple = items[i][0]; multiple <= n; multiple += items[i][0]) gain += frequency[multiple];
        gain--;
        if (gain > 0 && items[i][1] < 2 * minimumPrice) {
            batches[bn].price = items[i][1];
            batches[bn].count = gain;
            bn++;
        }
    }
    qsort(batches, (size_t)bn, sizeof(Batch3947), cmp3947);
    long long remaining = budget;
    long long answer = budget / minimumPrice;
    long long boosted = 0;
    for (int i = 0; i < bn; i++) {
        long long count = batches[i].count;
        long long affordable = remaining / batches[i].price;
        if (affordable < count) count = affordable;
        remaining -= count * batches[i].price;
        boosted += count;
        long long total = 2 * boosted + remaining / minimumPrice;
        if (total > answer) answer = total;
        if (count < batches[i].count) break;
    }
    free(frequency); free(batches);
    return (int)answer;
}

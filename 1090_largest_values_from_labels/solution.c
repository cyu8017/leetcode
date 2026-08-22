// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

#include <stdlib.h>

typedef struct {
    int value;
    int label;
} Item;

static int cmpItemDesc(const void* a, const void* b) {
    return ((const Item*)b)->value - ((const Item*)a)->value;
}

int largestValsFromLabels(int* values, int valuesSize, int* labels, int labelsSize, int numWanted, int useLimit) {
    (void)labelsSize;
    Item* items = (Item*)malloc((size_t)valuesSize * sizeof(Item));
    for (int i = 0; i < valuesSize; i++) {
        items[i].value = values[i];
        items[i].label = labels[i];
    }
    qsort(items, (size_t)valuesSize, sizeof(Item), cmpItemDesc);
    int used[20001] = {0};
    int ans = 0, taken = 0;
    for (int i = 0; i < valuesSize && taken < numWanted; i++) {
        int label = items[i].label;
        if (used[label] < useLimit) {
            used[label]++;
            ans += items[i].value;
            taken++;
        }
    }
    free(items);
    return ans;
}

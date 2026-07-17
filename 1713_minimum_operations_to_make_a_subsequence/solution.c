// LeetCode 1713 - Minimum Operations to Make a Subsequence
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

#include <stdlib.h>

typedef struct {
    int value;
    int index;
} ValueIndex;

static int compareValueIndex(const void* a, const void* b) {
    int va = ((const ValueIndex*)a)->value;
    int vb = ((const ValueIndex*)b)->value;
    return (va > vb) - (va < vb);
}

int minOperations(int* target, int targetSize, int* arr, int arrSize) {
    ValueIndex* sorted = (ValueIndex*)malloc(targetSize * sizeof(ValueIndex));
    for (int i = 0; i < targetSize; i++) {
        sorted[i].value = target[i];
        sorted[i].index = i;
    }
    qsort(sorted, targetSize, sizeof(ValueIndex), compareValueIndex);

    int* lis = (int*)malloc(targetSize * sizeof(int));
    int size = 0;
    for (int i = 0; i < arrSize; i++) {
        int lo = 0;
        int hi = targetSize - 1;
        int idx = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (sorted[mid].value == arr[i]) {
                idx = sorted[mid].index;
                break;
            }
            if (sorted[mid].value < arr[i]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        if (idx < 0) {
            continue;
        }
        lo = 0;
        hi = size;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (lis[mid] < idx) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        lis[lo] = idx;
        if (lo == size) {
            size++;
        }
    }
    free(sorted);
    free(lis);
    return targetSize - size;
}

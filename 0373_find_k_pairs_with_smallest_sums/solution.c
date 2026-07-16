// LeetCode 0373 - Find K Pairs with Smallest Sums
// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

#include <stdlib.h>

typedef struct {
    int sum;
    int index1;
    int index2;
} HeapEntry;

static int compareHeapEntries(const void* left, const void* right) {
    return ((const HeapEntry*)left)->sum - ((const HeapEntry*)right)->sum;
}

static void heapPush(HeapEntry* heap, int* heapSize, int sum, int index1, int index2) {
    heap[*heapSize].sum = sum;
    heap[*heapSize].index1 = index1;
    heap[*heapSize].index2 = index2;
    *heapSize += 1;
    qsort(heap, (size_t)*heapSize, sizeof(HeapEntry), compareHeapEntries);
}

static HeapEntry heapPop(HeapEntry* heap, int* heapSize) {
    HeapEntry top = heap[0];
    heap[0] = heap[*heapSize - 1];
    *heapSize -= 1;
    qsort(heap, (size_t)*heapSize, sizeof(HeapEntry), compareHeapEntries);
    return top;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the array elements are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** kSmallestPairs(int* nums1, int nums1Size, int* nums2, int nums2Size, int k, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;
    if (nums1Size == 0 || nums2Size == 0 || k == 0) {
        *returnColumnSizes = NULL;
        return NULL;
    }

    int heapCapacity = nums1Size < k ? nums1Size : k;
    if (heapCapacity < 1) {
        heapCapacity = 1;
    }
    HeapEntry* heap = (HeapEntry*)malloc((size_t)heapCapacity * sizeof(HeapEntry));
    int heapSize = 0;

    int seedCount = nums1Size < k ? nums1Size : k;
    for (int index = 0; index < seedCount; index++) {
        heapPush(heap, &heapSize, nums1[index] + nums2[0], index, 0);
    }

    int capacity = k;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)capacity * sizeof(int));

    while (heapSize > 0 && *returnSize < k) {
        HeapEntry top = heapPop(heap, &heapSize);
        result[*returnSize] = (int*)malloc(2 * sizeof(int));
        result[*returnSize][0] = nums1[top.index1];
        result[*returnSize][1] = nums2[top.index2];
        (*returnColumnSizes)[*returnSize] = 2;
        *returnSize += 1;

        if (top.index2 + 1 < nums2Size) {
            if (heapSize >= heapCapacity) {
                heapCapacity *= 2;
                heap = (HeapEntry*)realloc(heap, (size_t)heapCapacity * sizeof(HeapEntry));
            }
            heapPush(
                heap,
                &heapSize,
                nums1[top.index1] + nums2[top.index2 + 1],
                top.index1,
                top.index2 + 1
            );
        }
    }

    free(heap);
    return result;
}

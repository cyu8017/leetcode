// LeetCode 0321 - Create Maximum Number
// https://leetcode.com/problems/create-maximum-number/

#include <stdlib.h>
#include <string.h>

static int* pickMax(const int* values, int valuesSize, int count, int* returnSize) {
    int drop = valuesSize - count;
    int* stack = (int*)malloc((size_t)valuesSize * sizeof(int));
    int stackSize = 0;
    for (int index = 0; index < valuesSize; index++) {
        int value = values[index];
        while (drop > 0 && stackSize > 0 && stack[stackSize - 1] < value) {
            stackSize -= 1;
            drop -= 1;
        }
        stack[stackSize++] = value;
    }
    *returnSize = count;
    int* result = (int*)malloc((size_t)count * sizeof(int));
    memcpy(result, stack, (size_t)count * sizeof(int));
    free(stack);
    return result;
}

static int suffixGreater(
    const int* first,
    int firstSize,
    int left,
    const int* second,
    int secondSize,
    int right
) {
    while (left < firstSize && right < secondSize) {
        if (first[left] != second[right]) {
            return first[left] > second[right];
        }
        left += 1;
        right += 1;
    }
    return (firstSize - left) > (secondSize - right);
}

static int* mergeArrays(
    const int* first,
    int firstSize,
    const int* second,
    int secondSize,
    int* returnSize
) {
    int* result = (int*)malloc((size_t)(firstSize + secondSize) * sizeof(int));
    int left = 0;
    int right = 0;
    int write = 0;
    while (left < firstSize && right < secondSize) {
        if (suffixGreater(first, firstSize, left, second, secondSize, right)) {
            result[write++] = first[left++];
        } else {
            result[write++] = second[right++];
        }
    }
    while (left < firstSize) {
        result[write++] = first[left++];
    }
    while (right < secondSize) {
        result[write++] = second[right++];
    }
    *returnSize = write;
    return result;
}

static int compareVectors(const int* left, int leftSize, const int* right, int rightSize) {
    int minSize = leftSize < rightSize ? leftSize : rightSize;
    for (int index = 0; index < minSize; index++) {
        if (left[index] != right[index]) {
            return left[index] - right[index];
        }
    }
    return leftSize - rightSize;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxNumber(int* nums1, int nums1Size, int* nums2, int nums2Size, int k, int* returnSize) {
    int* best = NULL;
    int bestSize = 0;
    int minFirst = k - nums2Size;
    if (minFirst < 0) {
        minFirst = 0;
    }
    int maxFirst = k < nums1Size ? k : nums1Size;
    for (int takeFirst = minFirst; takeFirst <= maxFirst; takeFirst++) {
        int takeSecond = k - takeFirst;
        int firstSize = 0;
        int secondSize = 0;
        int* first = pickMax(nums1, nums1Size, takeFirst, &firstSize);
        int* second = pickMax(nums2, nums2Size, takeSecond, &secondSize);
        int candidateSize = 0;
        int* candidate = mergeArrays(first, firstSize, second, secondSize, &candidateSize);
        free(first);
        free(second);
        if (best == NULL || compareVectors(candidate, candidateSize, best, bestSize) > 0) {
            free(best);
            best = candidate;
            bestSize = candidateSize;
        } else {
            free(candidate);
        }
    }
    *returnSize = bestSize;
    return best;
}

// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

#include <stdlib.h>

static int cmpAsc(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int reductionOperations(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpAsc);
    int answer = 0;
    int rank = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[i - 1]) rank++;
        answer += rank;
    }
    return answer;
}

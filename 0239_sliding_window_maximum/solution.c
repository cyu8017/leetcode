// LeetCode 0239 - Sliding Window Maximum
// https://leetcode.com/problems/sliding-window-maximum/

#include <stdlib.h>

int* maxSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    int* result = malloc((size_t)(numsSize - k + 1) * sizeof(int));
    int* deque = malloc((size_t)numsSize * sizeof(int));
    int front = 0;
    int back = 0;
    *returnSize = 0;

    for (int index = 0; index < numsSize; index++) {
        while (front < back && nums[deque[back - 1]] <= nums[index]) {
            back--;
        }
        deque[back++] = index;
        if (deque[front] <= index - k) {
            front++;
        }
        if (index >= k - 1) {
            result[(*returnSize)++] = nums[deque[front]];
        }
    }

    free(deque);
    return result;
}

// LeetCode 0457 - Circular Array Loop
// https://leetcode.com/problems/circular-array-loop/

#include <stdbool.h>

static int nextIndex(int* nums, int length, int index) {
    long long next = ((long long)index + nums[index]) % length;
    if (next < 0) {
        next += length;
    }
    return (int)next;
}

bool circularArrayLoop(int* nums, int numsSize) {
    for (int start = 0; start < numsSize; start++) {
        if (nums[start] == 0) {
            continue;
        }
        bool forward = nums[start] > 0;
        int slow = start;
        int fast = start;
        while (1) {
            slow = nextIndex(nums, numsSize, slow);
            fast = nextIndex(nums, numsSize, nextIndex(nums, numsSize, fast));
            int sign = forward ? 1 : -1;
            if (nums[slow] * sign <= 0 || nums[fast] * sign <= 0 || nums[nextIndex(nums, numsSize, fast)] * sign <= 0) {
                break;
            }
            if (slow == fast) {
                if (slow == nextIndex(nums, numsSize, slow)) {
                    break;
                }
                return true;
            }
        }

        int index = start;
        int value = nums[start];
        while ((long long)nums[index] * value > 0) {
            int nxt = nextIndex(nums, numsSize, index);
            nums[index] = 0;
            index = nxt;
        }
    }
    return false;
}

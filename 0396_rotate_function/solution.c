// LeetCode 0396 - Rotate Function
// https://leetcode.com/problems/rotate-function/

static int maxInt(int left, int right) {
    return left > right ? left : right;
}

int maxRotateFunction(int* nums, int numsSize) {
    int total = 0;
    int current = 0;

    for (int index = 0; index < numsSize; index++) {
        total += nums[index];
        current += index * nums[index];
    }

    int best = current;
    for (int index = numsSize - 1; index > 0; index--) {
        current += total - numsSize * nums[index];
        best = maxInt(best, current);
    }

    return best;
}

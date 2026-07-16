// LeetCode 0413 - Arithmetic Slices
// https://leetcode.com/problems/arithmetic-slices/

int numberOfArithmeticSlices(int* nums, int numsSize) {
    if (numsSize < 3) {
        return 0;
    }

    int total = 0;
    int current = 0;

    for (int index = 2; index < numsSize; index++) {
        if (nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]) {
            current += 1;
            total += current;
        } else {
            current = 0;
        }
    }

    return total;
}

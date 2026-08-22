// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

void moveZeroes(int* nums, int numsSize) {
    int insert = 0;
    for (int index = 0; index < numsSize; index++) {
        if (nums[index] != 0) {
            nums[insert++] = nums[index];
        }
    }
    for (int index = insert; index < numsSize; index++) {
        nums[index] = 0;
    }
}

// LeetCode 0280 - Wiggle Sort
// https://leetcode.com/problems/wiggle-sort/

void wiggleSort(int* nums, int numsSize) {
    for (int index = 1; index < numsSize; index++) {
        if (index % 2 == 1 && nums[index] < nums[index - 1]) {
            int tmp = nums[index];
            nums[index] = nums[index - 1];
            nums[index - 1] = tmp;
        } else if (index % 2 == 0 && nums[index] > nums[index - 1]) {
            int tmp = nums[index];
            nums[index] = nums[index - 1];
            nums[index - 1] = tmp;
        }
    }
}

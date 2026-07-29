// LeetCode 0905 - Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParity(int* nums, int numsSize, int* returnSize) {
    int i = 0;
    for (int j = 0; j < numsSize; j++) {
        if (nums[j] % 2 == 0) {
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
            i++;
        }
    }
    *returnSize = numsSize;
    return nums;
}

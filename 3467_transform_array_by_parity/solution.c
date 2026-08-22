// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* transformArray(int* nums, int numsSize, int* returnSize) {
    for (int i = 0; i < numsSize; i++) nums[i] %= 2;
    int j = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) {
            int t = nums[i];
            nums[i] = nums[j];
            nums[j] = t;
            j++;
        }
    }
    *returnSize = numsSize;
    return nums;
}

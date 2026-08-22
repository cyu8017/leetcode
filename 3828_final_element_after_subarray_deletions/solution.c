// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

int finalElement(int* nums, int numsSize) {
    int a = nums[0], b = nums[numsSize - 1];
    return a > b ? a : b;
}

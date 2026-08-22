// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

int minimumOperations(int* nums, int numsSize) {
    int ops = 0;
    for (int i = numsSize - 2; i >= 0; i--) if (nums[i] != nums[i + 1]) ops++;
    return ops;
}

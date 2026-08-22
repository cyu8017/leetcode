// LeetCode 3674 - Minimum Operations to Equalize Array
// https://leetcode.com/problems/minimum-operations-to-equalize-array/

int minOperations(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != nums[0]) return 1;
    }
    return 0;
}

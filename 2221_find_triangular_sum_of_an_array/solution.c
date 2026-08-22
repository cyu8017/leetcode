// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

int triangularSum(int* nums, int numsSize) {
    int n = numsSize;
    while (n > 1) {
        for (int i = 0; i < n - 1; i++) {
            nums[i] = (nums[i] + nums[i + 1]) % 10;
        }
        n--;
    }
    return nums[0];
}

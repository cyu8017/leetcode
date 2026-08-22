// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

int* reverseSubarrays(int* nums, int numsSize, int k, int* returnSize) {
    int n = numsSize;
    int m = n / k;
    for (int i = 0; i < n; i += m) {
        int l = i, r = i + m - 1;
        while (l < r) {
            int t = nums[l]; nums[l] = nums[r]; nums[r] = t;
            l++; r--;
        }
    }
    *returnSize = n;
    return nums;
}

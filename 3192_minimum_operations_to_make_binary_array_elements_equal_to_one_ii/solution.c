// LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

int minOperations(int* nums, int numsSize) {
    int ans = 0, v = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i] ^ v;
        if (x == 0) { v ^= 1; ans++; }
    }
    return ans;
}

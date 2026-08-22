// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

int evenNumberBitwiseORs(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 0) ans |= nums[i];
    }
    return ans;
}

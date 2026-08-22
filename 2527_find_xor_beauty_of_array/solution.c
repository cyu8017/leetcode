// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

int xorBeauty(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) ans ^= nums[i];
    return ans;
}

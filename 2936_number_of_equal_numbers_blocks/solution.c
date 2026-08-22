// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

int blockCount(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int ans = 1;
    for (int i = 1; i < numsSize; i++) if (nums[i] != nums[i - 1]) ans++;
    return ans;
}

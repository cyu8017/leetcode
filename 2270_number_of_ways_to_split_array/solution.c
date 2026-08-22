// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

int waysToSplitArray(int* nums, int numsSize) {
    long long total = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    long long left = 0;
    int ans = 0;
    for (int i = 0; i < numsSize - 1; i++) {
        left += nums[i];
        if (left >= total - left) ans++;
    }
    return ans;
}

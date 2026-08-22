// LeetCode 2348 - Number of Zero-Filled Subarrays
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

long long zeroFilledSubarray(int* nums, int numsSize) {
    long long ans = 0, streak = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) { streak++; ans += streak; }
        else streak = 0;
    }
    return ans;
}

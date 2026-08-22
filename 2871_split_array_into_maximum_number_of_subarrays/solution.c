// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

int maxSubarrays(int* nums, int numsSize) {
    int ans = 0, cur = -1;
    for (int i = 0; i < numsSize; i++) {
        if (cur == -1) cur = nums[i];
        else cur &= nums[i];
        if (cur == 0) { ans++; cur = -1; }
    }
    return ans == 0 ? 1 : ans;
}

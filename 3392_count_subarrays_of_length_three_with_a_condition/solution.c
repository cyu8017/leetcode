// LeetCode 3392 - Count Subarrays of Length Three With a Condition
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

int countSubarrays(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i + 2 < numsSize; i++)
        if (nums[i] * 2 + nums[i + 2] * 2 == nums[i + 1]) ans++;
    return ans;
}

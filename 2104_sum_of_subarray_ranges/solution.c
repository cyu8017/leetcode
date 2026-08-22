// LeetCode 2104 - Sum of Subarray Ranges
// https://leetcode.com/problems/sum-of-subarray-ranges/

long long subArrayRanges(int* nums, int numsSize) {
    long long ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int mn = nums[i], mx = nums[i];
        for (int j = i; j < numsSize; j++) {
            if (nums[j] < mn) mn = nums[j];
            if (nums[j] > mx) mx = nums[j];
            ans += (long long)(mx - mn);
        }
    }
    return ans;
}

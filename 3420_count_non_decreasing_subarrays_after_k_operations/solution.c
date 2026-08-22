// LeetCode 3420 - Count Non Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

long long countNonDecreasingSubarrays(int* nums, int numsSize, int k) {
    long long ans = 0;
    for (int i = 0; i < numsSize; i++) {
        long long cost = 0; int maxV = nums[i];
        for (int j = i; j < numsSize; j++) {
            if (nums[j] >= maxV) maxV = nums[j];
            else cost += maxV - nums[j];
            if (cost > k) break;
            ans++;
        }
    }
    return ans;
}

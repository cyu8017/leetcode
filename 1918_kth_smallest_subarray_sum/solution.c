// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

static int countAtMost(int* nums, int n, int limit) {
    int total = 0, left = 0, ans = 0;
    for (int right = 0; right < n; right++) {
        total += nums[right];
        while (total > limit) total -= nums[left++];
        ans += right - left + 1;
    }
    return ans;
}

int kthSmallestSubarraySum(int* nums, int numsSize, int k) {
    int lo = nums[0], hi = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < lo) lo = nums[i];
        hi += nums[i];
    }
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (countAtMost(nums, numsSize, mid) >= k) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

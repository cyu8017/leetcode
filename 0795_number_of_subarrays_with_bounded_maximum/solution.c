// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

int numSubarrayBoundedMax(int* nums, int numsSize, int left, int right) {
    int ans = 0, last1 = -1, last2 = -1;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] >= left && nums[i] <= right) last1 = i;
        else if (nums[i] > right) { last1 = -1; last2 = i; }
        if (last1 != -1) ans += last1 - last2;
    }
    return ans;
}

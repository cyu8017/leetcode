// LeetCode 2970 - Count the Number of Incremovable Subarrays I
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

int incremovableSubarrayCount(int* nums, int numsSize) {
    int n = numsSize;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int prev = -1;
            int ok = 1;
            for (int t = 0; t < n; t++) {
                if (t >= i && t <= j) continue;
                if (nums[t] <= prev) {
                    ok = 0;
                    break;
                }
                prev = nums[t];
            }
            if (ok) ans++;
        }
    }
    return ans;
}

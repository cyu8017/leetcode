// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

int minAbsoluteDifference(int* nums, int numsSize) {
    int n = numsSize;
    int ans = n + 1;
    int last[4];
    last[0] = last[1] = last[2] = last[3] = -ans;
    for (int i = 0; i < n; i++) {
        int x = nums[i];
        if (x != 0) {
            int d = i - last[3 - x];
            if (d < ans) ans = d;
            last[x] = i;
        }
    }
    if (ans > n) return -1;
    return ans;
}

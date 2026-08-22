// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

int maxSum(int* nums, int numsSize) {
    int best[10];
    for (int i = 0; i < 10; i++) best[i] = -1;
    int ans = -1;
    for (int i = 0; i < numsSize; i++) {
        int v = nums[i], x = v, md = 0;
        while (x > 0) {
            int d = x % 10;
            if (d > md) md = d;
            x /= 10;
        }
        if (best[md] >= 0) {
            if (best[md] + v > ans) ans = best[md] + v;
            if (v > best[md]) best[md] = v;
        } else best[md] = v;
    }
    return ans;
}

// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

static int gcd(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }

int minimumSplits(int* nums, int numsSize) {
    int ans = 1, g = nums[0];
    for (int i = 1; i < numsSize; i++) {
        int ng = gcd(g, nums[i]);
        if (ng == 1) { ans++; g = nums[i]; }
        else g = ng;
    }
    return ans;
}

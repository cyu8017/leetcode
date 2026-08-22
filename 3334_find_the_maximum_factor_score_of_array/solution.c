// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

static int gcd3334(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }
static int lcm3334(int a, int b) { return a / gcd3334(a, b) * b; }

long long maxScore(int* nums, int numsSize) {
    int n = numsSize;
    int gcdAll = nums[0], lcmAll = nums[0];
    for (int i = 1; i < n; i++) {
        gcdAll = gcd3334(gcdAll, nums[i]);
        lcmAll = lcm3334(lcmAll, nums[i]);
    }
    long long ans = (long long)gcdAll * lcmAll;
    for (int skip = 0; skip < n; skip++) {
        int g = 0, l = 1, first = 1;
        for (int i = 0; i < n; i++) {
            if (i == skip) continue;
            if (first) { g = l = nums[i]; first = 0; }
            else { g = gcd3334(g, nums[i]); l = lcm3334(l, nums[i]); }
        }
        if (first) continue;
        long long v = (long long)g * l;
        if (v > ans) ans = v;
    }
    return ans;
}

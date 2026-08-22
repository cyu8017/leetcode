// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

static int gcd2470(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

static int lcm2470(int a, int b) {
    return a / gcd2470(a, b) * b;
}

int subarrayLCM(int* nums, int numsSize, int k) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int cur = 1;
        for (int j = i; j < numsSize; j++) {
            cur = lcm2470(cur, nums[j]);
            if (cur > k) break;
            if (cur == k) ans++;
        }
    }
    return ans;
}

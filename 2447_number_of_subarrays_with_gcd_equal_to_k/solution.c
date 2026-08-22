// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

static int gcd2447(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int subarrayGCD(int* nums, int numsSize, int k) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int g = 0;
        for (int j = i; j < numsSize; j++) {
            g = gcd2447(g, nums[j]);
            if (g < k) break;
            if (g == k) ans++;
        }
    }
    return ans;
}

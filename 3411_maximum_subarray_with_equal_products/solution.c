// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

static int gcd3411(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }

int maxLength(int* nums, int numsSize) {
    int n = numsSize, ans = 1;
    for (int i = 0; i < n; i++) {
        long long prod = 1; int g = 0; long long l = 1;
        for (int j = i; j < n; j++) {
            if (prod > 1000000000LL / nums[j]) break;
            prod *= nums[j];
            if (g == 0) { g = nums[j]; l = nums[j]; }
            else {
                g = gcd3411(g, nums[j]);
                l = l / gcd3411((int)l, nums[j]) * nums[j];
            }
            if (prod == l * g && j - i + 1 > ans) ans = j - i + 1;
        }
    }
    return ans;
}

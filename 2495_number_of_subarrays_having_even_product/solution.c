// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

long long evenProduct(int* nums, int numsSize) {
    long long n = numsSize;
    long long total = n * (n + 1) / 2;
    long long oddLen = 0, odd = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 1) {
            odd++;
            oddLen += odd;
        } else odd = 0;
    }
    return total - oddLen;
}

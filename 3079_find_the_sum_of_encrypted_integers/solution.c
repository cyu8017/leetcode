// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

static int encrypt(int x) {
    int mx = 0, p = 0;
    for (; x > 0; x /= 10) {
        int d = x % 10;
        if (d > mx) mx = d;
        p = p * 10 + 1;
    }
    return mx * p;
}

int sumOfEncryptedInt(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) ans += encrypt(nums[i]);
    return ans;
}

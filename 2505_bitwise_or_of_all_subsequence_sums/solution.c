// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

long long subsequenceSumOr(int* nums, int numsSize) {
    long long ans = 0, prefix = 0;
    for (int i = 0; i < numsSize; i++) {
        prefix += nums[i];
        ans |= (long long)nums[i] | prefix;
    }
    return ans;
}

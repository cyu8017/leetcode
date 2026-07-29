// LeetCode 1911 - Maximum Alternating Subsequence Sum
// https://leetcode.com/problems/maximum-alternating-subsequence-sum/

long long maxAlternatingSum(int* nums, int numsSize) {
    long long even = 0, odd = 0;
    for (int i = 0; i < numsSize; i++) {
        long long x = nums[i];
        long long ne = even > odd + x ? even : odd + x;
        long long no = odd > even - x ? odd : even - x;
        even = ne;
        odd = no;
    }
    return even;
}

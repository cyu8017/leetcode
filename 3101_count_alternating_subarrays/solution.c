// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

long long countAlternatingSubarrays(int* nums, int numsSize) {
    long long ans = 1, s = 1;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[i - 1]) s++;
        else s = 1;
        ans += s;
    }
    return ans;
}

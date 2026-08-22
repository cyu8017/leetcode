// LeetCode 2366 - Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

long long minimumReplacement(int* nums, int numsSize) {
    long long ans = 0;
    int prev = nums[numsSize - 1];
    for (int i = numsSize - 2; i >= 0; i--) {
        if (nums[i] <= prev) { prev = nums[i]; continue; }
        int parts = (nums[i] + prev - 1) / prev;
        ans += parts - 1;
        prev = nums[i] / parts;
    }
    return ans;
}

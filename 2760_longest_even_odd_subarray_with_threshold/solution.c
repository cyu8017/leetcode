// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

int longestAlternatingSubarray(int* nums, int numsSize, int threshold) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 != 0 || nums[i] > threshold) continue;
        int j = i;
        while (j + 1 < numsSize && nums[j + 1] <= threshold && nums[j + 1] % 2 != nums[j] % 2) j++;
        if (j - i + 1 > ans) ans = j - i + 1;
    }
    return ans;
}

// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

int alternatingSubarray(int* nums, int numsSize) {
    int ans = -1;
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            int diff = j - i;
            int expect = (diff % 2 == 0) ? -1 : 1;
            if (nums[j] - nums[j - 1] != expect) break;
            if (nums[i + 1] - nums[i] != 1) break;
            if (j - i + 1 > ans) ans = j - i + 1;
        }
    }
    return ans;
}

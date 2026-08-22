// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

static int ans2044, maxOr2044, *nums2044, n2044;

static void dfs2044(int i, int cur) {
    if (i == n2044) {
        if (cur == maxOr2044) ans2044++;
        return;
    }
    dfs2044(i + 1, cur);
    dfs2044(i + 1, cur | nums2044[i]);
}

int countMaxOrSubsets(int* nums, int numsSize) {
    maxOr2044 = 0;
    for (int i = 0; i < numsSize; i++) maxOr2044 |= nums[i];
    ans2044 = 0; nums2044 = nums; n2044 = numsSize;
    dfs2044(0, 0);
    return ans2044;
}

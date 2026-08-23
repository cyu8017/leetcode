// LeetCode 3644 - Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

class Solution {
    public int sortPermutation(int[] nums) {
        int ans = -1;
        for (int i = 0; i < nums.length; i++)
            if (i != nums[i]) ans &= nums[i];
        return Math.max(ans, 0);
    }
}

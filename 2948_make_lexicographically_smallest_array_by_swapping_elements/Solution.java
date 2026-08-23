// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

import java.util.Arrays;

class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Integer.compare(nums[a], nums[b]));
        int[] ans = new int[n];
        for (int i = 0; i < n; ) {
            int j = i + 1;
            while (j < n && nums[idx[j]] - nums[idx[j - 1]] <= limit) j++;
            int[] groupIdx = new int[j - i];
            for (int t = 0; t < j - i; t++) groupIdx[t] = idx[i + t];
            Arrays.sort(groupIdx);
            for (int t = 0; t < j - i; t++) ans[groupIdx[t]] = nums[idx[i + t]];
            i = j;
        }
        return ans;
    }
}

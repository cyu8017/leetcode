// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

import java.util.Arrays;

class Solution {
    public long findScore(int[] nums) {
        int n = nums.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> {
            if (nums[a] != nums[b]) return Integer.compare(nums[a], nums[b]);
            return Integer.compare(a, b);
        });
        boolean[] marked = new boolean[n];
        long ans = 0;
        for (int i : idx) {
            if (marked[i]) continue;
            ans += nums[i];
            marked[i] = true;
            if (i - 1 >= 0) marked[i - 1] = true;
            if (i + 1 < n) marked[i + 1] = true;
        }
        return ans;
    }
}

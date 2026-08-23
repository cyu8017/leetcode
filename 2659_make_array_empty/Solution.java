// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

import java.util.*;

class Solution {
    public long countOperationsToEmptyArray(int[] nums) {
        int n = nums.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, Comparator.comparingInt(a -> nums[a]));
        long ans = n;
        for (int i = 1; i < n; i++)
            if (idx[i] < idx[i - 1]) ans += n - i;
        return ans;
    }
}

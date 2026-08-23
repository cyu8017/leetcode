// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

import java.util.*;

class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length;
        int[] uniq = Arrays.stream(nums).distinct().sorted().toArray();
        int ans = n, j = 0;
        for (int i = 0; i < uniq.length; i++) {
            while (j < uniq.length && uniq[j] - uniq[i] + 1 <= n) j++;
            ans = Math.min(ans, n - (j - i));
        }
        return ans;
    }
}

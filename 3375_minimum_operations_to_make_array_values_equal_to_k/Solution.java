// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minOperations(int[] nums, int k) {
        var seen = new HashSet<Integer>();
        for (int x : nums) {
            if (x < k) return -1;
            if (x > k) seen.add(x);
        }
        return seen.size();
    }
}

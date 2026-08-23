// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minimumOperations(int[] nums) {
        var seen = new HashSet<>();
        for (int x : nums) if (x > 0) seen.add(x);
        return seen.size();
    }
}

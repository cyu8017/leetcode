// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int findMaxK(int[] nums) {
        var seen = new HashSet<Integer>();
        int ans = -1;
        for (int x : nums) {
            seen.add(x);
            if (x > 0 && seen.contains(-x) && x > ans) ans = x;
            if (x < 0 && seen.contains(-x) && -x > ans) ans = -x;
        }
        return ans;
    }
}

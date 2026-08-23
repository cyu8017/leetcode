// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int longestSquareStreak(int[] nums) {
        var set = new HashSet<Long>();
        for (int x : nums) set.add(x);
        int best = -1;
        for (int x : nums) {
            if (!set.contains(x)) continue;
            int length = 0;
            long cur = x;
            while (set.contains(cur)) {
                length++;
                set.remove(cur);
                if (cur > 100000) break;
                cur = cur * cur;
            }
            if (length >= 2 && length > best) best = length;
        }
        return best;
    }
}

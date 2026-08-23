// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

using System.Collections.Generic;

public class Solution {
    public int LongestSquareStreak(int[] nums) {
        var set = new HashSet<long>();
        foreach (int x in nums) set.Add(x);
        int best = -1;
        foreach (int x in nums) {
            if (!set.Contains(x)) continue;
            int length = 0;
            long cur = x;
            while (set.Contains(cur)) {
                length++;
                set.Remove(cur);
                if (cur > 100000) break;
                cur = cur * cur;
            }
            if (length >= 2 && length > best) best = length;
        }
        return best;
    }
}

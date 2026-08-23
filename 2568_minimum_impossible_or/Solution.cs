// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

using System.Collections.Generic;

public class Solution {
    public int MinImpossibleOR(int[] nums) {
        var set = new HashSet<int>(nums);
        for (int i = 1; ; i <<= 1) {
            if (!set.Contains(i)) return i;
        }
    }
}

// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

using System.Collections.Generic;

public class Solution {
    public int MissingMultiple(int[] nums, int k) {
        var s = new HashSet<int>(nums);
        for (int i = 1; ; i++) {
            int x = k * i;
            if (!s.Contains(x)) return x;
        }
    }
}

// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

using System.Collections.Generic;

public class Solution {
    public int MinimumOperations(int[] nums) {
        var list = new List<int>(nums);
        int ops = 0;
        while (true) {
            var seen = new HashSet<int>();
            bool dup = false;
            foreach (int x in list) {
                if (!seen.Add(x)) { dup = true; break; }
            }
            if (!dup) return ops;
            if (list.Count <= 3) return ops + 1;
            list.RemoveRange(0, 3);
            ops++;
        }
    }
}

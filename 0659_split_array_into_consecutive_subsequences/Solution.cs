// LeetCode 0659 - Split Array into Consecutive Subsequences
// https://leetcode.com/problems/split-array-into-consecutive-subsequences/

using System.Collections.Generic;

public class Solution {
    public bool IsPossible(int[] nums) {
        var freq = new Dictionary<int, int>();
        var tails = new Dictionary<int, int>();
        foreach (int num in nums) {
            freq.TryGetValue(num, out int c);
            freq[num] = c + 1;
        }
        foreach (int num in nums) {
            if (!freq.TryGetValue(num, out int f) || f == 0) continue;
            freq[num] = f - 1;
            tails.TryGetValue(num - 1, out int t);
            if (t > 0) {
                tails[num - 1] = t - 1;
                tails.TryGetValue(num, out int tn);
                tails[num] = tn + 1;
            } else {
                freq.TryGetValue(num + 1, out int f1);
                freq.TryGetValue(num + 2, out int f2);
                if (f1 > 0 && f2 > 0) {
                    freq[num + 1] = f1 - 1;
                    freq[num + 2] = f2 - 1;
                    tails.TryGetValue(num + 2, out int tn);
                    tails[num + 2] = tn + 1;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}

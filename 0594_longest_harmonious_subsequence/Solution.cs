// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/

using System.Collections.Generic;

public class Solution {
    public int FindLHS(int[] nums) {
        var counts = new Dictionary<int, int>();
        foreach (int num in nums) {
            counts.TryGetValue(num, out int c);
            counts[num] = c + 1;
        }
        int best = 0;
        foreach (var kv in counts) {
            if (counts.TryGetValue(kv.Key + 1, out int next)) {
                int total = kv.Value + next;
                if (total > best) best = total;
            }
        }
        return best;
    }
}

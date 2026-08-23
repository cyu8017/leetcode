// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

using System.Collections.Generic;

public class Solution {
    public int ShortestSequence(int[] rolls, int k) {
        var seen = new HashSet<int>();
        int ans = 1;
        foreach (int r in rolls) {
            seen.Add(r);
            if (seen.Count == k) {
                ans++;
                seen.Clear();
            }
        }
        return ans;
    }
}

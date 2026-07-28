// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int LastStoneWeightII(int[] stones) {
        int total = stones.Sum();
        var reachable = new HashSet<int> { 0 };
        foreach (int stone in stones) {
            var next = new HashSet<int>(reachable);
            foreach (int s in reachable) next.Add(s + stone);
            reachable = next;
        }
        int best = int.MaxValue;
        foreach (int s in reachable) best = Math.Min(best, Math.Abs(total - 2 * s));
        return best;
    }
}

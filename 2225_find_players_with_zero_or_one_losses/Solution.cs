// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> FindWinners(int[][] matches) {
        var lose = new Dictionary<int, int>();
        var seen = new HashSet<int>();
        foreach (var m in matches) {
            seen.Add(m[0]);
            seen.Add(m[1]);
            lose.TryGetValue(m[1], out int c);
            lose[m[1]] = c + 1;
        }
        var zero = new List<int>();
        var one = new List<int>();
        foreach (int p in seen) {
            lose.TryGetValue(p, out int L);
            if (L == 0) zero.Add(p);
            else if (L == 1) one.Add(p);
        }
        zero.Sort();
        one.Sort();
        return new List<IList<int>> { zero, one };
    }
}

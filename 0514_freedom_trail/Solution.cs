// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

using System.Collections.Generic;

public class Solution {
    public int FindRotateSteps(string ring, string key) {
        Dictionary<char, List<int>> positions = new Dictionary<char, List<int>>();
        for (int index = 0; index < ring.Length; index++) {
            if (!positions.ContainsKey(ring[index])) {
                positions[ring[index]] = new List<int>();
            }
            positions[ring[index]].Add(index);
        }
        Dictionary<string, int> memo = new Dictionary<string, int>();
        return Dp(0, 0, ring, key, positions, memo);
    }

    private int Dp(int ringIndex, int keyIndex, string ring, string key,
                   Dictionary<char, List<int>> positions, Dictionary<string, int> memo) {
        if (keyIndex == key.Length) {
            return 0;
        }
        string state = ringIndex + "," + keyIndex;
        if (memo.TryGetValue(state, out int cached)) {
            return cached;
        }
        int best = int.MaxValue;
        foreach (int pos in positions[key[keyIndex]]) {
            int clockwise = (pos - ringIndex + ring.Length) % ring.Length;
            int counter = (ringIndex - pos + ring.Length) % ring.Length;
            int steps = System.Math.Min(clockwise, counter) + 1;
            best = System.Math.Min(best, steps + Dp(pos, keyIndex + 1, ring, key, positions, memo));
        }
        memo[state] = best;
        return best;
    }
}

// LeetCode 1320 - Minimum Distance To Type A Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

using System.Collections.Generic;

public class Solution {
    public int MinimumDistance(string word) {
        int Distance(int a, int b) {
            if (a == 26) return 0;
            return System.Math.Abs(a / 6 - b / 6) + System.Math.Abs(a % 6 - b % 6);
        }
        var letters = new int[word.Length];
        for (int i = 0; i < word.Length; i++) letters[i] = word[i] - 'A';
        var dp = new Dictionary<int, int> { [26] = 0 };
        int previous = letters[0];
        for (int idx = 1; idx < letters.Length; idx++) {
            int current = letters[idx];
            var nxt = new Dictionary<int, int>();
            foreach (var kv in dp) {
                int free = kv.Key, cost = kv.Value;
                int v1 = cost + Distance(previous, current);
                if (!nxt.ContainsKey(free) || v1 < nxt[free]) nxt[free] = v1;
                int v2 = cost + Distance(free, current);
                if (!nxt.ContainsKey(previous) || v2 < nxt[previous]) nxt[previous] = v2;
            }
            dp = nxt;
            previous = current;
        }
        int ans = int.MaxValue;
        foreach (int v in dp.Values) ans = System.Math.Min(ans, v);
        return ans;
    }
}

// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

using System.Collections.Generic;

public class Solution {
    public int OpenLock(string[] deadends, string target) {
        var dead = new HashSet<string>(deadends);
        if (dead.Contains("0000")) return -1;
        var q = new Queue<(string, int)>();
        var seen = new HashSet<string> { "0000" };
        q.Enqueue(("0000", 0));
        while (q.Count > 0) {
            var (state, steps) = q.Dequeue();
            if (state == target) return steps;
            char[] chars = state.ToCharArray();
            for (int i = 0; i < 4; i++) {
                int digit = chars[i] - '0';
                foreach (int delta in new[] { -1, 1 }) {
                    chars[i] = (char)('0' + (digit + delta + 10) % 10);
                    string nxt = new string(chars);
                    chars[i] = (char)('0' + digit);
                    if (seen.Add(nxt) && !dead.Contains(nxt)) q.Enqueue((nxt, steps + 1));
                }
            }
        }
        return -1;
    }
}

// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

using System.Collections.Generic;

public class Solution {
    public IList<string> SplitMessage(string message, int limit) {
        int n = message.Length;
        for (int parts = 1; parts <= n; parts++) {
            int sbDigits = parts.ToString().Length;
            bool ok = true;
            int idx = 0;
            var res = new List<string>();
            for (int i = 1; i <= parts; i++) {
                int tail = 3 + i.ToString().Length + sbDigits;
                int cap = limit - tail;
                if (cap <= 0 || idx >= n) {
                    ok = false;
                    break;
                }
                int take = cap;
                if (take > n - idx) take = n - idx;
                res.Add(message.Substring(idx, take) + "<" + i + "/" + parts + ">");
                idx += take;
            }
            if (ok && idx == n) return res;
        }
        return new List<string>();
    }
}

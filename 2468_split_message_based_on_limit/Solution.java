// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> splitMessage(String message, int limit) {
        int n = message.length();
        for (int parts = 1; parts <= n; parts++) {
            int sbDigits = parts.toString().length;
            boolean ok = true;
            int idx = 0;
            var res = new ArrayList<String>();
            for (int i = 1; i <= parts; i++) {
                int tail = 3 + i.toString().length + sbDigits;
                int cap = limit - tail;
                if (cap <= 0 || idx >= n) {
                    ok = false;
                    break;
                }
                int take = cap;
                if (take > n - idx) take = n - idx;
                res.add(message.substring(idx, take) + "<" + i + "/" + parts + ">");
                idx += take;
            }
            if (ok && idx == n) return res;
        }
        return new ArrayList<String>();
    }
}

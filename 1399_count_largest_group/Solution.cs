// LeetCode 1399 - Count Largest Group
// https://leetcode.com/problems/count-largest-group/

using System.Collections.Generic;
public class Solution {
    public int CountLargestGroup(int n) {
        var c = new Dictionary<int, int>();
        for (int x = 1; x <= n; x++) {
            int s = 0, t = x;
            while (t > 0) { s += t % 10; t /= 10; }
            if (!c.ContainsKey(s)) c[s] = 0; c[s]++;
        }
        int m = 0, ans = 0;
        foreach (int v in c.Values) m = System.Math.Max(m, v);
        foreach (int v in c.Values) if (v == m) ans++;
        return ans;
    }
}

// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumWidth(int[] planks) {
        var cnt = new Dictionary<int, int>();
        foreach (int x in planks) {
            if (!cnt.ContainsKey(x)) cnt[x] = 0;
            cnt[x]++;
        }
        var t = new Dictionary<int, int>();
        int ans = 0;
        foreach (var kv in cnt) {
            int x = kv.Key, v1 = kv.Value;
            if (!t.ContainsKey(x)) t[x] = 0;
            t[x] += v1;
            ans = Math.Max(ans, t[x]);
            if (!t.ContainsKey(x * 2)) t[x * 2] = 0;
            t[x * 2] += v1 / 2;
            ans = Math.Max(ans, t[x * 2]);
            foreach (var kv2 in cnt) {
                int y = kv2.Key, v2 = kv2.Value;
                if (y > x) {
                    int key = x + y;
                    if (!t.ContainsKey(key)) t[key] = 0;
                    t[key] += Math.Min(v1, v2);
                    ans = Math.Max(ans, t[key]);
                }
            }
        }
        return ans;
    }
}

// LeetCode 1394 - Find Lucky Integer In An Array
// https://leetcode.com/problems/find-lucky-integer-in-an-array/

using System.Collections.Generic;
public class Solution {
    public int FindLucky(int[] arr) {
        var c = new Dictionary<int, int>();
        foreach (int x in arr) { if (!c.ContainsKey(x)) c[x] = 0; c[x]++; }
        int ans = -1;
        foreach (var kv in c) if (kv.Key == kv.Value) ans = System.Math.Max(ans, kv.Key);
        return ans;
    }
}

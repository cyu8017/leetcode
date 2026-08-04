// LeetCode 1394 - Find Lucky Integer In An Array
// https://leetcode.com/problems/find-lucky-integer-in-an-array/

import java.util.*;

class Solution {
    public int findLucky(int[] arr) {
        var c = new HashMap<>();
        for (int x : arr) { if (!c.containsKey(x)) c[x] = 0; c[x]++; }
        int ans = -1;
        for (var kv : c) if (kv.Key == kv.Value) ans = Math.max(ans, kv.Key);
        return ans;
    }
}

// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isPossibleToRearrange(String s, String t, int k) {
        int n = s.length();
        int sz = n / k;
        var cnt = new HashMap<String, Integer>();
        for (int i = 0; i < n; i += sz) {
            String a = s.substring(i, sz), b = t.substring(i, sz);
            if (!cnt.containsKey(a)) cnt.put(a, 0);
            cnt.put(a, cnt.get(a) + 1);
            if (!cnt.containsKey(b)) cnt.put(b, 0);
            cnt.put(b, cnt.get(b) - 1);
        }
        for (var v : cnt.values()) if (v != 0) return false;
        return true;
    }
}

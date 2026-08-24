// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean matchReplacement(String s, String sub, char[][] mappings) {
        var allow = new HashSet<Integer>();
        for (var m : mappings) allow.add((m[0] << 8) | m[1]);
        int n = s.length(), mlen = sub.length();
        for (int i = 0; i + mlen <= n; i++) {
            boolean ok = true;
            for (int j = 0; j < mlen; j++) {
                char a = s.charAt(i + j), b = sub.charAt(j);
                if (a == b || allow.contains((b << 8) | a)) continue;
                ok = false;
                break;
            }
            if (ok) return true;
        }
        return false;
    }
}

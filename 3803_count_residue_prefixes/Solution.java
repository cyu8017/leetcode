// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int residuePrefixes(String s) {
        var st = new HashSet<Character>();
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            st.add(s.charAt(i));
            if (st.size() == (i + 1) % 3) ans++;
        }
        return ans;
    }
}

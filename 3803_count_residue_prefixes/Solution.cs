// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

using System.Collections.Generic;

public class Solution {
    public int ResiduePrefixes(string s) {
        var st = new HashSet<char>();
        int ans = 0;
        for (int i = 0; i < s.Length; i++) {
            st.Add(s[i]);
            if (st.Count == (i + 1) % 3) ans++;
        }
        return ans;
    }
}

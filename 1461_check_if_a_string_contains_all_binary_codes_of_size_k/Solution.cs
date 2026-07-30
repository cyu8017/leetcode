// LeetCode 1461 - Check If A String Contains All Binary Codes Of Size K
// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

using System.Collections.Generic;
public class Solution {
    public bool HasAllCodes(string s, int k) {
        var set = new HashSet<string>();
        for (int i = 0; i <= s.Length - k; i++) set.Add(s.Substring(i, k));
        return set.Count == (1 << k);
    }
}

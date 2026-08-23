// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

using System.Collections.Generic;

public class Solution {
    public IList<string> TwoEditWords(string[] queries, string[] dictionary) {
        var ans = new List<string>();
        foreach (string q in queries) {
            bool ok = false;
            foreach (string d in dictionary) {
                int diff = 0;
                for (int i = 0; i < q.Length; i++) {
                    if (q[i] != d[i]) {
                        if (++diff > 2) break;
                    }
                }
                if (diff <= 2) {
                    ok = true;
                    break;
                }
            }
            if (ok) ans.Add(q);
        }
        return ans;
    }
}

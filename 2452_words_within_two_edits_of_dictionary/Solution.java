// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> twoEditWords(String[] queries, String[] dictionary) {
        var ans = new ArrayList<String>();
        for (String q : queries) {
            boolean ok = false;
            for (String d : dictionary) {
                int diff = 0;
                for (int i = 0; i < q.length(); i++) {
                    if (q.charAt(i) != d.charAt(i)) {
                        if (++diff > 2) break;
                    }
                }
                if (diff <= 2) {
                    ok = true;
                    break;
                }
            }
            if (ok) ans.add(q);
        }
        return ans;
    }
}

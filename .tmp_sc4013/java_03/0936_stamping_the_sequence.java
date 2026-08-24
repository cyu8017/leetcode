// LeetCode 0936 - Stamping The Sequence
// https://leetcode.com/problems/stamping-the-sequence/

import java.util.*;

class Solution {
    public int[] movesToStamp(String stamp, String target) {
        int n = target.length(), m = stamp.length();
        boolean[] done = new boolean[n];
        List<Integer> ans = new ArrayList<>();
        boolean changed = true;
        while (changed) {
            changed = false;
            for (int i = n - m; i >= 0; i--) {
                boolean ok = true, any = false;
                for (int j = 0; j < m; j++) {
                    if (!done[i + j] && target.charAt(i + j) != stamp.charAt(j)) { ok = false; break; }
                    if (!done[i + j]) any = true;
                }
                if (ok && any) {
                    for (int j = 0; j < m; j++) done[i + j] = true;
                    ans.add(i);
                    changed = true;
                    break;
                }
            }
        }
        for (boolean d : done) if (!d) return new int[0];
        Collections.reverse(ans);
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }
}

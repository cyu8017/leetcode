// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int minOperations(String s1, String s2, int x) {
        List<Integer> diff = new ArrayList<>();
        for (int i = 0; i < s1.length(); i++)
            if (s1.charAt(i) != s2.charAt(i)) diff.add(i);
        int m = diff.size();
        if (m % 2 == 1) return -1;
        if (m == 0) return 0;
        int[] dp2 = new int[m + 1];
        for (int i = 0; i <= m; i++) dp2[i] = 1 << 30;
        dp2[0] = 0;
        for (int i = 0; i < m; i++) {
            if (dp2[i] >= (1 << 30)) continue;
            if (i + 1 < m) {
                int cand = diff.get(i + 1) - diff.get(i);
                if (cand > x) cand = x;
                if (dp2[i] + cand < dp2[i + 2]) dp2[i + 2] = dp2[i] + cand;
            }
        }
        return dp2[m] >= (1 << 30) ? -1 : dp2[m];
    }
}

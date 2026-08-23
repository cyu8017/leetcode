// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int possibleStringCount(String word, int k) {
        final int mod = 1000000007;
        var groups = new ArrayList<Integer>();
        for (int i = 0; i < word.length(); ) {
            int j = i;
            while (j < word.length() && word.charAt(j) == word.charAt(i)) j++;
            groups.add(j - i);
            i = j;
        }
        int total = 1;
        for (int g : groups) total = (int)((long)total * g % mod);
        if (k <= groups.size()) return total;
        int need = k - 1;
        int[] dp = new int[need];
        dp[0] = 1;
        for (int g : groups) {
            int[] ndp = new int[need];
            int[] pref = new int[need + 1];
            for (int i = 0; i < need; i++) pref[i + 1] = (pref[i] + dp[i]) % mod;
            for (int s = 0; s < need; s++) {
                int lo = s - g;
                if (lo < 0) lo = 0;
                int hi = s - 1;
                if (hi >= 0) ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod;
            }
            dp = ndp;
        }
        int bad = 0;
        for (int v : dp) bad = (bad + v) % mod;
        return (total - bad + mod) % mod;
    }
}

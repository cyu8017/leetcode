// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    private int lcpOf(List<String> a) {
        if (a.isEmpty()) return 0;
        String pref = a.get(0);
        for (int t = 1; t < a.size(); t++) {
            String s = a.get(t);
            int i = 0;
            while (i < pref.length() && i < s.length() && pref.charAt(i) == s.charAt(i)) i++;
            pref = pref.substring(0, i);
            if (pref.isEmpty()) return 0;
        }
        return pref.length();
    }

    public int[] longestCommonPrefix(String[] words, int k) {
        int n = words.length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            List<String> rest = new ArrayList<>();
            for (int j = 0; j < n; j++) if (j != i) rest.add(words[j]);
            if (rest.size() < k) { ans[i] = 0; continue; }
            Collections.sort(rest);
            int best = 0;
            for (int j = 0; j + k - 1 < rest.size(); j++) {
                List<String> window = rest.subList(j, j + k);
                best = Math.max(best, lcpOf(window));
            }
            ans[i] = best;
        }
        return ans;
    }
}

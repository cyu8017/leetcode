// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

import java.util.*;

class Solution {
    public int expressiveWords(String s, String[] words) {
        List<int[]> target = groups(s);
        int ans = 0;
        for (String word : words) {
            List<int[]> source = groups(word);
            if (source.size() != target.size()) continue;
            boolean ok = true;
            for (int i = 0; i < source.size(); i++) {
                if (source.get(i)[0] != target.get(i)[0]) { ok = false; break; }
                int c1 = source.get(i)[1], c2 = target.get(i)[1];
                if (c1 > c2 || (c1 != c2 && c2 < 3)) { ok = false; break; }
            }
            if (ok) ans++;
        }
        return ans;
    }

    private List<int[]> groups(String text) {
        List<int[]> result = new ArrayList<>();
        int i = 0, n = text.length();
        while (i < n) {
            int j = i;
            while (j < n && text.charAt(j) == text.charAt(i)) j++;
            result.add(new int[] {text.charAt(i), j - i});
            i = j;
        }
        return result;
    }
}

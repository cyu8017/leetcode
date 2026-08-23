// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private int[] sig(String w) {
        int[] c = new int[26];
        for (char ch : w.toCharArray()) c[ch - 'a']++;
        return c;
    }

    private boolean eq(int[] a, int[] b) {
        for (int i = 0; i < 26; i++) if (a[i] != b[i]) return false;
        return true;
    }

    public List<String> removeAnagrams(String[] words) {
        List<String> ans = new ArrayList<>();
        ans.add(words[0]);
        int[] prev = sig(words[0]);
        for (int i = 1; i < words.length; i++) {
            int[] cur = sig(words[i]);
            if (!eq(cur, prev)) {
                ans.add(words[i]);
                prev = cur;
            }
        }
        return ans;
    }
}

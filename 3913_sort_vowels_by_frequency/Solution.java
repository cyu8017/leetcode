// LeetCode 3913 - Sort Vowels By Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public String sortVowels(String s) {
        Set<Character> st = new HashSet<>();
        for (char c : new char[] { 'a', 'e', 'i', 'o', 'u' }) st.add(c);
        List<Character> vowels = new ArrayList<>();
        Map<Character, Integer> cnt = new HashMap<>();
        for (char c : s.toCharArray()) {
            if (!st.contains(c)) continue;
            if (!cnt.containsKey(c)) { vowels.add(c); cnt.put(c, 0); }
            cnt.put(c, cnt.get(c) + 1);
        }
        vowels.sort((a, b) -> Integer.compare(cnt.get(b), cnt.get(a)));
        char[] ans = s.toCharArray();
        int i = 0;
        for (int k = 0; k < s.length(); k++) {
            if (!st.contains(s.charAt(k))) continue;
            char ch = vowels.get(i);
            ans[k] = ch;
            cnt.put(ch, cnt.get(ch) - 1);
            if (cnt.get(ch) == 0) i++;
        }
        return new String(ans);
    }
}

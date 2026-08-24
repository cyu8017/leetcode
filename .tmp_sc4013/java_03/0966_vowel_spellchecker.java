// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

import java.util.*;

class Solution {
    public String[] spellchecker(String[] wordlist, String[] queries) {
        Set<String> exact = new HashSet<>(Arrays.asList(wordlist));
        Map<String, String> lowerMap = new HashMap<>();
        Map<String, String> vowelMap = new HashMap<>();
        for (String w : wordlist) {
            String low = w.toLowerCase(Locale.ROOT);
            lowerMap.putIfAbsent(low, w);
            vowelMap.putIfAbsent(devowel(w), w);
        }
        String[] ans = new String[queries.length];
        for (int i = 0; i < queries.length; i++) {
            String q = queries[i];
            if (exact.contains(q)) ans[i] = q;
            else if (lowerMap.containsKey(q.toLowerCase(Locale.ROOT))) ans[i] = lowerMap.get(q.toLowerCase(Locale.ROOT));
            else if (vowelMap.containsKey(devowel(q))) ans[i] = vowelMap.get(devowel(q));
            else ans[i] = "";
        }
        return ans;
    }

    private String devowel(String w) {
        char[] chars = w.toLowerCase(Locale.ROOT).toCharArray();
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') chars[i] = '*';
        }
        return new String(chars);
    }
}

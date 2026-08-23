// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

import java.util.*;

class Solution {
    public int countVowelSubstrings(String word) {
        int ans = 0, n = word.length();
        for (int i = 0; i < n; i++) {
            Set<Character> seen = new HashSet<>();
            for (int j = i; j < n && isVowel(word.charAt(j)); j++) {
                seen.add(word.charAt(j));
                if (seen.size() == 5) ans++;
            }
        }
        return ans;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}

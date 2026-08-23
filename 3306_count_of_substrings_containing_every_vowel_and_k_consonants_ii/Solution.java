// LeetCode 3306 - Count of Substrings Containing Every Vowel and K Consonants II
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    private int atLeast(String word, int k) {
        Map<Character, Integer> cnt = new HashMap<>();
        int cons = 0, l = 0, ans = 0;
        for (int r = 0; r < word.length(); r++) {
            char c = word.charAt(r);
            if (isVowel(c)) cnt.merge(c, 1, Integer::sum);
            else cons++;
            while (cnt.size() == 5 && cons >= k) {
                ans += word.length() - r;
                char c2 = word.charAt(l);
                if (isVowel(c2)) {
                    int nv = cnt.get(c2) - 1;
                    if (nv == 0) cnt.remove(c2);
                    else cnt.put(c2, nv);
                } else cons--;
                l++;
            }
        }
        return ans;
    }

    public long countOfSubstrings(String word, int k) {
        return (long) atLeast(word, k) - atLeast(word, k + 1);
    }
}

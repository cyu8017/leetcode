// LeetCode 1935 - Maximum Number of Words You Can Type
// https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        boolean[] broken = new boolean[26];
        for (int i = 0; i < brokenLetters.length(); i++) broken[brokenLetters.charAt(i) - 'a'] = true;
        int ans = 0;
        for (String w : text.split(" ")) {
            boolean ok = true;
            for (int i = 0; i < w.length(); i++) {
                if (broken[w.charAt(i) - 'a']) { ok = false; break; }
            }
            if (ok) ans++;
        }
        return ans;
    }
}

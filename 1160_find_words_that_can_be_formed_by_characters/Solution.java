// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution {
    public int countCharacters(String[] words, String chars) {
        int[] avail = new int[26];
        for (char c : chars.toCharArray()) avail[c - 'a']++;
        int ans = 0;
        for (String word : words) {
            int[] need = new int[26];
            boolean ok = true;
            for (char c : word.toCharArray()) {
                if (++need[c - 'a'] > avail[c - 'a']) { ok = false; break; }
            }
            if (ok) ans += word.length();
        }
        return ans;
    }
}

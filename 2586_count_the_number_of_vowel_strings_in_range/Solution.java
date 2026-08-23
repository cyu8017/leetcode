// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        int ans = 0;
        for (int i = left; i <= right; ++i) {
            String w = words[i];
            if (isV(w.charAt(0)) && isV(w.charAt(w.length() - 1))) ans++;
        }
        return ans;
    }

    private boolean isV(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}

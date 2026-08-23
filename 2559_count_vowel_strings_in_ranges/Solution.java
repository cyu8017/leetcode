// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        int n = words.length;
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i];
            String w = words[i];
            if (w.length() > 0 && isV(w.charAt(0)) && isV(w.charAt(w.length() - 1))) pref[i + 1]++;
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; ++i) {
            ans[i] = pref[queries[i][1] + 1] - pref[queries[i][0]];
        }
        return ans;
    }

    private boolean isV(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}

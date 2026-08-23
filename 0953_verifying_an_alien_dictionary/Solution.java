// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution {
    private int[] rank = new int[26];

    public boolean isAlienSorted(String[] words, String order) {
        for (int i = 0; i < 26; i++) rank[order.charAt(i) - 'a'] = i;
        for (int i = 0; i + 1 < words.length; i++)
            if (!lessEq(words[i], words[i + 1])) return false;
        return true;
    }

    private boolean lessEq(String a, String b) {
        int n = Math.min(a.length(), b.length());
        for (int i = 0; i < n; i++) {
            if (rank[a.charAt(i) - 'a'] != rank[b.charAt(i) - 'a'])
                return rank[a.charAt(i) - 'a'] < rank[b.charAt(i) - 'a'];
        }
        return a.length() <= b.length();
    }
}

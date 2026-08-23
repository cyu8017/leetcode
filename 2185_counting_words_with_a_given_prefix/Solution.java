// LeetCode 2185 - Counting Words With a Given Prefix
// https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution {
    public int prefixCount(String[] words, String pref) {
        int ans = 0;
        for (String w : words)
            if (w.length() >= pref.length() && w.startsWith(pref)) ans++;
        return ans;
    }
}

// LeetCode 2114 - Maximum Number of Words Found in Sentences
// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution {
    public int mostWordsFound(String[] sentences) {
        int ans = 0;
        for (String s : sentences) {
            int c = 1;
            for (int i = 0; i < s.length(); i++) if (s.charAt(i) == ' ') c++;
            ans = Math.max(ans, c);
        }
        return ans;
    }
}

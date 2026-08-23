// LeetCode 0758 - Bold Words in String
// https://leetcode.com/problems/bold-words-in-string/

class Solution {
    public String boldWords(String[] words, String s) {
        int n = s.length();
        boolean[] bold = new boolean[n];
        for (String word : words) {
            int start = s.indexOf(word);
            while (start >= 0) {
                for (int i = start; i < start + word.length(); i++) bold[i] = true;
                start = s.indexOf(word, start + 1);
            }
        }
        StringBuilder parts = new StringBuilder();
        int i2 = 0;
        while (i2 < n) {
            if (bold[i2]) {
                parts.append("**");
                while (i2 < n && bold[i2]) parts.append(s.charAt(i2++));
                parts.append("**");
            } else parts.append(s.charAt(i2++));
        }
        return parts.toString();
    }
}

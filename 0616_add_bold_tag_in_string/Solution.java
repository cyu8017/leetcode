// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/

class Solution {
    public String addBoldTag(String s, String[] words) {
        int n = s.length();
        boolean[] bold = new boolean[n];
        for (String word : words) {
            int start = s.indexOf(word);
            while (start >= 0) {
                for (int i = start; i < start + word.length(); ++i) {
                    bold[i] = true;
                }
                start = s.indexOf(word, start + 1);
            }
        }
        StringBuilder parts = new StringBuilder();
        int i = 0;
        while (i < n) {
            if (bold[i]) {
                parts.append("<b>");
                while (i < n && bold[i]) {
                    parts.append(s.charAt(i++));
                }
                parts.append("</b>");
            } else {
                parts.append(s.charAt(i++));
            }
        }
        return parts.toString();
    }
}

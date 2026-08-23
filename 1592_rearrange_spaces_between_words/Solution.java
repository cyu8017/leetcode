// LeetCode 1592 - Rearrange Spaces Between Words
// https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution {
    public String reorderSpaces(String text) {
        String[] words = text.trim().split("\\s+");
        int spaces = 0;
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == ' ') {
                spaces++;
            }
        }
        if (words.length <= 1) {
            return (words.length == 0 ? "" : words[0]) + " ".repeat(spaces);
        }
        int between = spaces / (words.length - 1);
        int trailing = spaces % (words.length - 1);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            if (i > 0) {
                sb.append(" ".repeat(between));
            }
            sb.append(words[i]);
        }
        sb.append(" ".repeat(trailing));
        return sb.toString();
    }
}

// LeetCode 1717 - Maximum Score From Removing Substrings
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution {
    public int maximumGain(String s, int x, int y) {
        int first;
        int second;
        StringBuilder rest = new StringBuilder();
        if (x >= y) {
            first = remove(s, 'a', 'b', x, rest);
            second = remove(rest.toString(), 'b', 'a', y, new StringBuilder());
        } else {
            first = remove(s, 'b', 'a', y, rest);
            second = remove(rest.toString(), 'a', 'b', x, new StringBuilder());
        }
        return first + second;
    }

    private int remove(String text, char open, char close, int score, StringBuilder rest) {
        int gained = 0;
        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);
            if (rest.length() > 0 && rest.charAt(rest.length() - 1) == open && ch == close) {
                rest.deleteCharAt(rest.length() - 1);
                gained += score;
            } else {
                rest.append(ch);
            }
        }
        return gained;
    }
}

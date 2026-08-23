// LeetCode 0557 - Reverse Words in a String III
// https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution {
    public String reverseWords(String s) {
        char[] chars = s.toCharArray();
        int n = chars.length;
        int start = 0;
        for (int i = 0; i <= n; ++i) {
            if (i == n || chars[i] == ' ') {
                reverse(chars, start, i - 1);
                start = i + 1;
            }
        }
        return new String(chars);
    }

    private void reverse(char[] chars, int left, int right) {
        while (left < right) {
            char tmp = chars[left];
            chars[left] = chars[right];
            chars[right] = tmp;
            ++left;
            --right;
        }
    }
}

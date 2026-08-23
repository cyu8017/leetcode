// LeetCode 2000 - Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

class Solution {
    public String reversePrefix(String word, char ch) {
        int pos = word.indexOf(ch);
        if (pos < 0) return word;
        char[] arr = word.toCharArray();
        for (int l = 0, r = pos; l < r; l++, r--) {
            char tmp = arr[l];
            arr[l] = arr[r];
            arr[r] = tmp;
        }
        return new String(arr);
    }
}

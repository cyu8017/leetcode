// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution {
    public boolean canMakeSubsequence(String str1, String str2) {
        int j = 0;
        for (int i = 0; i < str1.length() && j < str2.length(); i++) {
            char a = str1.charAt(i), b = str2.charAt(j);
            if (a == b || (a - 'a' + 1) % 26 == (b - 'a')) j++;
        }
        return j == str2.length();
    }
}

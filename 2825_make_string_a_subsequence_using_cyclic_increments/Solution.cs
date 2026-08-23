// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

public class Solution {
    public bool CanMakeSubsequence(string str1, string str2) {
        int j = 0;
        for (int i = 0; i < str1.Length && j < str2.Length; i++) {
            char a = str1[i], b = str2[j];
            if (a == b || (a - 'a' + 1) % 26 == (b - 'a')) j++;
        }
        return j == str2.Length;
    }
}

// LeetCode 0557 - Reverse Words in a String III
// https://leetcode.com/problems/reverse-words-in-a-string-iii/

public class Solution {
    public string ReverseWords(string s) {
        char[] arr = s.ToCharArray();
        int n = arr.Length;
        int start = 0;
        for (int i = 0; i <= n; ++i) {
            if (i == n || arr[i] == ' ') {
                System.Array.Reverse(arr, start, i - start);
                start = i + 1;
            }
        }
        return new string(arr);
    }
}

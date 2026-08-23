// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

public class Solution {
    public string ReverseOnlyLetters(string s) {
        char[] arr = s.ToCharArray();
        int i = 0, j = arr.Length - 1;
        while (i < j) {
            while (i < j && !char.IsLetter(arr[i])) i++;
            while (i < j && !char.IsLetter(arr[j])) j--;
            (arr[i], arr[j]) = (arr[j], arr[i]);
            i++;
            j--;
        }
        return new string(arr);
    }
}

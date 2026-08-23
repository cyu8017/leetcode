// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

public class Solution {
    public string ShiftingLetters(string s, int[] shifts) {
        char[] arr = s.ToCharArray();
        int total = 0;
        for (int i = arr.Length - 1; i >= 0; i--) {
            total = (total + shifts[i]) % 26;
            arr[i] = (char)((arr[i] - 'a' + total) % 26 + 'a');
        }
        return new string(arr);
    }
}

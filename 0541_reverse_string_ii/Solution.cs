// LeetCode 0541 - Reverse String II
// https://leetcode.com/problems/reverse-string-ii/

public class Solution {
    public string ReverseStr(string s, int k) {
        char[] chars = s.ToCharArray();
        for (int start = 0; start < chars.Length; start += 2 * k) {
            int end = System.Math.Min(start + k, chars.Length) - 1;
            int left = start;
            int right = end;
            while (left < right) {
                char temp = chars[left];
                chars[left] = chars[right];
                chars[right] = temp;
                left++;
                right--;
            }
        }
        return new string(chars);
    }
}

// LeetCode 0541 - Reverse String II
// https://leetcode.com/problems/reverse-string-ii/

class Solution {
    public String reverseStr(String s, int k) {
        char[] chars = s.toCharArray();
        for (int start = 0; start < chars.length; start += 2 * k) {
            int end = Math.min(start + k, chars.length) - 1;
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
        return new String(chars);
    }
}

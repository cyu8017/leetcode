// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

class Solution {
    public String reversePrefix(String s, int k) {
        char[] arr = s.toCharArray();
        reverse(arr, 0, 0 + k);
        return new String(arr);
    }

    private void reverse(char[] a) { reverse(a, 0, a.length); }
    private void reverse(char[] a, int l, int r) {
        for (int i = l, j = r - 1; i < j; i++, j--) {
            char t = a[i]; a[i] = a[j]; a[j] = t;
        }
    }
    private void reverse(int[] a) { reverse(a, 0, a.length); }
    private void reverse(int[] a, int l, int r) {
        for (int i = l, j = r - 1; i < j; i++, j--) {
            int t = a[i]; a[i] = a[j]; a[j] = t;
        }
    }
}

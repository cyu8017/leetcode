// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

class Solution {
    public int minimumFlips(int n) {
        String s;
        long x = n;
        if (x == 0) s = "0";
        else {
            var sb = new StringBuilder();
            while (x > 0) {
                sb.append((char)('0' + (x & 1)));
                x >>= 1;
            }
            char[] arr = sb.toString().toCharArray();
            reverse(arr);
            s = new String(arr);
        }
        int m = s.length(), cnt = 0;
        for (int i = 0; i < m / 2; i++) {
            if (s.charAt(i) != s.charAt(m - i - 1)) cnt++;
        }
        return cnt * 2;
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

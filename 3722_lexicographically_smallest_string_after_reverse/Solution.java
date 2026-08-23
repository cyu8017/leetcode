// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

class Solution {
    public String lexSmallest(String s) {
        String ans = s;
        int n = s.length();
        for (int k = 1; k <= n; k++) {
            char[] a1 = s.toCharArray();
            reverse(a1, 0, 0 + k);
            String t1 = new String(a1);
            char[] a2 = s.toCharArray();
            reverse(a2, n - k, n - k + k);
            String t2 = new String(a2);
            if (t1.compareTo(ans) < 0) ans = t1;
            if (t2.compareTo(ans) < 0) ans = t2;
        }
        return ans;
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

// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

class Solution {
    public String lexSmallest(String s) {
        int n = s.length();
        String best = s;
        for (int i = 1; i <= n; i++) {
            char[] t = s.toCharArray();
            reverse(t, 0, 0 + i);
            String ts = new String(t);
            if (ts.compareTo(best) < 0) best = ts;
        }
        for (int i = 0; i < n; i++) {
            char[] t = s.toCharArray();
            reverse(t, i, i + n - i);
            String ts = new String(t);
            if (ts.compareTo(best) < 0) best = ts;
        }
        return best;
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

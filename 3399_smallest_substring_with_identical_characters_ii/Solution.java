// LeetCode 3399 - Smallest Substring With Identical Characters II
// https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

class Solution {
    public int minLength(String s, int numOps) {
        int n = s.length();
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(s, n, numOps, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean ok(String s, int n, int numOps, int L) {
        int ops = 0;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && s.charAt(j) == s.charAt(i)) j++;
            ops += (j - i) / (L + 1);
            i = j;
        }
        return ops <= numOps;
    }
}

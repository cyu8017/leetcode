// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

class Solution {
    private int n;
    private int[] order;
    private long total;

    private long countValid(int t) {
        boolean[] star = new boolean[n];
        for (int i = 0; i <= t; i++) star[order[i]] = true;
        long invalid = 0;
        for (int i = 0; i < n;) {
            if (star[i]) {
                i++;
                continue;
            }
            int j = i;
            while (j < n && !star[j]) j++;
            long L = j - i;
            invalid += L * (L + 1) / 2;
            i = j;
        }
        return total - invalid;
    }

    public int minTime(String s, int[] order, int k) {
        this.order = order;
        n = s.length();
        total = 1L * n * (n + 1) / 2;
        if (k > total) return -1;
        int lo = 0, hi = n - 1, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (countValid(mid) >= k) {
                ans = mid;
                hi = mid - 1;
            } else lo = mid + 1;
        }
        return ans;
    }
}

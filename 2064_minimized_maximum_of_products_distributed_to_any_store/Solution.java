// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution {
    public int minimizedMaximum(int n, int[] quantities) {
        int lo = 1, hi = 0;
        for (int q : quantities) hi = Math.max(hi, q);
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (can(n, quantities, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean can(int n, int[] quantities, int x) {
        int need = 0;
        for (int q : quantities) {
            need += (q + x - 1) / x;
            if (need > n) return false;
        }
        return true;
    }
}

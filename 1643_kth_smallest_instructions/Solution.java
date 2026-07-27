// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/

class Solution {
    public String kthSmallestPath(int[] destination, int k) {
        int v = destination[0], h = destination[1];
        StringBuilder ans = new StringBuilder();
        while (h + v > 0) {
            if (h > 0) {
                long count = comb(h + v - 1, v);
                if (k <= count) {
                    ans.append('H');
                    h--;
                    continue;
                }
                k -= (int) count;
            }
            ans.append('V');
            v--;
        }
        return ans.toString();
    }

    private long comb(int n, int r) {
        if (r < 0 || r > n) return 0;
        r = Math.min(r, n - r);
        long res = 1;
        for (int i = 1; i <= r; i++) {
            res = res * (n - r + i) / i;
        }
        return res;
    }
}

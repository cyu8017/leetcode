// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

class Solution {
    public long minTotalTime(int[] forward, int[] backward, int[] queries) {
        int n = forward.length;
        int sumB = 0;
        for (int v : backward) sumB += v;
        int[] pf = new int[n + 1], pb = new int[n + 1];
        for (int i = 0; i < n; i++) {
            pf[i + 1] = pf[i] + forward[i];
            pb[i + 1] = pb[i] + backward[i];
        }
        long ans = 0;
        int pos = 0;
        for (int q : queries) {
            int r = 0;
            if (q < pos) r = pf[n];
            r += pf[q] - pf[pos];
            int l = 0;
            if (q > pos) l = sumB;
            l += pb[pos] - pb[q];
            ans += Math.min(l, r);
            pos = q;
        }
        return ans;
    }
}

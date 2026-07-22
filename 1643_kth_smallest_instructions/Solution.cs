// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/

using System.Text;

public class Solution {
    public string KthSmallestPath(int[] destination, int k) {
        int v = destination[0], h = destination[1];
        var ans = new StringBuilder();
        while (h + v > 0) {
            if (h > 0) {
                long count = Comb(h + v - 1, v);
                if (k <= count) { ans.Append('H'); h--; continue; }
                k -= (int)count;
            }
            ans.Append('V');
            v--;
        }
        return ans.ToString();
    }

    private static long Comb(int n, int r) {
        if (r < 0 || r > n) return 0;
        r = System.Math.Min(r, n - r);
        long res = 1;
        for (int i = 1; i <= r; i++) res = res * (n - r + i) / i;
        return res;
    }
}

// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

using System;
using System.Linq;

public class Solution {
    public int MinimizedMaximum(int n, int[] quantities) {
        bool Can(int x) {
            int need = 0;
            foreach (int q in quantities) {
                need += (q + x - 1) / x;
                if (need > n) return false;
            }
            return true;
        }
        int lo = 1, hi = quantities.Max();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (Can(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}

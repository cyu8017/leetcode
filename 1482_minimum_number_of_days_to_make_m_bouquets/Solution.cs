// LeetCode 1482 - Minimum Number Of Days To Make M Bouquets
// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

using System.Linq;
public class Solution {
    public int MinDays(int[] bloomDay, int m, int k) {
        if ((long)m * k > bloomDay.Length) return -1;
        bool Possible(int day) {
            int bouquets = 0, run = 0;
            foreach (int x in bloomDay) {
                run = x <= day ? run + 1 : 0;
                if (run == k) { bouquets++; run = 0; }
            }
            return bouquets >= m;
        }
        int lo = bloomDay.Min(), hi = bloomDay.Max();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (Possible(mid)) hi = mid; else lo = mid + 1;
        }
        return lo;
    }
}

// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

using System.Linq;

public class Solution {
    public int MaximizeSweetness(int[] sweetness, int k) {
        int lo = 1, hi = sweetness.Sum() / (k + 1);
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int pieces = 0, current = 0;
            foreach (int value in sweetness) {
                current += value;
                if (current >= mid) {
                    pieces++;
                    current = 0;
                }
            }
            if (pieces >= k + 1) lo = mid + 1;
            else hi = mid - 1;
        }
        return hi;
    }
}

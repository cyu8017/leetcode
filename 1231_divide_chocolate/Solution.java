// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

class Solution {
    public int maximizeSweetness(int[] sweetness, int k) {
        int lo = 1, hi = 0;
        for (int x : sweetness) hi += x;
        hi /= k + 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int pieces = 0, current = 0;
            for (int value : sweetness) {
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


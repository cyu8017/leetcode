// LeetCode 1954 - Minimum Garden Perimeter to Collect Enough Apples
// https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

public class Solution {
    public long MinimumPerimeter(long neededApples) {
        long lo = 1, hi = 100000;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            long apples = 2 * mid * (mid + 1) * (2 * mid + 1);
            if (apples >= neededApples) hi = mid;
            else lo = mid + 1;
        }
        return 8 * lo;
    }
}
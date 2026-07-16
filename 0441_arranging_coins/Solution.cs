// LeetCode 0441 - Arranging Coins
// https://leetcode.com/problems/arranging-coins/

public class Solution {
    public int ArrangeCoins(int n) {
        int low = 0;
        int high = n;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if ((long)mid * (mid + 1) / 2 <= n) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return high;
    }
}

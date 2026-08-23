// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

public class Solution {
    public int LateFee(int[] daysLate) {
        int F(int x) {
            if (x == 1) return 1;
            if (x > 5) return 3 * x;
            return 2 * x;
        }
        int ans = 0;
        foreach (int x in daysLate) ans += F(x);
        return ans;
    }
}

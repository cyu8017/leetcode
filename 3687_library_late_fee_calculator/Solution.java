// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

class Solution {
    private int fee(int x) {
        if (x == 1) return 1;
        if (x > 5) return 3 * x;
        return 2 * x;
    }

    public int lateFee(int[] daysLate) {
        int ans = 0;
        for (int x : daysLate) ans += fee(x);
        return ans;
    }
}

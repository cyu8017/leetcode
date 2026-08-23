// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

import java.util.Arrays;

class Solution {
    public double minTime(int n, int k, int m, int[] time, double[] mul) {
        int[] t = time.clone();
        Arrays.sort(t);
        double total = 0;
        int stage = 0, left = n;
        while (left > 0) {
            int take = Math.min(k, left);
            int slow = t[left - 1];
            total += (double)slow * mul[stage % m];
            left -= take;
            stage++;
            if (left > 0) {
                total += (double)t[0] * mul[stage % m];
                stage++;
            }
        }
        return total;
    }
}

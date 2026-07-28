// LeetCode 1052 - Grumpy Bookstore Owner
// https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int base = 0;
        for (int i = 0; i < customers.length; i++) {
            if (grumpy[i] == 0) {
                base += customers[i];
            }
        }
        int gain = 0, best = 0;
        for (int i = 0; i < customers.length; i++) {
            if (grumpy[i] == 1) {
                gain += customers[i];
            }
            if (i >= minutes && grumpy[i - minutes] == 1) {
                gain -= customers[i - minutes];
            }
            best = Math.max(best, gain);
        }
        return base + best;
    }
}

// LeetCode 1052 - Grumpy Bookstore Owner
// https://leetcode.com/problems/grumpy-bookstore-owner/

public class Solution {
    public int MaxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int n = customers.Length;
        int baseSatisfied = 0;
        for (int i = 0; i < n; i++) {
            if (grumpy[i] == 0) {
                baseSatisfied += customers[i];
            }
        }
        int gain = 0, best = 0;
        for (int i = 0; i < n; i++) {
            if (grumpy[i] == 1) {
                gain += customers[i];
            }
            if (i >= minutes && grumpy[i - minutes] == 1) {
                gain -= customers[i - minutes];
            }
            if (gain > best) {
                best = gain;
            }
        }
        return baseSatisfied + best;
    }
}

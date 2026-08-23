// LeetCode 0440 - K-th Smallest in Lexicographical Order
// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution {
    public int findKthNumber(int n, int k) {
        int current = 1;
        k--;

        while (k > 0) {
            long steps = countSteps(n, current, current + 1L);
            if (steps <= k) {
                current++;
                k -= steps;
            } else {
                current *= 10;
                k--;
            }
        }

        return current;
    }

    private long countSteps(int n, long first, long last) {
        long steps = 0;
        while (first <= n) {
            steps += Math.min(n + 1L, last) - first;
            first *= 10;
            last *= 10;
        }
        return steps;
    }
}

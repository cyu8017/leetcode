// LeetCode 1492 - The Kth Factor Of N
// https://leetcode.com/problems/the-kth-factor-of-n/

public class Solution {
    public int KthFactor(int n, int k) {
        for (int x = 1; x <= n; x++)
            if (n % x == 0) { k--; if (k == 0) return x; }
        return -1;
    }
}

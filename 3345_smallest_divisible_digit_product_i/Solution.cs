// LeetCode 3345 - Smallest Divisible Digit Product I
// https://leetcode.com/problems/smallest-divisible-digit-product-i/

public class Solution {
    public int SmallestNumber(int n, int t) {
        for (int x = n;; x++) {
            int p = 1, y = x;
            while (y > 0) {
                p *= y % 10;
                y /= 10;
            }
            if (p % t == 0) return x;
        }
    }
}

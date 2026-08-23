// LeetCode 0069 - Sqrt(x)
// https://leetcode.com/problems/sqrtx/

public class Solution {
    public int MySqrt(int x) {
        if (x < 2) {
            return x;
        }

        int left = 2;
        int right = x / 2;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            long square = (long)mid * mid;
            if (square == x) {
                return mid;
            }
            if (square < x) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return right;
    }
}

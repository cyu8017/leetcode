// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

public class Solution {
    public long MakeIntegerBeautiful(long n, int target) {
        int DigitSum(long x) {
            int s = 0;
            while (x > 0) {
                s += (int)(x % 10);
                x /= 10;
            }
            return s;
        }
        long orig = n, pow10 = 1;
        while (DigitSum(n) > target) {
            n = n / 10 + 1;
            pow10 *= 10;
        }
        return n * pow10 - orig;
    }
}

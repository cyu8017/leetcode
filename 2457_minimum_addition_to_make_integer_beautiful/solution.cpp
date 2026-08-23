// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

class Solution {
public:
    long long makeIntegerBeautiful(long long n, int target) {
        auto digitSum = [](long long x) {
            int s = 0;
            while (x > 0) {
                s += (int)(x % 10);
                x /= 10;
            }
            return s;
        };
        long long orig = n, pow10 = 1;
        while (digitSum(n) > target) {
            n = n / 10 + 1;
            pow10 *= 10;
        }
        return n * pow10 - orig;
    }
};

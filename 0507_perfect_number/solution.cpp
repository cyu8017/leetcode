// LeetCode 0507 - Perfect Number
// https://leetcode.com/problems/perfect-number/

class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) {
            return false;
        }
        int total = 1;
        for (int divisor = 2; divisor * divisor <= num; ++divisor) {
            if (num % divisor == 0) {
                total += divisor;
                const int pair = num / divisor;
                if (pair != divisor) {
                    total += pair;
                }
            }
        }
        return total == num;
    }
};

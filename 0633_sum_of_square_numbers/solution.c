// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/

#include <math.h>
#include <stdbool.h>

bool judgeSquareSum(int c) {
    long long left = 0;
    long long right = (long long)sqrt((double)c);
    while (left <= right) {
        long long sum = left * left + right * right;
        if (sum == c) {
            return true;
        }
        if (sum < c) {
            left++;
        } else {
            right--;
        }
    }
    return false;
}

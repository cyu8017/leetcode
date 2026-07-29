// LeetCode 1404 - Number of Steps to Reduce a Number in Binary Representation to One
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

#include <string.h>

int numSteps(char* s) {
    int n = (int)strlen(s);
    int steps = 0, carry = 0;
    for (int i = n - 1; i >= 1; i--) {
        int value = (s[i] - '0') + carry;
        if (value == 1) { steps += 2; carry = 1; }
        else steps += 1;
    }
    return steps + carry;
}

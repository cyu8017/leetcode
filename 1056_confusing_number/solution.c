// LeetCode 1056 - Confusing Number
// https://leetcode.com/problems/confusing-number/

#include <stdbool.h>

bool confusingNumber(int n) {
    int rotate[10];
    for (int i = 0; i < 10; i++) {
        rotate[i] = -1;
    }
    rotate[0] = 0;
    rotate[1] = 1;
    rotate[6] = 9;
    rotate[8] = 8;
    rotate[9] = 6;
    int original = n;
    int rotated = 0;
    while (n > 0) {
        int d = n % 10;
        if (rotate[d] < 0) {
            return false;
        }
        rotated = rotated * 10 + rotate[d];
        n /= 10;
    }
    return rotated != original;
}

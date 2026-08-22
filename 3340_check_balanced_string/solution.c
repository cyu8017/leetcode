// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

#include <stdbool.h>

bool isBalanced(char* num) {
    int even = 0, odd = 0;
    for (int i = 0; num[i]; i++) {
        if (i % 2 == 0) even += num[i] - '0';
        else odd += num[i] - '0';
    }
    return even == odd;
}

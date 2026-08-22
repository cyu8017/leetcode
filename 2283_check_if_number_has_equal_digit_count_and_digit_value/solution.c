// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

#include <stdbool.h>
#include <string.h>

bool digitCount(char* num) {
    int cnt[10] = {0};
    int n = (int)strlen(num);
    for (int i = 0; i < n; i++) {
        cnt[num[i] - '0']++;
    }
    for (int i = 0; i < n; i++) {
        if (cnt[i] != num[i] - '0') return false;
    }
    return true;
}

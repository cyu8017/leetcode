// LeetCode 0420 - Strong Password Checker
// https://leetcode.com/problems/strong-password-checker/

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int max_int(int a, int b) {
    return a > b ? a : b;
}

static int min_int(int a, int b) {
    return a < b ? a : b;
}

int strongPasswordChecker(char* password) {
    int length = (int)strlen(password);
    int missing = 3;
    bool hasLower = false;
    bool hasUpper = false;
    bool hasDigit = false;

    for (int index = 0; index < length; index++) {
        unsigned char ch = (unsigned char)password[index];
        if (islower(ch)) {
            hasLower = true;
        } else if (isupper(ch)) {
            hasUpper = true;
        } else if (isdigit(ch)) {
            hasDigit = true;
        }
    }
    if (hasLower) {
        missing--;
    }
    if (hasUpper) {
        missing--;
    }
    if (hasDigit) {
        missing--;
    }

    int replace = 0;
    int oneRepeat = 0;
    int twoRepeat = 0;
    int index = 0;
    while (index < length) {
        int run = 1;
        while (index + run < length && password[index + run] == password[index]) {
            run++;
        }
        if (run >= 3) {
            replace += run / 3;
            if (run % 3 == 0) {
                oneRepeat++;
            } else if (run % 3 == 1) {
                twoRepeat++;
            }
        }
        index += run;
    }

    if (length < 6) {
        return max_int(6 - length, missing);
    }
    if (length <= 20) {
        return max_int(missing, replace);
    }

    int deleteCount = length - 20;
    replace -= min_int(deleteCount, oneRepeat);
    deleteCount -= min_int(deleteCount, oneRepeat);
    replace -= min_int(deleteCount / 2, twoRepeat);
    deleteCount -= min_int(deleteCount / 2, twoRepeat) * 2;
    replace -= deleteCount / 3;
    return length - 20 + max_int(missing, replace);
}

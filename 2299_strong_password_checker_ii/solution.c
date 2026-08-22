// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

#include <stdbool.h>
#include <string.h>

bool strongPasswordCheckerII(char* password) {
    int n = (int)strlen(password);
    if (n < 8) return false;
    const char* special = "!@#$%^&*()-+";
    bool hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;
    for (int i = 0; i < n; i++) {
        char c = password[i];
        if (i > 0 && c == password[i - 1]) return false;
        if (c >= 'a' && c <= 'z') hasLower = true;
        else if (c >= 'A' && c <= 'Z') hasUpper = true;
        else if (c >= '0' && c <= '9') hasDigit = true;
        else {
            for (int j = 0; special[j]; j++) {
                if (c == special[j]) { hasSpecial = true; break; }
            }
        }
    }
    return hasLower && hasUpper && hasDigit && hasSpecial;
}

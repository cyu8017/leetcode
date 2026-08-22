// LeetCode 3941 - Password Strength
// https://leetcode.com/problems/password-strength/

#include <ctype.h>
#include <stdbool.h>

int passwordStrength(char* password) {
    bool seen[256] = {0};
    int ans = 0;
    for (int i = 0; password[i]; i++) {
        unsigned char ch = (unsigned char)password[i];
        if (seen[ch]) continue;
        seen[ch] = true;
        if (islower(ch)) ans += 1;
        else if (isupper(ch)) ans += 2;
        else if (isdigit(ch)) ans += 3;
        else ans += 5;
    }
    return ans;
}

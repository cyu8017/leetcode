// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

#include <ctype.h>
#include <string.h>

int countKeyChanges(char* s) {
    int n = (int)strlen(s);
    int ans = 0;
    for (int i = 1; i < n; i++) {
        if (tolower((unsigned char)s[i]) != tolower((unsigned char)s[i - 1])) ans++;
    }
    return ans;
}

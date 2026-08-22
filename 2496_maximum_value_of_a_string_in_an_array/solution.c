// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

#include <string.h>
#include <stdbool.h>

int maximumValue(char** strs, int strsSize) {
    int ans = 0;
    for (int t = 0; t < strsSize; t++) {
        char* s = strs[t];
        bool allDigit = true;
        int val = 0;
        int len = (int)strlen(s);
        for (int i = 0; i < len; i++) {
            if (s[i] < '0' || s[i] > '9') { allDigit = false; break; }
            val = val * 10 + (s[i] - '0');
        }
        if (!allDigit) val = len;
        if (val > ans) ans = val;
    }
    return ans;
}

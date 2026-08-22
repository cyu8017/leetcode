// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

#include <stdlib.h>
#include <string.h>

char* removeTrailingZeros(char* num) {
    int i = (int)strlen(num) - 1;
    while (i >= 0 && num[i] == '0') i--;
    char* ans = (char*)malloc((size_t)i + 2);
    memcpy(ans, num, (size_t)i + 1);
    ans[i + 1] = '\0';
    return ans;
}

// LeetCode 3498 - Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/

#include <string.h>

int reverseDegree(char* s) {
    int ans = 0;
    for (int i = 0; s[i]; i++) {
        ans += (26 - (s[i] - 'a')) * (i + 1);
    }
    return ans;
}

// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

#include <string.h>
#include <stdbool.h>

static bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int beautifulSubstrings(char* s, int k) {
    int ans = 0, n = (int)strlen(s);
    for (int i = 0; i < n; i++) {
        int v = 0, c = 0;
        for (int j = i; j < n; j++) {
            if (isVowel(s[j])) v++; else c++;
            if (v == c && (v * c) % k == 0) ans++;
        }
    }
    return ans;
}

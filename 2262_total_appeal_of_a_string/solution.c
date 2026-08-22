// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

#include <string.h>

long long appealSum(char* s) {
    int last[26];
    for (int i = 0; i < 26; i++) last[i] = -1;
    long long ans = 0, cur = 0;
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        cur += i - last[c];
        last[c] = i;
        ans += cur;
    }
    return ans;
}

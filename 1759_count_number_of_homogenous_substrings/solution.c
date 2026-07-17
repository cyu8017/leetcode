// LeetCode 1759 - Count Number of Homogenous Substrings
// https://leetcode.com/problems/count-number-of-homogenous-substrings/

#include <string.h>

int countHomogenous(char* s) {
    const long long MOD = 1000000007LL;
    long long ans = 0;
    int n = (int)strlen(s);
    int i = 0;
    while (i < n) {
        int j = i;
        while (j < n && s[j] == s[i]) {
            j++;
        }
        long long length = j - i;
        ans = (ans + length * (length + 1) / 2) % MOD;
        i = j;
    }
    return (int)ans;
}

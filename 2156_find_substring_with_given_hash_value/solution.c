// LeetCode 2156 - Find Substring With Given Hash Value
// https://leetcode.com/problems/find-substring-with-given-hash-value/

#include <stdlib.h>
#include <string.h>

char* subStrHash(char* s, int power, int modulo, int k, int hashValue) {
    int n = (int)strlen(s);
    long long pk = 1, mod = modulo;
    for (int i = 0; i < k - 1; i++) pk = pk * power % mod;
    long long h = 0;
    int ans = 0;
    for (int i = n - 1; i >= n - k; i--)
        h = (h * power + (s[i] - 'a' + 1)) % mod;
    if (h == hashValue) ans = n - k;
    for (int i = n - k - 1; i >= 0; i--) {
        h = (h - (s[i + k] - 'a' + 1) * pk % mod + mod) % mod;
        h = (h * power + (s[i] - 'a' + 1)) % mod;
        if (h == hashValue) ans = i;
    }
    char* out = (char*)malloc((size_t)k + 1);
    memcpy(out, s + ans, (size_t)k);
    out[k] = '\0';
    return out;
}

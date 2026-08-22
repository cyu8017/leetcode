// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

#include <string.h>
#include <stdbool.h>

static bool check3138(char* s, int n, int* cnt, int k) {
    for (int i = 0; i < n; i += k) {
        int cnt1[26] = {0};
        for (int j = i; j < i + k; j++) cnt1[s[j] - 'a']++;
        for (int j = 0; j < 26; j++)
            if (cnt1[j] * (n / k) != cnt[j]) return false;
    }
    return true;
}

int minAnagramLength(char* s) {
    int n = (int)strlen(s);
    int cnt[26] = {0};
    for (int i = 0; i < n; i++) cnt[s[i] - 'a']++;
    for (int i = 1; ; i++) {
        if (n % i == 0 && check3138(s, n, cnt, i)) return i;
    }
}

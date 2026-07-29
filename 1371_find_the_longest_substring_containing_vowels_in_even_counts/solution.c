// LeetCode 1371 - Find the Longest Substring Containing Vowels in Even Counts
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

#include <string.h>

int findTheLongestSubstring(char* s) {
    int first[32];
    for (int i = 0; i < 32; i++) first[i] = -2;
    first[0] = -1;
    int mask = 0, ans = 0;
    const char* vowels = "aeiou";
    for (int i = 0; s[i]; i++) {
        const char* p = strchr(vowels, s[i]);
        if (p) mask ^= 1 << (p - vowels);
        if (first[mask] != -2) {
            int len = i - first[mask];
            if (len > ans) ans = len;
        } else first[mask] = i;
    }
    return ans;
}

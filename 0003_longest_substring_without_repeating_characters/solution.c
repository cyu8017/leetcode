// LeetCode 0003 - Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int last[256];
    for (int i = 0; i < 256; i++) {
        last[i] = -1;
    }

    int best = 0;
    int start = 0;
    int n = (int)strlen(s);

    for (int i = 0; i < n; i++) {
        unsigned char ch = (unsigned char)s[i];
        if (last[ch] >= start) {
            start = last[ch] + 1;
        }
        last[ch] = i;
        if (i - start + 1 > best) {
            best = i - start + 1;
        }
    }

    return best;
}

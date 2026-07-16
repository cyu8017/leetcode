// LeetCode 0395 - Longest Substring with At Least K Repeating Characters
// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

#include <string.h>

static int maxInt(int left, int right) {
    return left > right ? left : right;
}

static int longestSubstringImpl(const char* s, int k) {
    if (s[0] == '\0') {
        return 0;
    }

    int counts[256] = {0};
    for (int index = 0; s[index] != '\0'; index++) {
        counts[(unsigned char)s[index]] += 1;
    }

    for (int ch = 0; ch < 256; ch++) {
        if (counts[ch] > 0 && counts[ch] < k) {
            int best = 0;
            char part[100005];
            int partLength = 0;

            for (int index = 0; s[index] != '\0'; index++) {
                if ((unsigned char)s[index] == ch) {
                    part[partLength] = '\0';
                    best = maxInt(best, longestSubstringImpl(part, k));
                    partLength = 0;
                } else {
                    part[partLength++] = s[index];
                }
            }
            part[partLength] = '\0';
            best = maxInt(best, longestSubstringImpl(part, k));
            return best;
        }
    }

    return (int)strlen(s);
}

int longestSubstring(char* s, int k) {
    return longestSubstringImpl(s, k);
}

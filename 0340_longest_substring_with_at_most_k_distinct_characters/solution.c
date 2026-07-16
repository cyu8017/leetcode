// LeetCode 0340 - Longest Substring with At Most K Distinct Characters
// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

#include <string.h>

int lengthOfLongestSubstringKDistinct(char* s, int k) {
    if (k == 0) {
        return 0;
    }

    int length = (int)strlen(s);
    int counts[256] = {0};
    int distinct = 0;
    int left = 0;
    int best = 0;

    for (int right = 0; right < length; right++) {
        unsigned char ch = (unsigned char)s[right];
        if (counts[ch] == 0) {
            distinct += 1;
        }
        counts[ch] += 1;

        while (distinct > k) {
            unsigned char leftChar = (unsigned char)s[left];
            counts[leftChar] -= 1;
            if (counts[leftChar] == 0) {
                distinct -= 1;
            }
            left += 1;
        }

        int window = right - left + 1;
        if (window > best) {
            best = window;
        }
    }

    return best;
}

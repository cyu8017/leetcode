// LeetCode 2168 - Unique Substrings With Equal Digit Frequency
// https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// rolling hash set for substrings
typedef struct { unsigned long long h; bool used; } HS;

int equalDigitFrequency(char* s) {
    int n = (int)strlen(s);
    int cap = 1 << 18;
    HS* set = (HS*)calloc((size_t)cap, sizeof(HS));
    int count = 0;
    for (int i = 0; i < n; i++) {
        int freq[10] = {0};
        int maxf = 0, kinds = 0;
        unsigned long long h = 0;
        for (int j = i; j < n; j++) {
            int d = s[j] - '0';
            if (freq[d] == 0) kinds++;
            freq[d]++;
            if (freq[d] > maxf) maxf = freq[d];
            h = h * 11 + (unsigned long long)(d + 1);
            if (maxf * kinds == j - i + 1) {
                unsigned idx = (unsigned)(h % (unsigned)cap);
                for (;;) {
                    if (!set[idx].used) { set[idx].used = true; set[idx].h = h; count++; break; }
                    if (set[idx].h == h) break;
                    idx = (idx + 1) % (unsigned)cap;
                }
            }
        }
    }
    free(set);
    return count;
}

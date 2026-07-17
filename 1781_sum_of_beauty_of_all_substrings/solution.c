// LeetCode 1781 - Sum of Beauty of All Substrings
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

#include <limits.h>
#include <string.h>

int beautySum(char* s) {
    int n = strlen(s);
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int freq[26] = {0};
        for (int j = i; j < n; j++) {
            freq[s[j] - 'a']++;
            int lo = INT_MAX;
            int hi = 0;
            for (int c = 0; c < 26; c++) {
                if (freq[c] > 0) {
                    if (freq[c] < lo) lo = freq[c];
                    if (freq[c] > hi) hi = freq[c];
                }
            }
            ans += hi - lo;
        }
    }
    return ans;
}
